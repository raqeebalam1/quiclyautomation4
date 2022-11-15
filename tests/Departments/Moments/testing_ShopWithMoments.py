import time

from selenium.webdriver.common import alert

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

    def Moments(self):
        time.sleep(5)
        self.depart_page.click_Shopbydepartment()
       # time.sleep(2)
       # self.depart_page.click_Moments()
        time.sleep(3)
        self.depart_page.click_Department_Moments()
        time.sleep(2)
        self.depart_page.click_ExploreQuickllyMoments()
        time.sleep(2)
        self.depart_page.click_Addtocart_Ganeshbox()
        self.depart_page.click_Plus_Ganeshbox()
        self.depart_page.click_Next()
        self.test_AddRecipient()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(5)
        self.depart_page.click_ProceedtoCheckout()
        time.sleep(5)
        self.depart_page.click_payment1()

    def test_AddRecipient(self):
       # self.depart_page.select_dropdown()
       # self.depart_page.click_signin()
        self.depart_page.RecipientFName("Test")
        self.depart_page.RecipientLName("Account")
        self.depart_page.RecipientEmail("testaccount@quicklly.com")
        self.depart_page.RecipientPhone("1234567890")
        self.depart_page.RecipientAddress("1400 N Lake Shore Dr, Chicago, IL, USA")
        self.depart_page.RecipientApartment("1")
        self.depart_page.click_Submit()
        self.depart_page.click_Skipthistep()
        time.sleep(3)
        # self.depart_page.click_MiniCart()
        # self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()

        time.sleep(2)
       # alert = self.driver.switch_to.alert
       # alert.accept()
        #AccountLabel = self.depart_page.get_attribute(Department.Account, 'innerHTML')
        #print(AccountLabel)
        #self.assertEqual(self.actual2, AccountLabel)


    def test_Moments(self):
        time.sleep(3)
        self.Moments()


