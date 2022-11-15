from resources.config_methods import DataClass
from resources.locators import LogIn
from resources.page_objects.base_page import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_SignIn(self):
        self.scroll_to_element(LogIn.SignIn_button)
        self.click(LogIn.SignIn_button)

    def enter_email(self, email):
        self.find_elements(LogIn.email_textbox).clear()
        self.find_element(LogIn.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.find_elements(LogIn.password_textbox).clear()
        self.find_element(LogIn.password_textbox).send_keys(password)

    def click_login(self):
        self.scroll_to_element(LogIn.login_button)
        self.click(LogIn.login_button)

    def click_Privacy(self):
        self.click(LogIn.privacy_link)

    def click_TermsAndConditions(self):
        self.click(LogIn.terms_link)

    def click_home(self):
        self.click(LogIn.home_button)
