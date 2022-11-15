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
    actual4 = "Gorkha Kitchen"
    actual5 = "Adda Indian Cuisine"
    actual6 = "Kabobchi"
    actual7 = "Cafe Alif"
    actual8 = "Aroma Desi Grill"
    actual9 = "Aloo Samosa"
    actual10 = "Chilli Beef Roll"
    actual11 = "2 Beef Tacos"
    actual12 = "4Pc Tikka"
    actual13 = "Chicken Biryani"


    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def food(self):
        time.sleep(5)
        self.depart_page.click_food()
        time.sleep(5)
        self.depart_page.scroll_to_element(Department.MakkahCafe)
        time.sleep(2)
        self.depart_page.click_MakkahCafe()
        self.depart_page.click_AddAlooSam()
        self.depart_page.click_AddtoCartAlooSam()
        time.sleep(4)
        self.depart_page.click_submitAlooSam()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()
        time.sleep(10)

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
        time.sleep(2)
        AccountLabel = self.depart_page.get_attribute(Department.Account2, 'innerHTML')
        print(AccountLabel)
        self.assertEqual(self.actual2, AccountLabel)

    def test_shopWithFood(self):
        self.food()
        ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

    def test_LabelGorkha(self):
        search = self.depart_page.get_attribute(Department.GorkahChicken, 'placeholder')
        print(search)
        self.assertEqual(self.actual4, search)

    def test_LabelAdda(self):
        search = self.depart_page.get_attribute(Department.AddaIndian, 'placeholder')
        print(search)
        self.assertEqual(self.actual5, search)

    def test_LabelKabobchi(self):
        search = self.depart_page.get_attribute(Department.Kabobchi, 'placeholder')
        print(search)
        self.assertEqual(self.actual6, search)

    def test_LabelAlif(self):
        search = self.depart_page.get_attribute(Department.CafeAlif, 'placeholder')
        print(search)
        self.assertEqual(self.actual7, search)

    def test_LabelAloSamosa(self):
        search = self.depart_page.get_attribute(Department.AaloSamosa2, 'placeholder')
        print(search)
        self.assertEqual(self.actual9, search)

    def test_LabelChiliBeef(self):
        search = self.depart_page.get_attribute(Department.ChilliBeef, 'placeholder')
        print(search)
        self.assertEqual(self.actual10, search)

    def test_LabelTaco(self):
        search = self.depart_page.get_attribute(Department.BeefTaco, 'placeholder')
        print(search)
        self.assertEqual(self.actual11, search)

    def test_LabelTikka(self):
        search = self.depart_page.get_attribute(Department.Tikka, 'placeholder')
        print(search)
        self.assertEqual(self.actual12, search)

    def test_LabelBiryani(self):
        search = self.depart_page.get_attribute(Department.Biryani, 'placeholder')
        print(search)
        self.assertEqual(self.actual13, search)

