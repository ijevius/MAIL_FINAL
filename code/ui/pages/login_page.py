import os
import sys
sys.path.append("/home/rus/PycharmProjects/final_app_mairu/code")
import creds
from .base_page import BasePage
from ui.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def make_login(self, login=creds.GOOD_LOGIN, password=creds.GOOD_PASSWORD):
        login_input = self.find(LoginPageLocators.LOGIN_INPUT_LOCATOR, 5)
        login_input.clear()
        password_input = self.find(LoginPageLocators.PASSWORD_INPUT_LOCATOR, 5)
        password_input.clear()
        login_input.send_keys(login)
        password_input.send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON_LOCATOR)
        return self

    def go_reg(self):
        self.click(LoginPageLocators.REG_HINT_LOCATOR, 5)