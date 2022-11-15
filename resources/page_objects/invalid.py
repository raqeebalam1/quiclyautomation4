from resources.config_methods import DataClass
from resources.locators import Invalid
from resources.page_objects.base_page import BasePage


class InvalidZipcodes(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterZip(self, zipcode):
        self.find_element(Invalid.enter_zip).clear()
        self.find_element(Invalid.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Invalid.submit_zip)
