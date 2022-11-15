import time
from resources import ui_test_class
from resources.page_objects.weekly_page import WEEKLY
from resources.page_objects.weekly_page import Weekly

class TesWEEKLYORDER(ui_test_class.UVXVXVIIIClass):
    weekly_page: WEEKLY
    weekly_page: Weekly

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"
    actual5 = "Rajbhog Diwali Party Pack  "

    @classmethod
    def setUpClass(cls):
        super(TesWEEKLYORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesWEEKLYORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.weekly_page.zip("60611")
        self.weekly_page.submit_zip()
        search = self.weekly_page.get_attribute(Weekly.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.weekly_page.select_dropdown()
        self.weekly_page.click_signin()
        self.weekly_page.EnterEmail("testaccount@quicklly.com")
        self.weekly_page.EnterPass("123456")
        self.weekly_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_weeklyOrder(self):
        time.sleep(5)
        for i in range(2):
            self.weekly_page.click_RightArrow()
        self.weekly_page.click_NationWideShop()
        self.weekly_page.click_indianSweet()
        self.weekly_page.click_weekly()
        self.weekly_page.click_buildABox()
        self.weekly_page.click_addPistaGhari()
        # for i in range(4):
        #     time.sleep(2)
        #     self.weekly_page.click_plusPistaGhari()
        # quantityLabel = self.weekly_page.get_attribute(Weekly.quantity, 'innerHTML')
        # print(quantityLabel)
        # self.assertEqual(self.actual4, quantityLabel)

    def test_weeklyOrderCheckout(self):
        self.weekly_page.click_addToCartPistaGhari()
        time.sleep(2)
        self.weekly_page.click_Cart()
        self.weekly_page.click_Checkout()
        self.weekly_page.click_Checkout2()
        # self.weekly_page.click_payment1()
        # time.sleep(5)
        # self.weekly_page.click_Pay()
        # ThankYouLabel = self.weekly_page.get_attribute(Weekly.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)


    def test_labelRajbogh(self):
        label = self.weekly_page.get_attribute(Weekly.Rajbogh, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)