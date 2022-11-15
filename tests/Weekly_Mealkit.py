import time
from resources import ui_test_class
from resources.page_objects.weekly_page import WEEKLY
from resources.page_objects.weekly_page import Weekly

class TesWEEKLYORDER(ui_test_class.UVXVXVIIIClass):
    weekly_page: WEEKLY
    weekly_page: Weekly

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"
    actual19 = "Indian Meal Kit Delivery"

    @classmethod
    def setUpClass(cls):
        super(TesWEEKLYORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesWEEKLYORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.weekly_page.zip("60611")
        self.weekly_page.submit_zip()
        search = self.weekly_page.get_attribute(Weekly.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.weekly_page.select_dropdown()
        self.weekly_page.click_signin()
        self.weekly_page.EnterEmail("testaccount@quicklly.com")
        self.weekly_page.EnterPass("123456")
        self.weekly_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(11):
            time.sleep(5)
            self.weekly_page.click_RightArrow()
        self.weekly_page.click_MealKit()
        self.weekly_page.click_indianMealKitSub()
        time.sleep(3)
        label1 = self.weekly_page.get_attribute(Weekly.IndianMealKitDelivery, 'innerHTML')
        print(label1)
        self.assertEqual(self.actual19, label1)

    # def test_clickmeal10(self):
    #     time.sleep(3)
    #     self.weekly_page.click_Biweekly2()
    #     self.mealkit_page.click_Monthly2()
    #     self.mealkit_page.click_Once2()
    #     self.weekly_page.click_10mealkit()
    #     label = self.weekly_page.get_attribute(Weekly.indianSubscription, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #     self.weekly_page.click_Bisibelebath()
    #     self.weekly_page.click_PlusBisibelebath()
    #     self.weekly_page.click_PlusBisibelebath()
    #     self.weekly_page.click_PlusBisibelebath()
    #     self.weekly_page.click_MinusBisiblebath()
    #     self.weekly_page.click_DetailsMisalpav()
    #     self.weekly_page.click_CloseDetailsMisalpav()
    #     self.weekly_page.click_DalFry()
    #     self.weekly_page.click_MasalaBhindi()
    #     self.weekly_page.click_Pudinarice()
    #     self.weekly_page.click_AddGajarhalwa()
    #     self.weekly_page.click_PlusGajarhalwa()
    #     self.weekly_page.click_PlusGajarhalwa()
    #     self.weekly_page.click_PlusGajarhalwa()
    #     self.mealkit_page.click_AddToCart()
    #     self.Payment()
    #
    # def Payment(self)
    #     time.sleep(5)
    #     self.mealkit_page.click_MiniCart()
    #     self.mealkit_page.click_Checkout()
    #     time.sleep(5)
    #     self.mealkit_page.click_ProceedtoCheckout()
    #     time.sleep(5)
    #     self.mealkit_page.click_payment1()
    #     time.sleep(5)
    #     self.mealkit_page.click_Pay()
#