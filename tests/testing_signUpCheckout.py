import time
from resources import ui_test_class
from resources.page_objects.SignUpCheckout_page import SUC
from resources.page_objects.SignUpCheckout_page import SignUpCheckout


class TesDEPARTMENT(ui_test_class.UVXVIIIClass):
    signupcheckout_page: SUC
    signupcheckout_page: SignUpCheckout

    actual1 = "Thank you"
    actual2 = "Your account"
    actual3 = "Search for products..."

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def food(self):
        time.sleep(2)
        self.signupcheckout_page.click_food()
        time.sleep(2)
        self.signupcheckout_page.click_MakkiFood()
        self.signupcheckout_page.click_addTenders()
        self.signupcheckout_page.click_AddToCartTenders()
        time.sleep(4)
        self.signupcheckout_page.click_submitTenders()
        self.signupcheckout_page.click_MiniCart()
        self.signupcheckout_page.click_Checkout()
        self.signupcheckout_page.click_payment1()
        time.sleep(5)
        self.signupcheckout_page.click_Pay()
        time.sleep(10)

    def Grocery(self):
        time.sleep(2)
        self.signupcheckout_page.EnterElementForSearch("lemon grass")
        self.signupcheckout_page.click_SearchButton()
        self.signupcheckout_page.click_additem()
        self.signupcheckout_page.click_ADDLG()
        time.sleep(5)
        self.signupcheckout_page.click_addPotato()
        self.signupcheckout_page.click_AddToCartPotato()
        self.signupcheckout_page.click_MiniCart1()
        self.signupcheckout_page.click_Checkout()
        self.signupcheckout_page.click_Checkout2()
        self.signupcheckout_page.click_payment1()
        time.sleep(5)
        self.signupcheckout_page.click_Pay()
        time.sleep(10)

    def Catering(self):
        time.sleep(2)
        self.signupcheckout_page.click_LeftArrow()
        self.signupcheckout_page.click_Catering()
        time.sleep(1)
        self.signupcheckout_page.click_Hyderabad()
        time.sleep(2)
        self.signupcheckout_page.click_AddBeef()
        self.signupcheckout_page.click_AddToCartBeef()
        self.signupcheckout_page.click_Delivery()
        time.sleep(5)
        self.signupcheckout_page.click_timeOfDelivery()
        self.signupcheckout_page.Submit_Beef()
        self.signupcheckout_page.click_MiniCart()
        time.sleep(5)
        self.signupcheckout_page.click_Checkout()
        self.signupcheckout_page.click_needAccount()
        self.signupcheckout_page.firstName("quicklly")
        self.signupcheckout_page.lastName("test")
        self.signupcheckout_page.Address("Chicago Riverwalk, Chicago, IL 60611, USA")
        self.signupcheckout_page.Phone("2233561248")
        self.signupcheckout_page.emailAddress("quicklly2042@gmail.com")
        self.signupcheckout_page.Password("123456")
        self.signupcheckout_page.ConfirmPassword("123456")
        self.signupcheckout_page.click_Register()
        time.sleep(15)
        self.signupcheckout_page.click_payment1()
        time.sleep(25)
        self.signupcheckout_page.EnterCardNumber("5555444433331111")
        time.sleep(5)
        self.signupcheckout_page.EnterExpirationDate("0225")
        self.signupcheckout_page.EnterCVV("158")
        time.sleep(2)
        self.signupcheckout_page.click_Pay1()
        time.sleep(10)

    def tiffin(self):
        self.signupcheckout_page.click_quicklly()
        self.signupcheckout_page.submit_zip()
        time.sleep(5)
        for i in range(4):
            self.signupcheckout_page.click_RightArrow()
            time.sleep(3)
        self.signupcheckout_page.click_Tiffin()
        self.signupcheckout_page.click_Chicago()
        self.signupcheckout_page.select_VegThali()
        self.signupcheckout_page.click_AddToCartVT()
        self.signupcheckout_page.submitVT()
        self.signupcheckout_page.click_AddToCartVT()
        self.signupcheckout_page.click_MiniCart()
        self.signupcheckout_page.click_Checkout()
        self.signupcheckout_page.click_Checkout2()
        time.sleep(5)
        self.signupcheckout_page.click_payment1()
        self.signupcheckout_page.click_Pay()
        time.sleep(10)

    def MealKit(self):
        self.signupcheckout_page.click_quicklly()
        self.signupcheckout_page.submit_zip()
        time.sleep(2)
        self.signupcheckout_page.click_MealKit()
        self.signupcheckout_page.click_IndianMealKit()
        self.signupcheckout_page.click_SelectProducts()
        self.signupcheckout_page.click_AddMixVegetable()
        self.signupcheckout_page.click_AddMisalPav()
        for i in range(10):
            self.signupcheckout_page.click_PlusMixVegetable()
        self.signupcheckout_page.click_AddToCartNW()
        self.signupcheckout_page.click_MiniCart()
        self.signupcheckout_page.click_Checkout()
        self.signupcheckout_page.click_Checkout2()
        self.signupcheckout_page.click_payment1()
        time.sleep(5)
        self.signupcheckout_page.click_Pay()
        time.sleep(10)

    def test_EnterZipCode(self):
        self.signupcheckout_page.zip("60611")
        self.signupcheckout_page.submit_zip()
        search = self.signupcheckout_page.get_attribute(SignUpCheckout.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_shopWithGrocery(self):
        self.signupcheckout_page.click_quicklly()
        self.signupcheckout_page.submit_zip()
        self.Grocery()
        ThankYouLabel = self.signupcheckout_page.get_attribute(SignUpCheckout.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithFood(self):
        self.signupcheckout_page.click_quicklly()
        self.signupcheckout_page.submit_zip()
        self.food()
        ThankYouLabel = self.signupcheckout_page.get_attribute(SignUpCheckout.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithCatering(self):
        self.Catering()
        ThankYouLabel = self.signupcheckout_page.get_attribute(SignUpCheckout.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithTiffin(self):
        self.tiffin()
        ThankYouLabel = self.signupcheckout_page.get_attribute(SignUpCheckout.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

    # def test_shopWithMealKit(self):
    #     self.MealKit()
    #     ThankYouLabel = self.signupcheckout_page.get_attribute(SignUpCheckout.ThankYou, 'innerHTML')
    #     print(ThankYouLabel)
    #     self.assertEqual(self.actual1, ThankYouLabel)
