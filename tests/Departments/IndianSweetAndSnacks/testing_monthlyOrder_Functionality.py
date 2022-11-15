import time
from resources import ui_test_class
from resources.page_objects.monthly_page import Monthly
from resources.page_objects.monthly_page import MONTHLY


class TesMONTHLYORDER(ui_test_class.UVXVXVVClass):
    monthly_page: Monthly
    monthly_page: MONTHLY

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"
    actual5 = "Rajbhog Diwali Party Pack  "

    @classmethod
    def setUpClass(cls):
        super(TesMONTHLYORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesMONTHLYORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.monthly_page.zip("60611")
        self.monthly_page.submit_zip()
        search = self.monthly_page.get_attribute(Monthly.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.monthly_page.select_dropdown()
        self.monthly_page.click_signin()
        self.monthly_page.EnterEmail("testaccount@quicklly.com")
        self.monthly_page.EnterPass("123456")
        self.monthly_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_monthlyOrder(self):
        time.sleep(5)
        for i in range(13):
            self.monthly_page.click_LeftArrow1()
        self.monthly_page.click_NationWideShop()
        self.monthly_page.click_indianSweet()
        self.monthly_page.click_monthly()
        self.monthly_page.click_buildABox()
        self.monthly_page.click_addPistaGhari()
        # for i in range(4):
        #     self.monthly_page.click_plusPistaGhari()
        # quantityLabel = self.monthly_page.get_attribute(Monthly.quantity, 'innerHTML')
        # print(quantityLabel)
        # self.assertEqual(self.actual4, quantityLabel)

    def test_monthlyOrderCheckout(self):
        self.monthly_page.click_addToCartPistaGhari()
        time.sleep(2)
        self.monthly_page.click_Cart()
        self.monthly_page.click_Checkout()
        self.monthly_page.click_Checkout2()
        # self.monthly_page.click_payment1()
        # time.sleep(5)
        # self.monthly_page.click_Pay()
        # ThankYouLabel = self.monthly_page.get_attribute(Monthly.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_labelRajbogh(self):
        label = self.monthly_page.get_attribute(Monthly.Rajbogh, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)