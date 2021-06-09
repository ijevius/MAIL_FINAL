from .base_page import BasePage
from locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    def make_reg(self):
        pass


    def go_login(self):
        self.click(RegistrationPageLocators.LOGIN_HINT_LOCATOR, 5)