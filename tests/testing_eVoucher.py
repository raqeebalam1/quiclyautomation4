import time
from resources import ui_test_class
from resources.locators import Coupon
from resources.page_objects.eVoucher import evoucher
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TesEVoucher(ui_test_class.UVIClass):
    eVoucher_page: evoucher
    eVoucher_page: Coupon

    actual1 = "Your cart is empty"
    actual2 = "Invalid Coupon.!"
    actual3 = "Search for products..."


    @classmethod
    def setUpClass(cls):
        super(TesEVoucher, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesEVoucher, cls).tearDownClass()
        cls.driver.quit()

    def Signin(self):
        time.sleep(2)
        self.eVoucher_page.click_signin()
        self.eVoucher_page.EnterEmail("testaccount@quicklly.com")
        self.eVoucher_page.EnterPass("123456")
        self.eVoucher_page.click_login()

    def test_EnterZipCode(self):
        self.eVoucher_page.zip("60611")
        self.eVoucher_page.submit_zip()
        search = self.eVoucher_page.get_attribute(Coupon.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    # def test_EnterZipcode(self):
    #     self.Signin()
    #     time.sleep(2)
    #     self.eVoucher_page.EnterZipcode("60611")
    #     self.eVoucher_page.ClickSubmit()
    #     try:
    #         WebDriverWait(self.driver, 5).until(EC.alert_is_present())
    #         alert = self.driver.switch_to.alert
    #         alert.accept()
    #         print("alert Exists in page")
    #     except TimeoutException:
    #         print("alert does not Exist in page")
    #     time.sleep(2)
    #
    #     empty = self.eVoucher_page.get_attribute(Coupon.empty_cart, 'innerHTML')
    #     print(empty)
    #     self.assertEqual(self.actual1, empty)

    def test_addItem(self):
        time.sleep(1)
        self.eVoucher_page.click_Grocery()
        time.sleep(3)
        self.eVoucher_page.click_additem()
        self.eVoucher_page.click_AddItem1()
        self.eVoucher_page.click_additem2()
        self.eVoucher_page.click_additem3()
        self.eVoucher_page.click_additem4()
        self.eVoucher_page.click_MiniCart()
        self.Signin()
        self.eVoucher_page.click_Checkout()
        self.eVoucher_page.click_Checkout2()

    def test_checkInputMoreThanTextbox(self):
        self.eVoucher_page.EnterEvoucher("131618331813184844608426108494546449")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputLessThanTextbox(self):
        self.eVoucher_page.EnterEvoucher("13161833181318484460842610")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputNumbersOnly(self):
        self.eVoucher_page.EnterEvoucher("12458")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkCopyPaste(self):
        self.eVoucher_page.EnterEvoucher1("12458")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputDecimalNumbers(self):
        self.eVoucher_page.EnterEvoucher("52.4785")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputFormattedNumbers(self):
        self.eVoucher_page.EnterEvoucher("$110,00")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputAlphabets(self):
        self.eVoucher_page.EnterEvoucher("acvfdsbhjk")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputUpperCaseAlphabets(self):
        self.eVoucher_page.EnterEvoucher("ABXJUDBJNCU")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputLowerCaseAlphabets(self):
        self.eVoucher_page.EnterEvoucher("acvfdsbsdjv")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputMixAlphabets(self):
        self.eVoucher_page.EnterEvoucher("ABfgXJUer")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkSpecialCharacters(self):
        self.eVoucher_page.EnterEvoucher("!@#$%^&*()_+|}{:?><';/.,`")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkAllowSpecialCharacters(self):
        self.eVoucher_page.EnterEvoucher("!@#$%^&*()_+|}{:?><';/.,`")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkHTMLCharacters(self):
        self.eVoucher_page.EnterEvoucher("<h1>My First Heading</h1>")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkJavaScriptHTMLCharacters(self):
        self.eVoucher_page.EnterEvoucher("var x = 5;")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkSQLInjectionCharacters(self):
        self.eVoucher_page.EnterEvoucher("SELECT * FROM Users WHERE UserId = 105 OR 1=1;")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkOnlySpaces(self):
        self.eVoucher_page.EnterEvoucher("        ")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkBlankInput(self):
        self.eVoucher_page.EnterEvoucher("")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkTrailingSpaces(self):
        self.eVoucher_page.EnterEvoucher("    15d6c")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkLeadingSpaces(self):
        self.eVoucher_page.EnterEvoucher("15d6c     ")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)
