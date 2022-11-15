from resources.config_methods import DataClass
from resources.locators import Contact
from resources.page_objects.base_page import BasePage


class contactUs(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_element(Contact.enter_zip).clear()
        self.find_element(Contact.enter_zip).send_keys(zipcode)

    def click_contact(self):
        self.scroll_to_element(Contact.contact)
        element = self.driver.find_element_by_link_text('CONTACT')
        self.driver.execute_script("arguments[0].click();", element)

    def Fullname(self, name):
        self.find_element(Contact.name).clear()
        self.find_element(Contact.name).send_keys(name)

    def EmailAddress(self, mail):
        self.find_element(Contact.email).clear()
        self.find_element(Contact.email).send_keys(mail)

    def Subject(self, sub):
        self.find_element(Contact.subject).clear()
        self.find_element(Contact.subject).send_keys(sub)

    def Comment(self, com):
        self.find_element(Contact.comment).clear()
        self.find_element(Contact.comment).send_keys(com)

    def SendNow(self):
        element = self.driver.find_element_by_xpath('//*[@id="main-contact-form"]/div/fieldset/ul/div/button')
        self.driver.execute_script("arguments[0].click();", element)
