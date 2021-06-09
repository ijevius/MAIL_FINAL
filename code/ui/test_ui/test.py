import pytest
from faker import Faker

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base import BaseCase
from ui.locators import *

from db.mysql.models import User

fake = Faker()

@pytest.mark.UI
class TestUI(BaseCase):

    def test_good_login(self):
        self.login_page.make_login()
        got_logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.LOGOUT_BUTTON_LOCATOR)
        )
        assert got_logout_button

    def test_good_login_badonlypassword(self):
        self.login_page.make_login(password="x")
        got_error_block = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.INVALID_USERNAMEPASSWORD_LOCATOR)
        )
        assert got_error_block

    def test_short_login(self):
        self.login_page.make_login(password="xwegwegwegwg", login='x')
        got_error_block = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.SHORT_LOGIN_LOCATOR)
        )
        assert got_error_block

    def test_has_random_fact(self):
        self.login_page.make_login()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.RANDOM_FACT_LOCATOR)
        )

    def test_api_click(self):
        self.login_page.make_login()
        block = self.login_page.find(WelcomePageLocators.API_PIC_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.WIKI_API_LOCATOR)
        )

    def test_pm_click(self):
        self.login_page.make_login()
        block = self.login_page.find(WelcomePageLocators.PM_ARTICLE_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.PM_TITLE_LOCATOR)
        )

    def test_smtp_click(self):
        self.login_page.make_login()
        block = self.login_page.find(WelcomePageLocators.SMTP_PIC_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.WIKI_SMTP_LOCATOR)
        )
        #self.driver.close()

    def test_pyhistory_click(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.PYTHON_BLOCK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.PY_HISTORY_LINK_LOCATOR, 15)
        block.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.PYHISTORY_TITLE_LOCATOR)
        )

    def test_flask_click(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.PYTHON_BLOCK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.FLASK_LINK_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.FLASK_LOGO_LOCATOR)
        )
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'W')
        #self.driver.close()

    def test_linux_click(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.LINUX_BLOCK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.CENTOS_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(WelcomePageLocators.CENTOS_ANYWHERE_LOCATOR))

    def test_wireshark_news(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.NETWORK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.WIRE_NEWS_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.WIRE_2OK_LOCATOR)
        )
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'W')
        #self.driver.close()

    def test_wireshark_download(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.NETWORK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.WIREDOWNLOAD_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.WIREDOWN_OK_LOCATOR)
        )
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'W')

    def test_examples(self):
        self.login_page.make_login()
        self.login_page.move_to(WelcomePageLocators.NETWORK_LOCATOR[1])
        block = self.login_page.find(WelcomePageLocators.TCP_EXAMPLES_LOCATOR, 15)
        block.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(WelcomePageLocators.TCP_OK_LOCATOR)
        )
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'W')
        self.driver.window_handles[0]
        #self.driver.close()

    def test_logout(self):
        self.login_page.make_login()
        button = self.login_page.find(WelcomePageLocators.LOGOUT_BUTTON_LOCATOR, 15)
        button.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_INPUT_LOCATOR)
        )

    def test_goreg(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR)
        )

    def test_reg_shortlogin(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        login_input.send_keys("tes")
        email_input.send_keys(fake.email())
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.SHORT_LOGIN_LOCATOR)
        )

    def test_reg_diffpasswds(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        login_input.send_keys(fake.first_name()+" "+fake.last_name())
        email_input.send_keys(fake.email())
        password_input.send_keys("12345")
        password2_input.send_keys("12345342")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.MATCH_LOCATOR)
        )

    def test_reg_shortemail(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        login_input.send_keys(fake.first_name() + " " + fake.last_name())
        email_input.send_keys("boss")
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.SHORT_EMAIL_LOCATOR)
        )

    '''
    def test_reg_goodnocheckbox(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        #checkbox.click()
        login_input.send_keys(fake.first_name() + " " + fake.last_name())
        email_input.send_keys(fake.email())
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.SHORT_EMAIL_LOCATOR)
        )'''

    def test_reg_bademail(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        login_input.send_keys(fake.first_name() + " " + fake.last_name())
        email_input.send_keys("boss3535132512351235")
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.INVALID_EMAIL_LOCATOR)
        )

    def test_gologinfromreg(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        self.login_page.click(RegistrationPageLocators.LOGIN_HINT_LOCATOR, 15)
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.REG_HINT_LOCATOR)
        )

    def test_usernamerepeat(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        login_input.send_keys(last_user.username)
        email_input.send_keys(fake.email())
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.EXISTS_LOCATOR)
        )

    def test_emailrepeat(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        last_user = self.mysql.session.query(User).order_by(-User.id).first()
        login_input.send_keys("3498n309v")
        email_input.send_keys(last_user.email)
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_EXISTS_LOCATOR)
        )

    def test_longusername(self):
        self.login_page.click(LoginPageLocators.REG_HINT_LOCATOR, 15)
        login_input = self.login_page.find(RegistrationPageLocators.LOGIN_INPUT_LOCATOR, 5)
        email_input = self.login_page.find(RegistrationPageLocators.EMAIL_INPUT_LOCATOR, 5)
        password_input = self.login_page.find(RegistrationPageLocators.PASSWORD1_INPUT_LOCATOR, 5)
        password2_input = self.login_page.find(RegistrationPageLocators.PASSWORD2_INPUT_LOCATOR, 5)
        checkbox = self.login_page.find(RegistrationPageLocators.TERM_CHECKBOX_LOCATOR, 5)
        go = self.login_page.find(RegistrationPageLocators.REG_BUTTON_LOCATOR, 5)
        checkbox.click()
        login_input.send_keys("x"*20)
        email_input.send_keys(fake.email())
        password_input.send_keys("12345")
        password2_input.send_keys("12345")
        go.click()
        assert WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RegistrationPageLocators.LONG_USERNAME_LOCATOR)
        )