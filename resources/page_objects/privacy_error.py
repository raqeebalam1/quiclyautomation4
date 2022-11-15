from .base_page import BasePage
from ..config_methods import DataClass
from ..locators import PrivacyErrorPageLocators


class PrivacyError(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def open_learn_more_link(self):
        self.click(PrivacyErrorPageLocators.learn_more_link)

    def click_advanced_button(self):
        self.click(PrivacyErrorPageLocators.advanced_button)

    def open_proceed_link(self):
        self.click(PrivacyErrorPageLocators.proceed_link)

    def click_hide_advanced_button(self):
        self.click(PrivacyErrorPageLocators.advanced_button)

    def click_back_to_safety_button(self):
        self.click(PrivacyErrorPageLocators.back_to_safety_button)
