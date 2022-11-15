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
    actual4 = "Indian Catering Chicago IL"
    actual5 = "Hyderabad House"

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()


    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    # def BackToPage(self):
    #     self.depart_page.click_quicklly()
    #     time.sleep(3)
    #     self.depart_page.zip("60611")
    #     self.depart_page.submit_zip()
    #     time.sleep(5)
    #     for i in range(4):
    #         time.sleep(1)
    #         self.depart_page.click_LeftArrow()
    #     self.depart_page.click_Catering()
    #     time.sleep(2)

    def Catering(self):
        time.sleep(5)
        for i in range(9):
            time.sleep(1)
            self.depart_page.click_RightArrow()
        self.depart_page.click_Catering()
        time.sleep(2)
        self.depart_page.click_Hyderabad()
        self.depart_page.click_AddBeef()
        # self.depart_page.click_Medium()
        # self.depart_page.click_Qty1()
        # self.depart_page.click_3Qty()
        self.depart_page.click_AddToCartBeef()
        # self.depart_page.click_Delivery()
        # time.sleep(5)
        # self.depart_page.click_timeOfDelivery()
        self.depart_page.click_SubmitBeef()
        time.sleep(3)
        self.depart_page.click_MiniCart()
        time.sleep(5)
        self.depart_page.click_Checkout()
        time.sleep(2)
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()
        time.sleep(10)

    # def test_AddMomo(self):
        # self.depart_page.click_IndianCateringStore()
        # time.sleep(3)
        # search = self.depart_page.get_attribute(Department.IndianCatering, 'placeholder')
        # print(search)
        # self.assertEqual(self.actual4, search)
        # self.BackToPage()
        # time.sleep(10)
        # self.depart_page.click_MomoFactory()
        # self.depart_page.click_AddMomo()
        # self.depart_page.click_AddToCartBeef()
        # self.depart_page.click_Delivery()
        # time.sleep(5)
        # self.depart_page.click_timeOfDelivery()
        # time.sleep(3)
        # self.depart_page.click_SubmitBeef()
        # self.depart_page.click_IndianCateringStore()
        # self.depart_page.click_AddGulabJamun()
        # self.depart_page.click_AddToCartBeef()
        # self.depart_page.click_LargeQuantity()
        # self.depart_page.click_3Qty()
        # self.depart_page.click_Delivery()
        # time.sleep(5)
        # self.depart_page.click_timeOfDelivery()
        # time.sleep(3)
        # self.depart_page.click_SubmitBeef()
        # self.depart_page.click_MiniCart()
        # time.sleep(5)
        # self.depart_page.click_Checkout()
        # time.sleep(2)
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
        # self.depart_page.select_dropdown()
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


    # def test_shopWithCatering(self):
    #     self.Catering()
    #     ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
    #     print(ThankYouLabel)
    #     self.assertEqual(self.actual1, ThankYouLabel)

    def test_labelHyderaabad(self):
        label = self.depart_page.get_attribute(Department.Hyderabadlabel, 'textContent')
        print(label)
        self.assertEqual(self.actual5, label)