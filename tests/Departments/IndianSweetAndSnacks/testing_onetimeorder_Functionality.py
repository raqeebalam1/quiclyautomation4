import time
from resources import ui_test_class
from resources.page_objects.onetime_page import ONETIME
from resources.page_objects.onetime_page import OneTime

class TesONETIMEORDER(ui_test_class.UVXVXVIIClass):
    one_page: ONETIME
    one_page: OneTime

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"
    actual5 = "Rajbhog Diwali Party Pack  "

    @classmethod
    def setUpClass(cls):
        super(TesONETIMEORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesONETIMEORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.one_page.zip("60611")
        self.one_page.submit_zip()
        search = self.one_page.get_attribute(OneTime.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.one_page.select_dropdown()
        self.one_page.click_signin()
        self.one_page.EnterEmail("testaccount@quicklly.com")
        self.one_page.EnterPass("123456")
        self.one_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_oneTimeOrder(self):
        time.sleep(5)
        for i in range(2):
            self.one_page.click_RightArrow()
        self.one_page.click_NationWideShop()
        self.one_page.click_indianSweet()
        self.one_page.click_buildABox()
        self.one_page.click_addPistaGhari()
        time.sleep(10)
        # for i in range(4):
        #     self.one_page.click_plusPistaGhari()
        # quantityLabel = self.one_page.get_attribute(OneTime.quantity, 'innerHTML')
        # print(quantityLabel)
        # self.assertEqual(self.actual4, quantityLabel)

    def test_oneTimeOrderCheckout(self):
        self.one_page.click_addToCartPistaGhari()
        time.sleep(2)
        self.one_page.click_Cart()
        self.one_page.click_Checkout()
        self.one_page.click_Checkout2()
        # self.one_page.click_payment1()
        # time.sleep(5)
        # self.one_page.click_Pay()
        # ThankYouLabel = self.one_page.get_attribute(OneTime.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_labelRajbogh(self):
        label = self.one_page.get_attribute(OneTime.Rajbogh, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)