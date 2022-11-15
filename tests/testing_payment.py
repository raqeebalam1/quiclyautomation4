import time
from resources import ui_test_class
from resources.page_objects.payment import Payment
from resources.page_objects.payment import Pay
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TesPAYMENT(ui_test_class.UVXVIIClass):
    payment_page: Pay
    payment_page: Payment

    actual1 = "Thank you"
    actual2 = "Your account"
    actual3 = "Search for products..."
    actual4 = "Add Payment Method"
    actual5 = "Use saved payment method"
    expected_res = "Card Number"
    expected_res1 = "Expiration Date"
    expected_res2 = "CVV"
    actual6 = "158"
    actual7 = "Log In"
    actual8 = "Pay"
    mp = {}

    @classmethod
    def setUpClass(cls):
        super(TesPAYMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesPAYMENT, cls).tearDownClass()
        cls.driver.quit()

    def compare_placeholders(self):

        cardNumber_placeholder = self.payment_page.get_attribute(Payment.cardNumber, 'placeholder')
        expiry_placeholder = self.payment_page.get_attribute(Payment.expiry, 'placeholder')
        Cvv_placeholder = self.payment_page.get_attribute(Payment.CVV, 'placeholder')

        if self.expected_res == cardNumber_placeholder:
            self.mp['Card Number'] = True

        else:
            self.mp['Card Number'] = False

        if self.expected_res1 == expiry_placeholder:
            self.mp['Expiration Date'] = True

        else:
            self.mp['Expiration Date'] = False

        if self.expected_res2 == Cvv_placeholder:
            self.mp['CVV'] = True

        else:
            self.mp['CVV'] = False

        print(self.mp)

    def Signin(self):
        self.payment_page.EnterEmail("testaccount@quicklly.com")
        self.payment_page.EnterPass("123456")
        self.payment_page.click_login()

    def addItem(self):
        time.sleep(2)
        self.payment_page.click_fresh()
        self.payment_page.click_additem()
        self.payment_page.click_ADDLG()
        time.sleep(5)
        self.payment_page.click_MiniCart1()
        self.payment_page.click_Checkout()
        self.payment_page.click_Checkout2()

    def switchFrames(self):
        self.driver.switch_to_default_content()
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.driver.find_element_by_css_selector('#braintree-dropin-modal-frame')))

    def test_EnterZipCode(self):
        self.payment_page.zip("60611")
        self.payment_page.submit_zip()
        search = self.payment_page.get_attribute(Payment.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_additem(self):
        self.addItem()
        time.sleep(5)
        paymentLabel = self.payment_page.get_attribute(Payment.loginLabel, 'innerHTML')
        print(paymentLabel)
        self.assertEqual(self.actual7, paymentLabel)

    def test_clickPayment(self):
        self.Signin()
        self.payment_page.click_payment1()
        payLabel = self.payment_page.get_attribute(Payment.Pay, 'value')
        print(payLabel)
        self.assertEqual(self.actual8, payLabel)

    def test_paymentMethod(self):
        self.payment_page.click_paymentMethod()
        self.switchFrames()
        AddPaymentLabel = self.payment_page.get_attribute(Payment.AddMethod, 'innerHTML')
        print(AddPaymentLabel)
        self.assertEqual(self.actual4, AddPaymentLabel)
        time.sleep(10)

    def test_paymentMethodAddingLink(self):
        self.payment_page.click_AddPaymentMethod()
        time.sleep(15)
        SavePaymentLabel = self.payment_page.get_attribute(Payment.savePaymentMethod, 'innerHTML')
        print(SavePaymentLabel)
        self.assertEqual(self.actual5, SavePaymentLabel)
        time.sleep(10)


    def test_paymentMethodDetails1(self):
        self.payment_page.EnterCardNumber("5555444433331111")
        self.payment_page.EnterExpiry("0225")
        self.payment_page.EnterCVV("158")
        value = self.payment_page.get_attribute(Payment.CVV, 'value')
        print(value)
        self.assertEqual(self.actual6, value)
        time.sleep(10)

    def test_paymentMethodDetails(self):
        self.compare_placeholders()
        self.assertTrue(all(self.mp.values()), self.mp)

    def test_paymentMethodPay(self):
        self.payment_page.click_AddMethod()
        self.payment_page.click_Pay()
        time.sleep(15)
        ThankYouLabel = self.payment_page.get_attribute(Payment.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)
