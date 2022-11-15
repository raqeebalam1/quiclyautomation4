import time
from resources import ui_test_class
from resources.page_objects.department import Department
from resources.page_objects.department import Dept
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TesDEPARTMENT(ui_test_class.UVIIClass):
    depart_page: Dept
    depart_page: Department

    actual1 = "Thank you"
    actual2 = "Your Account"
    actual3 = "Search for products..."

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def Liquor(self):
        time.sleep(5)
        self.depart_page.click_Liquor()
        time.sleep(5)
        # self.depart_page.click_beer()
        # time.sleep(2)
        # self.depart_page.click_gin()
        # time.sleep(2)
        self.depart_page.click_AmsterdamGin()
        self.depart_page.click_AmsterdamGin200ml()
        time.sleep(2)
        self.depart_page.click_AddToCartAmsterdamGin()
        time.sleep(2)
        self.depart_page.click_legalCheckBox()
        time.sleep(2)
        self.depart_page.click_elderCheckBox()
        time.sleep(2)
        self.depart_page.click_submitAlcohol()
        time.sleep(2)
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(5)
        # self.depart_page.click_Checkout2()
        # time.sleep(10)
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()
        # time.sleep(10)

    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()
        search = self.depart_page.get_attribute(Department.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIN(self):
        self.depart_page.select_dropdown()
        self.depart_page.click_signin()
        self.depart_page.EnterEmail("testaccount@quicklly.com")
        self.depart_page.EnterPass("123456")
        self.depart_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        AccountLabel = self.depart_page.get_attribute(Department.Account, 'innerHTML')
        print(AccountLabel)
        self.assertEqual(self.actual2, AccountLabel)


    def test_shopWithLiquor(self):
        self.Liquor()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)
