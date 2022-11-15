from resources.config_methods import DataClass
from resources.locators import Refer
from resources.page_objects.base_page import BasePage


class ReferAFriend(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_refer(self):
        self.click(Refer.refer)

    def click_referLink(self):
        self.click(Refer.referLink)

    def click_facebook(self):
        element = self.driver.find_element_by_css_selector('#referfb')
        self.driver.execute_script("arguments[0].click();", element)

    def click_facebookLink(self):
        element = self.driver.find_element_by_xpath('//*[@id="shareonFacebookBtn"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_twitter(self):
        element = self.driver.find_element_by_xpath('//*[@id="refertw"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_twitterLink(self):
        element = self.driver.find_element_by_xpath('//*[@id="shareonTwitterBtn"]')
        self.driver.execute_script("arguments[0].click();", element)
