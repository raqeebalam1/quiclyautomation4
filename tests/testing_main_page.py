#!/usr/local/bin/python
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources import ui_test_class
from resources.page_objects.LogIn import LogIn


class TesLogin(ui_test_class.UIClass):
    heading = 'quicklly'

    expected_res = "Email Address"
    expected_res1 = "Password"
    expected_res19 = "Log In"
    expected_res20 = "Email :"
    expected_res21 = "Password :"
    mp = {}
    mp1 = {}
    actual1 = "Need an Account? Signup"
    actual2 = "Continue as a Guest"
    actual3 = "Forgot Password?"
    actual4 = "Introduction"
    actual5 = "Acceptance of the Terms of Use"
    actual6 = "&nbsp; Email or Password doesn't match "
    actual7 = "This field is required."
    actual8 = "Please enter a valid email address."
    actual9 = "&nbsp; One or more fields are blanks or doesn't have correct value "

    @classmethod
    def setUpClass(cls):
        super(TesLogin, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesLogin, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesLogin, self).setUp()
        self.base_page.driver.refresh()

    def compare_placeholders(self):

        email_placeholder = self.maine_page.get_attribute(LogIn.email, 'placeholder')
        password_placeholder = self.maine_page.get_attribute(LogIn.pasw, 'placeholder')

        if self.expected_res == email_placeholder:
            self.mp['email'] = True

        else:
            self.mp['email'] = False

        if self.expected_res1 == password_placeholder:
            self.mp['password'] = True
            print(self.mp)

        else:
            self.mp['password'] = False
            print(self.mp)



    def compare_res_texts(self):

        heading_login = self.maine_page.get_attribute(LogIn.login_heading, 'innerHTML')
        emailtext_heading = self.maine_page.get_attribute(LogIn.email_text, 'innerHTML')
        passwordtext_heading = self.maine_page.get_attribute(LogIn.password_text, 'innerHTML')
        print(heading_login)
        print(emailtext_heading)
        print(passwordtext_heading)

        if self.expected_res19 == heading_login:
            self.mp1['login'] = True

        else:
            self.mp1['login'] = False

        if self.expected_res20 == emailtext_heading:
            self.mp1['email'] = True

        else:
            self.mp1['email'] = False

        if self.expected_res21 == passwordtext_heading:
            self.mp1['password'] = True
            print(self.mp1)

        else:
            self.mp1['password'] = False
            print(self.mp1)



    def compare_res_fields_required(self):

        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        password_field = self.maine_page.get_attribute(LogIn.password_field_error, 'innerHTML')
        print(email_field + ": Email")
        print(password_field + ": Password")

    def test_login(self):

        """Login"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)    #error not generating
        self.assertEqual(self.actual6, error_messages)

    def test_login_placeholders(self):

        """placeholders for Login page"""
        self.maine_page.click_SignIn()
        self.compare_placeholders()
        self.assertTrue(all(self.mp.values()), self.mp)

    def test_login_texts(self):

        """headings for Login page"""
        self.maine_page.click_SignIn()
        self.compare_res_texts()
        self.assertTrue(all(self.mp1.values()), self.mp1)

    def test_FieldsRequired(self):

        """Fields Required for Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        self.assertEqual(self.actual7, email_field)
        self.compare_res_fields_required()

    def test_checkNeedAnAccount_link(self):

        """Checking NeedAnAccount Link On Login Page"""
        self.maine_page.click_SignIn()
        NeedAnAccount_check = self.maine_page.get_attribute(LogIn.needanaccount_signin, 'innerHTML')
        print(NeedAnAccount_check)
        self.assertEqual(self.actual1, NeedAnAccount_check)

    def test_checkContinueAsGuest_link(self):

        """Checking ContinueAsGuest Link On Login Page"""
        self.maine_page.click_SignIn()
        ContinueAsGuest_check = self.maine_page.get_attribute(LogIn.ContinueAsGuest_link, 'innerHTML')
        print(ContinueAsGuest_check)
        self.assertEqual(self.actual2, ContinueAsGuest_check)

    def test_forgotPassword_link(self):

        """Checking Forgot Password Link On Login Page"""
        self.maine_page.click_SignIn()
        ForgotPassword_check = self.maine_page.get_attribute(LogIn.ForgotPassword_link, 'innerHTML')
        print(ForgotPassword_check)
        self.assertEqual(self.actual3, ForgotPassword_check)

    def test_privacy_link(self):

        """Checking Privacy Link On Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_Privacy()
        Introduction = self.maine_page.get_attribute(LogIn.Intro, 'innerHTML')
        print(Introduction)
        self.assertEqual(self.actual4, Introduction)
        print("Privacy link is clickable")

    def test_TermsAndConditions_link(self):

        """Checking Terms&Conditions Link On Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_TermsAndConditions()
        TermsOfUse = self.maine_page.get_attribute(LogIn.Terms, 'innerHTML')
        print(TermsOfUse)
        self.maine_page.click_home()
        self.assertEqual(self.actual5, TermsOfUse)
        print("Terms&Condition link is clickable")

    def test_DotBetweenEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin.123@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)
        print("Accepted")

    def test_DotBetweenSubDomain(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)
        print("Accepted")

    def test_DigitsInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LogIn.doesnt_match))
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)
        print("Accepted")

    def test_UnderScoreInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123_abc@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)
        print("Accepted")

    def test_DashInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123-abc@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)
        print("Accepted")

    def test_ValidEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("1123abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        self.assertEqual(self.actual8, email_field)
        print("Not Accepted")

    def test_ValidEmail2(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        self.assertEqual(self.actual8, email_field)
        print("Not Accepted")

    def test_ValidEmail3(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("abc@abc@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        self.assertEqual(self.actual8, email_field)
        print("Not Accepted")

    def test_ValidEmail4(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("abc….....abc@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        self.assertEqual(self.actual8, email_field)
        print("Not Accepted")

    def test_ValidEmail5(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("255.255. 255.255")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        self.assertEqual(self.actual8, email_field)
        print("Not Accepted")

    def test_EmailAndPassDontMatch(self):

        """Checking EmailAndPassDontMatch Label """
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual6, error_messages)

    def test_password_minLength(self):

        """Checking Password Min Length"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
        self.assertEqual(self.actual9, error_messages)
