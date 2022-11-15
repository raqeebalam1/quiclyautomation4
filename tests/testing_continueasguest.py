import unittest

from resources import ui_test_class
from resources.page_objects.guest import ContinueAsGuest
from resources.page_objects.guest import guest


class TesCAG(ui_test_class.UIIClass):
    guest_page: guest
    guest_page: ContinueAsGuest
    expected_res2 = "First Name"
    expected_res3 = "Last Name"
    expected_res4 = "Enter your address"
    expected_res5 = "Apartment, Suite, Building (Optional)"
    expected_res6 = "Phone (ex:333-545-6789)"
    expected_res7 = "Email Address"
    expected_res_text_1 = "Shipping Address"
    expected_res_text_2 = "Submit"
    expected_error_1 = ""

    actual1 = "Need an Account? Signup"
    actual2 = "User Login"
    actual3 = "Sign In"
    actual4 = "This field is required."
    actual5 = "Please enter at least 10 characters."
    actual6 = "Please enter a valid email address."
    actual7 = "Your current address does not look right. Please select a valid address!"

    dictpl = {}
    dicttext = {}
    dictfr = {}

    @classmethod
    def setUpClass(cls):
        super(TesCAG, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCAG, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesCAG, self).setUp()
        self.base_page.driver.refresh()


    def compare_res_placeholders(self):

        firstname_placeholder = self.guest_page.get_attribute(ContinueAsGuest.firstname, 'placeholder')
        lastname_placeholder = self.guest_page.get_attribute(ContinueAsGuest.lastname, 'placeholder')
        address_placeholder = self.guest_page.get_attribute(ContinueAsGuest.fullAddress, 'placeholder')
        apartment_placeholder = self.guest_page.get_attribute(ContinueAsGuest.Apartment, 'placeholder')
        mob_placeholder = self.guest_page.get_attribute(ContinueAsGuest.MobileNumber, 'placeholder')
        mail_placeholder = self.guest_page.get_attribute(ContinueAsGuest.EmailAddress, 'placeholder')

        if self.expected_res2 == firstname_placeholder:
            self.dictpl['firstname'] = True

        else:
            self.dictpl['firstname'] = False

        if self.expected_res3 == lastname_placeholder:
            self.dictpl['lastname'] = True

        else:
            self.dictpl['lastname'] = False

        if self.expected_res4 == address_placeholder:
            self.dictpl['full address'] = True

        else:
            self.dictpl['full address'] = False

        if self.expected_res5 == apartment_placeholder:
            self.dictpl['Apartment'] = True

        else:
            self.dictpl['Apartment'] = False

        if self.expected_res6 == mob_placeholder:
            self.dictpl['mobile number'] = True

        else:
            self.dictpl['mobile number'] = False

        if self.expected_res7 == mail_placeholder:
            self.dictpl['email'] = True
            print(self.dictpl)

        else:
            self.dictpl['email'] = False
            print(self.dictpl)

    def compare_res_texts(self):

        shippingaddress_Text = self.guest_page.get_attribute(ContinueAsGuest.Shipping_address, 'innerHTML')
        submit_text = self.guest_page.get_attribute(ContinueAsGuest.Submit_name, 'innerHTML')

        if self.expected_res_text_1 == shippingaddress_Text:
            self.dicttext['Shipping Address'] = True

        else:
            self.dicttext['Shipping Address'] = False

        if self.expected_res_text_2 == submit_text:
            self.dicttext['Submit'] = True
            print(self.dicttext)

        else:
            self.dicttext['Submit'] = False
            print(self.dicttext)

    def compare_res_requiredfields(self):

        self.guest_page.click_submit()
        firstname_field = self.guest_page.get_attribute(ContinueAsGuest.firstname_error, 'innerHTML')
        print(firstname_field)
        address_field = self.guest_page.get_attribute(ContinueAsGuest.Address_error, 'innerHTML')
        print(address_field)
        mobile_field = self.guest_page.get_attribute(ContinueAsGuest.Mobile_error, 'innerHTML')
        print(mobile_field)
        email_field = self.guest_page.get_attribute(ContinueAsGuest.email_error, 'innerHTML')
        print(email_field)

    def test_checkingSignIn_link(self):

        """Checking If SignIn Button Is There Or Not"""
        signin_button_check = self.guest_page.get_attribute(ContinueAsGuest.signin_button, 'innerHTML')
        print(signin_button_check)
        self.assertEqual(self.actual3, signin_button_check)

    def test_ContinueAsGuest(self):

        """Adding Shipping Address To ContinueAsGuest"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.guest_page.first_name("Saad")
        self.guest_page.last_name("Adil")
        self.guest_page.full_address("Lahore, Pakistan")
        self.guest_page.apartment("")
        self.guest_page.mobile_number("333-416-3429")
        self.guest_page.email_address('saadadil3@gmail.com')
        self.guest_page.click_submit()
        print("shipping address was entered successfully")
        #Error = self.guest_page.get_attribute(ContinueAsGuest.googleError, 'innerHTML')
        #self.assertEqual(self.actual7, Error)

    def test_checkNeedAnAccount_link(self):

        """Checking NeedAnAccount Link On ContinueAsGuest Page"""
        NeedAnAccount_check = self.guest_page.get_attribute(ContinueAsGuest.needanaccount_signin, 'innerHTML')
        print(NeedAnAccount_check)
        self.assertEqual(self.actual1, NeedAnAccount_check)

    def test_UserLogIn_link(self):

        """Checking User Login Link On ContinueAsGuest Page"""
        LogIn_check = self.guest_page.get_attribute(ContinueAsGuest.user_login, 'innerHTML')
        print(LogIn_check)
        self.assertEqual(self.actual2, LogIn_check)


    def test_placeholders(self):

        """Placeholders for ContinueAsGuest Page"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.compare_res_placeholders()
        self.assertTrue(all(self.dictpl.values()), self.dictpl)


    def test_texts(self):

        """Headings for ContinueAsGuest Page"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.compare_res_texts()
        self.assertTrue(all(self.dicttext.values()), self.dicttext)

    def test_fieldsRequired(self):

        """Fields required for ContinueAsGuest Page"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.compare_res_requiredfields()
        firstname_field = self.guest_page.get_attribute(ContinueAsGuest.firstname_error, 'innerHTML')
        self.assertEqual(self.actual4, firstname_field)

    def test_check_invalidMob_input(self):

        """Mobile Input check for ContinueAsGuest Page"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.guest_page.mobile_number("1234")
        self.guest_page.click_submit()
        mob_invalid_check = self.guest_page.get_attribute(ContinueAsGuest.invalid_mobile, 'innerHTML')
        print(mob_invalid_check)
        self.assertEqual(self.actual5, mob_invalid_check)

    def test_check_invalidEmail_input(self):

        """Email Input check for ContinueAsGuest Page"""
        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.guest_page.email_address("msamiadil")
        self.guest_page.click_submit()
        email_invalid_check = self.guest_page.get_attribute(ContinueAsGuest.invalid_Email, 'innerHTML')
        print(email_invalid_check)
        self.assertEqual(self.actual6, email_invalid_check)

