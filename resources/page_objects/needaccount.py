from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.config_methods import DataClass
from resources.locators import NeedAnAccount
from resources.page_objects.base_page import BasePage



class needanaccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_sign_button(self):
        self.scroll_to_element(NeedAnAccount.signin)
        self.click(NeedAnAccount.signin)

    def click_NeedAnAccount(self):
        self.click(NeedAnAccount.NeedAnAccount_button)

    def Firstname(self, first_name):
        self.find_elements(NeedAnAccount.firname).clear()
        self.find_element(NeedAnAccount.firname).send_keys(first_name)

    def Lastname(self, lastname):
        self.find_elements(NeedAnAccount.lasname).clear()
        self.find_element(NeedAnAccount.lasname).send_keys(lastname)

    def enter_address(self, add):
        self.find_elements(NeedAnAccount.enteraddress).clear()
        self.find_element(NeedAnAccount.enteraddress).send_keys(add)

    def enter_apartment(self, apartno):
        self.find_elements(NeedAnAccount.apartmentno).clear()
        self.find_element(NeedAnAccount.apartmentno).send_keys(apartno)

    def mobile(self, mobno):
        self.find_elements(NeedAnAccount.mobileno).clear()
        self.find_element(NeedAnAccount.mobileno).send_keys(mobno)

    def enteremail(self, mail):
        self.find_elements(NeedAnAccount.email2).clear()
        self.find_element(NeedAnAccount.email2).send_keys(mail)


    def password(self, pas):
        self.find_elements(NeedAnAccount.pass2).clear()
        self.find_element(NeedAnAccount.pass2).send_keys(pas)

    def confirm_password(self, cpass):
        self.find_elements(NeedAnAccount.ConfirmPassword).clear()
        self.find_element(NeedAnAccount.ConfirmPassword).send_keys(cpass)

    def register_button(self):
        self.click(NeedAnAccount.register_button)

    def check_element(self):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(NeedAnAccount.googleError))
        Error = self.get_attribute(NeedAnAccount.googleError, 'innerHTML')
        print(Error)
