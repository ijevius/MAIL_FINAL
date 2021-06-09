import logging
import shutil
import sys
import os

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from api.client import ApiClient
from db.mysql.client import MysqlClient
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='123456', db_name='technoatom')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()

def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:81/login')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')

@pytest.fixture(scope='function')
def api_client(config):
    return ApiClient(config['url'])

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    debug_log = request.config.getoption('--debug_log')

    '''if request.config.getoption('--selenoid'):
        selenoid = 'http://127.0.0.1:4444'
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
    else:'''
    selenoid = None
    vnc = False

    return {'url': url, 'browser': browser, 'debug_log': debug_log, 'selenoid': selenoid, 'vnc': vnc}


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_test_dir = 'C:\\tests'
    else:
        base_test_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):  # execute only once on main worker
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    # save to config for all workers
    config.base_test_dir = base_test_dir

@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.get(url)
    browser.minimize_window()
    yield browser
    browser.close()


@pytest.fixture(scope='function', autouse=True)
def logger(test_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')

    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)