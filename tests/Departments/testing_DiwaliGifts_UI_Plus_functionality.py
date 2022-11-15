import time
from resources import ui_test_class
from resources.page_objects.diwali import Diwali_Kit
from resources.page_objects.diwali import DiwaliGift
from selenium.webdriver.support.color import Color


class TesDIWALI(ui_test_class.UVXVVXIIIClass):
    diwali_page: DiwaliGift
    diwali_page: Diwali_Kit

    actual1 = "Choose meal kit box"
    actual2 = "5 Meal Kit"
    actual3 = "Search for products..."
    actual4 = "Personalized Gift Basket"

    @classmethod
    def setUpClass(cls):
        super(TesDIWALI, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDIWALI, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.mealkit_page.click_quicklly()
    #     self.mealkit_page.zip("60611")
    #     self.mealkit_page.submit_zip()
    #     time.sleep(5)
    #     for i in range(6):
    #         time.sleep(1)
    #         self.mealkit_page.click_RightArrow()
    #     self.mealkit_page.click_MealKit()
    #     time.sleep(3)
    #     self.mealkit_page.click_indianMealKitSub()



    def Signin(self):
        self.diwali_page.select_dropdown()
        self.diwali_page.click_signin()
        self.diwali_page.EnterEmail("testaccount@quicklly.com")
        self.diwali_page.EnterPass("123456")
        self.diwali_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.diwali_page.zip("60611")
        self.diwali_page.submit_zip()
        self.Signin()
        search = self.diwali_page.get_attribute(Diwali_Kit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        # for i in range(5):
        #     time.sleep(5)
        #     self.diwali_page.click_LeftArrow()
        self.diwali_page.click_DiwaliGift()
        self.diwali_page.click_GiftNow()
        self.diwali_page.zip("60611")
        self.diwali_page.submit_zip1()
        time.sleep(3)
        label1 = self.diwali_page.get_attribute(Diwali_Kit.GiftBasketLabel, 'innerHTML')
        print(label1)
        self.assertEqual(self.actual4, label1)


    def test_AddingToCart(self):
        time.sleep(3)
        self.diwali_page.SmallPack()
        self.diwali_page.SubmitDeal()
        self.diwali_page.PlusSmallBox()
        self.diwali_page.PlusSmallBox()
        self.diwali_page.MinusSmallBox()
        self.diwali_page.RectangleBox()
        # self.diwali_page.SubmitDeal()
        self.diwali_page.BurfiBox()
        # self.diwali_page.SubmitDeal()
        self.diwali_page.DetailsComboBox()
        self.diwali_page.CloseDetailsComboBox()
        self.diwali_page.Click_Next()
        self.test_AddRecipient()
        self.Payment()

    def test_AddRecipient(self):
        # self.depart_page.select_dropdown()
        # self.depart_page.click_signin()
        self.diwali_page.RecipientFName("Test")
        self.diwali_page.RecipientLName("Account")
        self.diwali_page.RecipientEmail("testaccount@quicklly.com")
        self.diwali_page.RecipientPhone("1234567890")
        self.diwali_page.RecipientAddress("1400 N Lake Shore Dr, Chicago, IL, USA")
        self.diwali_page.RecipientApartment("1")
        self.diwali_page.click_Submit()
        self.diwali_page.click_Skipthistep()
        time.sleep(3)

    def Payment(self):
        self.diwali_page.click_MiniCart()
        self.diwali_page.click_Checkout()
        time.sleep(5)
        self.diwali_page.click_ProceedtoCheckout()
        time.sleep(5)
        self.diwali_page.click_payment1()
        time.sleep(5)
        self.diwali_page.click_Pay()
        time.sleep(3)
        thankYou = self.mealkit_page.get_attribute(Diwali_Kit.ThankYou, 'innerHTML')
        print(thankYou)