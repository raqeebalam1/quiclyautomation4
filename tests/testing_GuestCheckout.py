import time
from resources import ui_test_class
from resources.locators import GuestCheckout
from resources.page_objects.guestCheckout_page import CheckoutWithGuest


class TesCHECKOUTWITHGUEST(ui_test_class.UVXIIClass):
    guestCheckout_page: GuestCheckout
    guestCheckout_page: CheckoutWithGuest

    actualLabel = "Items in your  cart"
    label = ""

    @classmethod
    def setUpClass(cls):
        super(TesCHECKOUTWITHGUEST, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCHECKOUTWITHGUEST, cls).tearDownClass()
        cls.driver.quit()

    def Checkout(self):
        self.guestCheckout_page.enterZip("60611")
        self.guestCheckout_page.click_SubmitZip()
        time.sleep(2)
        self.guestCheckout_page.EnterElementForSearch("lemon grass")
        self.guestCheckout_page.click_SearchButton()
        time.sleep(2)
        self.guestCheckout_page.click_Potato()
        self.guestCheckout_page.click_AddToCart()
        self.guestCheckout_page.click_Cart()
        self.guestCheckout_page.click_Checkout()
        self.guestCheckout_page.click_checkout2()
        time.sleep(3)
        self.guestCheckout_page.click_guestLogin()
        self.guestCheckout_page.Enter_Name("quicklly")
        self.guestCheckout_page.Enter_Name2("test")
        self.guestCheckout_page.EnterAddress("East Chicago Avenue, Chicago, IL 60611, USA")
        self.guestCheckout_page.EnterNumber("1452336548")
        self.guestCheckout_page.Enter_email("qicklly1245@gmail.com")
        self.guestCheckout_page.click_submit()
        time.sleep(10)
        self.label = self.guestCheckout_page.get_attribute(GuestCheckout.shoppingCarts, 'innerHTML')
        print(self.label)

    def test_guestCheckout(self):
        self.Checkout()
        self.assertEqual(self.label, self.actualLabel)
