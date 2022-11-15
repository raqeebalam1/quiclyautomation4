from resources.config_methods import DataClass
from resources.locators import ContinueAsGuest
from resources.page_objects.base_page import BasePage


class guest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def signin_button(self):
        self.scroll_to_element(ContinueAsGuest.signin_button)
        self.click(ContinueAsGuest.signin_button)

    def click_Continue_As_Guest(self):
        self.scroll_to_element(ContinueAsGuest.ContinueAsGuest_button)
        self.click(ContinueAsGuest.ContinueAsGuest_button)

    def first_name(self, firstname):
        self.find_elements(ContinueAsGuest.firstname).clear()
        self.find_element(ContinueAsGuest.firstname).send_keys(firstname)

    def last_name(self, lastname):
        self.find_elements(ContinueAsGuest.lastname).clear()
        self.find_element(ContinueAsGuest.lastname).send_keys(lastname)

    def full_address(self, fulladdress):
        self.find_elements(ContinueAsGuest.fullAddress).clear()
        self.find_element(ContinueAsGuest.fullAddress).send_keys(fulladdress)
        # // *[ @ id = "autocomplete2"]

    def apartment(self, apart):
        self.find_elements(ContinueAsGuest.Apartment).clear()
        self.find_element(ContinueAsGuest.Apartment).send_keys(apart)

    def mobile_number(self, number):
        self.find_elements(ContinueAsGuest.MobileNumber).clear()
        self.find_element(ContinueAsGuest.MobileNumber).send_keys(number)

    def email_address(self, eaddress):
        self.find_elements(ContinueAsGuest.EmailAddress).clear()
        self.find_element(ContinueAsGuest.EmailAddress).send_keys(eaddress)


    def click_submit(self):
        self.click(ContinueAsGuest.submit_button)
