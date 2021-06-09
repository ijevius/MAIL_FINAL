import pytest
from _pytest.fixtures import FixtureRequest

from db.mysql.builder import MySQLBuilder
from ui.pages.login_page import LoginPage


class BaseCase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, login_page, logger, api_client, mysql_client):
        self.driver = driver
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.config = config
        self.logger = logger
        self.logger.debug('Initial setup done!')
        self.api_client = api_client
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.prepare()