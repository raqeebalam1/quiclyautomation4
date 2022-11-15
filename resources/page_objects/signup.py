import time
from resources.config_methods import DataClass
from resources.locators import SignUp
from resources.page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys as K


class signUp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_signin(self):
        self.click(SignUp.signin)

    def click_needAccount(self):
        self.click(SignUp.needAccount)

    def firstName(self, fname):
        self.find_element(SignUp.firstName).clear()
        self.find_element(SignUp.firstName).send_keys(fname)

    def lastName(self, lname):
        self.find_element(SignUp.lastName).clear()
        self.find_element(SignUp.lastName).send_keys(lname)

    def Address(self, add):
        self.find_element(SignUp.Address).clear()
        self.find_element(SignUp.Address).send_keys(add)
        time.sleep(5)
        self.find_element(SignUp.Address).send_keys(K.ARROW_DOWN)
        self.find_element(SignUp.Address).send_keys(K.ENTER)

    def Phone(self, ph):
        self.find_element(SignUp.Phone).clear()
        self.find_element(SignUp.Phone).send_keys(ph)

    def emailAddress(self, email):
        self.find_element(SignUp.email).clear()
        self.find_element(SignUp.email).send_keys(email)

    def Password(self, password):
        self.find_element(SignUp.password).clear()
        self.find_element(SignUp.password).send_keys(password)

    def ConfirmPassword(self, cpass):
        self.find_element(SignUp.confirmpassword).clear()
        self.find_element(SignUp.confirmpassword).send_keys(cpass)

    def click_Register(self):
        self.click(SignUp.register)

    def EnterEmail2(self, email2):
        self.find_element(SignUp.email2).clear()
        self.find_element(SignUp.email2).send_keys(email2)

    def EnterPassword2(self, pass2):
        self.find_element(SignUp.password2).clear()
        self.find_element(SignUp.password2).send_keys(pass2)

    def click_login(self):
        self.click(SignUp.logIn)
