import time

from resources import ui_test_class
from resources.page_objects.forgetpassword import ForgetPassword
from resources.page_objects.forgetpassword import forgetpass


class TesFP(ui_test_class.UIIIIClass):

    forget_page: ForgetPassword
    forget_page: forgetpass
    expected_res16 = "Enter your registered Email Id"
    expected_res17 = "Forgot Password"
    expected_res18 = "Why register with us."
    fp = {}
    fp1 = {}

    actual1 = "Password reset link has been sent on email!"

    @classmethod
    def setUpClass(cls):
        super(TesFP, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesFP, cls).tearDownClass()
        cls.driver.quit()

    def compare_res_Headings(self):

        forgotpassword_heading = self.forget_page.get_attribute(ForgetPassword.heading1, 'innerHTML')
        whyregister_heading = self.forget_page.get_attribute(ForgetPassword.heading2, 'innerHTML')

        if self.expected_res17 == forgotpassword_heading:
            self.fp['forgot password'] = True

        else:
            self.fp['forgot password'] = False

        if self.expected_res18 == whyregister_heading:
            self.fp['why register with us.'] = True
            print(self.fp)

        else:
            self.fp['why register with us.'] = False
            print(self.fp)

    def compare_res_Placeholders(self):

        registeredemail_placeholder = self.forget_page.get_attribute(ForgetPassword.registered_email, 'placeholder')


        if self.expected_res16 == registeredemail_placeholder:
            self.fp1['Enter your registered Email Id'] = True
            print(self.fp1)


        else:
            self.fp1['Enter your registered Email Id'] = False
            print(self.fp1)

    def test_ForgetPassword(self):
        """Adding User Details For Forget Password"""
        # time.sleep(3)
        self.forget_page.click_Signin()
        self.forget_page.click_ForgetPassword()
        self.forget_page.registred_email("testaccount@quicklly.com")
        self.forget_page.click_submit()
        invalid_email = self.forget_page.get_attribute(ForgetPassword.invalid_email, 'textContent')
        print(invalid_email)
        self.assertEqual(self.actual1, invalid_email)


    def test_headings(self):
        """Headings for ForgotPassword page"""
        self.compare_res_Headings()
        self.assertTrue(all(self.fp.values()), self.fp)

    def test_placeholders(self):
        """Placeholders for ForgotPassword page"""
        self.compare_res_Placeholders()
        self.assertTrue(all(self.fp1.values()), self.fp1)
