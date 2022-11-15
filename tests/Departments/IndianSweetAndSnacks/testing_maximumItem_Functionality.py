import time
from resources import ui_test_class
from resources.page_objects.max_page import Maximum
from resources.page_objects.max_page import MAXIMUM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TesMAXIMUMITEM(ui_test_class.UVXVXVVIClass):
    max_page: Maximum
    max_page: MAXIMUM

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "We're sorry, you have reached max quantity allowed in this box"
    text = ""
    actual5 = "Rajbhog Diwali Party Pack  "

    @classmethod
    def setUpClass(cls):
        super(TesMAXIMUMITEM, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesMAXIMUMITEM, cls).tearDownClass()
        cls.driver.quit()

    def alert(self):
        time.sleep(5)
        for i in range(6):
            self.max_page.click_RightArrow()
        self.max_page.click_NationWideShop()
        self.max_page.click_indianSweet()
        self.max_page.click_monthly()
        self.max_page.click_buildABox()
        self.max_page.click_addPistaGhari()
        for i in range(5):
            self.max_page.click_plusPistaGhari()
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.text = alert.text
            print(self.text)
            alert.accept()
            print("alert Exists in page")
        except TimeoutException:
            print("alert does not Exist in page")
        self.max_page.click_addToCartPistaGhari()
        self.max_page.click_Cart()

    def test_EnterZipCode(self):
        self.max_page.zip("60611")
        self.max_page.submit_zip()
        search = self.max_page.get_attribute(Maximum.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.max_page.select_dropdown()
        self.max_page.click_signin()
        self.max_page.EnterEmail("testaccount@quicklly.com")
        self.max_page.EnterPass("123456")
        self.max_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_labelRajbogh(self):
        label = self.max_page.get_attribute(Maximum.Rajbogh, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_maximumPopup(self):
        self.alert()
        self.assertEqual(self.actual4, self.text)

