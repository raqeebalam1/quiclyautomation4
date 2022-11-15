import time
from resources import ui_test_class
from resources.locators import SignUp
from resources.page_objects.signup import signUp
import pandas as pd


class TesSIGNUP(ui_test_class.UVXClass):
    signup_page: SignUp
    signup_page: signUp

    actual = "Free Same - Day Delivery From Top Rated Stores"

    @classmethod
    def setUpClass(cls):
        super(TesSIGNUP, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesSIGNUP, cls).tearDownClass()
        cls.driver.quit()

    def Credentials(self):
        self.signup_page.click_signin()
        self.signup_page.click_needAccount()
        data = pd.read_excel(r'Data/signupCredentials.xls', dtype=str)
        fname = pd.DataFrame(data, columns=['First Name']).values[0]
        lname = pd.DataFrame(data, columns=['Last Name']).values[0]
        address = pd.DataFrame(data, columns=['Address']).values[0]
        phone = pd.DataFrame(data, columns=['Phone']).values[0]
        email = pd.DataFrame(data, columns=['Email Address']).values[0]
        password = pd.DataFrame(data, columns=['Password']).values[0]
        confirmpassword = pd.DataFrame(data, columns=['Confirm Password']).values[0]
        self.signup_page.firstName(fname)
        self.signup_page.lastName(lname)
        self.signup_page.Address(address)
        self.signup_page.Phone(phone)
        self.signup_page.emailAddress(email)
        self.signup_page.Password(password)
        self.signup_page.ConfirmPassword(confirmpassword)
        self.signup_page.click_Register()
        time.sleep(25)


    def test_signup(self):
        self.Credentials()
        headingLabel = self.signup_page.get_attribute(SignUp.heading, 'innerHTML')
        print(headingLabel)
        self.assertEqual(self.actual, headingLabel)


