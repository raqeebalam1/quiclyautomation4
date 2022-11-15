from resources.config_methods import DataClass
from resources.locators import ZipCode
from resources.page_objects.base_page import BasePage


class Zip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)


    def zip(self, zipcode):
        self.find_element(ZipCode.enter_zip).clear()
        self.find_element(ZipCode.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(ZipCode.submit_zip)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_department(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_cross(self):
        self.click(ZipCode.cross)
