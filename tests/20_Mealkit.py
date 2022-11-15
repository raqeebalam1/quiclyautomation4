import time

from selenium.webdriver.common import alert

from resources import ui_test_class
from resources.page_objects.indianmeal import IndianMeal
from resources.page_objects.indianmeal import IndianMealKit
from selenium.webdriver.support.color import Color


class TesROTIKIT(ui_test_class.UVXVXIVClass):
    mealkit_page: IndianMeal
    mealkit_page: IndianMealKit

    actual1 = "Choose meal kit box"
    actual2 = "5 Meal Kit"
    actual3 = "Search for products..."
    actual4 = "Ready-to-Eat Meal Kit"
    actual5 = "Shipping"
    actual6 = "Free"
    actual7 = "Price"
    actual8 = "Dry Packed Meal Kit"
    actual9 = "HOW IT WORKS"
    actual10 = "Select Your Meal"
    actual11 = "We Cook & Deliver "
    actual12 = "Heat, Eat & Enjoy"
    actual13 = "#3155a6"
    actual14 = "OUR PRODUCTS"
    actual15 = "Enjoy the comfort of homely Indian food"
    actual16 = " Indian Food Subscription Box"
    actual17 = "Free Delivery"
    actual18 = "Thank you"
    actual19 = "Indian Meal Kit Delivery"
    actual20 = "10 Meal Kit"
    actual21 = "20 Meal Kit"

    @classmethod
    def setUpClass(cls):
        super(TesROTIKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesROTIKIT, cls).tearDownClass()
        cls.driver.quit()


    def Signin(self):
        self.mealkit_page.select_dropdown()
        self.mealkit_page.click_signin()
        self.mealkit_page.EnterEmail("testaccount@quicklly.com")
        self.mealkit_page.EnterPass("123456")
        self.mealkit_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.mealkit_page.zip("60611")
        self.mealkit_page.submit_zip()
        self.Signin()
        search = self.mealkit_page.get_attribute(IndianMealKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(6):
            time.sleep(5)
            self.mealkit_page.click_LeftArrow()
        self.mealkit_page.click_MealKit()
        self.mealkit_page.click_indianMealKitSub()
        time.sleep(3)
        label1 = self.mealkit_page.get_attribute(IndianMealKit.IndianMealKitDelivery, 'innerHTML')
        print(label1)
        self.assertEqual(self.actual19, label1)


    def test_clickmeal20(self):
        time.sleep(3)
        self.mealkit_page.click_Biweekly3()
    #     self.mealkit_page.click_Once2()
        self.mealkit_page.click_20mealkit()
        label = self.mealkit_page.get_attribute(IndianMealKit.indianSubscription, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)
        self.mealkit_page.click_Bisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_PlusBisibelebath()
        self.mealkit_page.click_MinusBisiblebath()
        self.mealkit_page.click_DetailsMisalpav()
        self.mealkit_page.click_CloseDetailsMisalpav()
        self.mealkit_page.click_DalFry()
        self.mealkit_page.click_MasalaBhindi()
        self.mealkit_page.click_Pudinarice()
        self.mealkit_page.click_AddGajarhalwa()
        self.mealkit_page.click_PlusGajarhalwa()
        self.mealkit_page.click_PlusGajarhalwa()
        self.mealkit_page.click_PlusGajarhalwa()
        self.mealkit_page.click_PlusGajarhalwa()
        self.mealkit_page.click_PlusGajarhalwa()
        # self.mealkit_page.click_AddToCart()
        self.mealkit_page.click_Indianmealkitdelivery()

    def test_clickmeal20_M(self):
        time.sleep(3)
        self.mealkit_page.click_Monthly3()
        self.mealkit_page.click_20mealkit()
        label = self.mealkit_page.get_attribute(IndianMealKit.indianSubscription, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)
        time.sleep(3)
        self.mealkit_page.click_Bisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_MinusBisiblebath2()
        self.mealkit_page.click_DalFry2()
        self.mealkit_page.click_MasalaBhindi2()
        self.mealkit_page.click_Pudinarice2()
        self.mealkit_page.click_AddGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_Indianmealkitdelivery()

    def test_clickmeal20_O(self):
        time.sleep(3)
        self.mealkit_page.click_Once3()
        self.mealkit_page.click_20mealkit()
        label = self.mealkit_page.get_attribute(IndianMealKit.indianSubscription, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)
        self.mealkit_page.click_Bisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_PlusBisibelebath2()
        self.mealkit_page.click_MinusBisiblebath2()
        self.mealkit_page.click_DalFry2()
        self.mealkit_page.click_MasalaBhindi2()
        self.mealkit_page.click_Pudinarice2()
        self.mealkit_page.click_AddGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_PlusGajarhalwa2()
        self.mealkit_page.click_AddToCart2()
        self.Payment()

    # def test_labelChooseMeal(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.chooseMEal, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual1, label)

    # def test_labelReadyToEAt(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.readyToEat, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual4, label)

    # def test_labelShipping(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.shipping, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual5, label)
    #
    # def test_labelFree(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.free, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual6, label)
    #
    # def test_labelPrice(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.price, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual7, label)
    #
    # def test_labelDryPacked(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.dryPacked, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual8, label)

    # def test_labelHowItWorks(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.howItWorks, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual9, label)
    #
    # def test_labelSelectMeal(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.selectMeal, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual10, label)
    #
    # def test_labelCookAndDeliver(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.cookAndDeliver, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual11, label)
    #
    # def test_labelEatAndEnjoy(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.eatAndEnjoy, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual12, label)
    #
    # def test_labelOurProducts(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.OurProducts, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual14, label)
    #
    # def test_labelEnjoyTheComfort(self):
    #     label = self.mealkit_page.get_attribute(IndianMealKit.enjoyTheComfort, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual15, label)

    # def test_clickweekly(self):
    #     self.mealkit_page.click_IMKS()
        # self.BactToPage()
        # self.mealkit_page.click_weekly()
        # colorLabel = self.driver.find_element_by_css_selector(
        #     '#searchhide > section.productsection > div > div > div.organicproductcontent.icecreamsubscription.firstpp1 > div > div.divcustomtabpanels > ul > li.weekly.tablinks.active').value_of_css_property('background-color')
        # hex = Color.from_string(colorLabel).hex
        # print(hex)
        # self.assertEqual(self.actual13, hex)

    # def test_clickbiweekly(self):
    #     self.mealkit_page.click_Biweekly()
    #     self.Payment()
    #     thankYou = self.mealkit_page.get_attribute(IndianMealKit.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickmonthly(self):
    #     self.mealkit_page.click_Monthly()
    #     self.Payment()
    #     thankYou = self.mealkit_page.get_attribute(IndianMealKit.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickonce(self):
    #     self.mealkit_page.click_Once()
    #     self.Payment()
    #     thankYou = self.mealkit_page.get_attribute(IndianMealKit.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickweekly1(self):
    #     self.mealkit_page.click_weekly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > section.productsection > div > div > div.organicproductcontent.icecreamsubscription.firstpp2 > div > div.divcustomtabpanels > ul > li.weekly.tablinks').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickbiweekly2(self):
    #     self.BactToPage()
    #     self.mealkit_page.click_Biweekly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > section.productsection > div > div > div.organicproductcontent.icecreamsubscription.firstpp2 > div > div.divcustomtabpanels > ul > li.bi-weekly.tablinks').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickmonthly2(self):
    #     self.BactToPage()
    #     self.mealkit_page.click_Monthly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > section.productsection > div > div > div.organicproductcontent.icecreamsubscription.firstpp2 > div > div.divcustomtabpanels > ul > li.monthly.tablinks').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickonce2(self):
    #     self.BactToPage()
    #     self.mealkit_page.click_Once2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > section.productsection > div > div > div.organicproductcontent.icecreamsubscription.firstpp2 > div > div.divcustomtabpanels > ul > li.one-time.tablinks.active').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickselectProducts(self):
    #     self.mealkit_page.click_selectProduct()
    #     label = self.mealkit_page.get_attribute(IndianMealKit.SubscriptionBox, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual16, label)
    #
    # def test_clickselectProducts2(self):
    #     self.mealkit_page.click_IMKS()
    #     self.mealkit_page.click_selectProduct2()
    #     label = self.mealkit_page.get_attribute(IndianMealKit.SubscriptionBox, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual16, label)

    def Payment(self):
        time.sleep(5)
        self.mealkit_page.click_MiniCart1()
        self.mealkit_page.click_Checkout()
        time.sleep(5)
        # self.mealkit_page.click_ProceedtoCheckout()
        # time.sleep(5)
        # self.mealkit_page.click_payment1()