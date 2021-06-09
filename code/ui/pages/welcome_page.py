from .base_page import BasePage
from locators import WelcomePageLocators


class WelcomePage(BasePage):
    locators = WelcomePageLocators()

    def click_api(self):
        self.click(WelcomePageLocators.WIKI_API_LOCATOR, 15)