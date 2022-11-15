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
    actual4 = "Jasneet K."
    actual5 = "Shikha P."
    actual6 = "Shilpa D."

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def tiffin(self):
        time.sleep(5)
        for i in range(10):
            time.sleep(2)
            self.depart_page.click_LeftArrow()
        time.sleep(1)
        self.depart_page.click_Tiffin1()
        time.sleep(10)
        self.depart_page.click_KamdarTiffin()
        # self.depart_page.click_Date()
        # self.depart_page.click_ChangeSlot()
        # self.depart_page.click_Schedule()
        # self.depart_page.click_Slot()
        # self.depart_page.click_Time()
        # self.depart_page.click_Submit4()
        time.sleep(5)
        self.depart_page.select_VegThali()
        time.sleep(5)
        self.depart_page.click_Roti()
        time.sleep(5)
        self.depart_page.click_AddToCartVT()
        self.depart_page.submitVT()
        self.depart_page.click_AddToCartVT()
        # self.depart_page.click_AddToCartVT()
        time.sleep(5)
        self.depart_page.click_MiniCart1()
        self.depart_page.click_Checkout()
        self.depart_page.click_Checkout2()
        # self.depart_page.click_payment2()
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
        AccountLabel = self.depart_page.get_attribute(Department.Account, 'innerHTML')
        print(AccountLabel)
        self.assertEqual(self.actual2, AccountLabel)

    def test_labelJasneet(self):
        label = self.depart_page.get_attribute(Department.labelJasneet, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelShikha(self):
        label = self.depart_page.get_attribute(Department.labelShika, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelShilpa(self):
        label = self.depart_page.get_attribute(Department.labelShilpa, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_shopWithTiffin(self):
        self.tiffin()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

