import time
from resources import ui_test_class
from resources.page_objects.rotikit import RotiBox
from resources.page_objects.rotikit import RotiKit
from selenium.webdriver.support.color import Color


class TesROTIKIT(ui_test_class.UVXVXIIIClass):
    roti_page: RotiKit
    roti_page: RotiBox

    actual1 = ""
    actual2 = " Order Roti Kit"
    actual3 = "Search for products..."
    actual4 = "Small Whole Wheat Rotis   "
    actual5 = "Fresh Tawa Roti"
    actual6 = "Roti"
    actual7 = "Multigrain Roti"
    actual8 = "Rotla"
    actual9 = "Paratha"
    actual10 = "Thepla"
    actual11 = "Specialty Roti"
    actual12 = "Bhakhri"
    actual13 = "Gluten Free"
    actual14 = "What We Deliver"
    actual15 = "Fresh Homemade Taste!"
    actual16 = "Premium Ingredients"
    actual17 = "Free Delivery"
    actual18 = "What are Rotis?"
    actual19 = "#446084"
    actual20 = "Expedite Delivery (Deliver in 1-2 business days)"
    actual21 = " Indian Bread Roti Kit"
    actual22 = "Thank you"

    @classmethod
    def setUpClass(cls):
        super(TesROTIKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesROTIKIT, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.roti_page.click_quicklly()
    #     time.sleep(3)
    #     self.roti_page.zip("60611")
    #     self.roti_page.submit_zip()
    #     time.sleep(5)
    #     for i in range(5):
    #         time.sleep(1)
    #         self.roti_page.click_RightArrow()
    #     self.roti_page.click_MealKit()
        # self.roti_page.click_rotiKit()

    def Payment(self):
        # self.roti_page.click_buildABox()
        # self.roti_page.click_AddRoti()
        # for i in range(4):
        #     time.sleep(1)
        #     self.roti_page.click_plusRoti()
        time.sleep(2)
        # self.roti_page.click_AddToCart()
        self.roti_page.click_MiniCart()
        self.roti_page.click_Checkout()
        time.sleep(5)
        # self.roti_page.click_Checkout2()
        # self.roti_page.click_payment1()
        # time.sleep(5)
        # self.roti_page.click_ProceedtoCheckout()
        # time.sleep(5)
        # self.roti_page.click_payment1()
        # time.sleep(5)
        # self.roti_page.click_Pay()
        # time.sleep(3)
        # thankYou = self.roti_page.get_attribute(RotiKit.ThankYou, 'innerHTML')
        # print(thankYou)

    def test_Signin(self):
        self.roti_page.select_dropdown()
        self.roti_page.click_signin()
        self.roti_page.EnterEmail("testaccount@quicklly.com")
        self.roti_page.EnterPass("123456")
        self.roti_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()

    def test_EnterZipCode(self):
        self.roti_page.zip("60611")
        self.roti_page.submit_zip()
        # self.Signin()
        search = self.roti_page.get_attribute(RotiKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(8)
        for i in range(6):
            time.sleep(1)
            self.roti_page.click_RightArrow()
            time.sleep(1)
        #self.roti_page.click_MealKit()
        self.roti_page.click_rotiKit()
        label = self.roti_page.get_attribute(RotiKit.RotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)
        self.roti_page.click_buildABox()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)
        time.sleep(3)
        # self.roti_page.click_DetailsCornRoti()
        # self.roti_page.click_CancelDetailsCornRoti()
        self.roti_page.click_AddWheatBakhri()
        # self.roti_page.click_AddWheatBakhri()
        # self.roti_page.click_AddWheatBakhri()
        self.roti_page.click_AddMasalaParatha()
        self.roti_page.click_PlusMasalaParatha()
        self.roti_page.click_PlusMasalaParatha()
        self.roti_page.click_MinusMasalaParatha()
        self.roti_page.click_PlusMasalaParatha()
        self.roti_page.click_PlusMasalaParatha()
        time.sleep(3)
        self.roti_page.click_AddToCart()
        time.sleep(10)
        # self.Payment()

    # def test_clickbuildABox(self):
    #     self.BactToPage()
        # time.sleep(5)
        # self.roti_page.click_buildABox()
        # label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual21, label)

    # def test_AddItems(self):
    #     self.test_clickIndian()
    #     time.sleep(3)
    #     self.roti_page.click_Weekly()
        # self.roti_page.click_buildABox()
        # label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual21, label)
        # time.sleep(3)
        # self.roti_page.click_AddWheatBakhri()
        # self.roti_page.click_AddWheatBakhri()
        # self.roti_page.click_AddWheatBakhri()
        # self.roti_page.click_AddMasalaParatha()
        # self.roti_page.click_PlusMasalaParatha()
        # self.roti_page.click_PlusMasalaParatha()
        # self.roti_page.click_MinusMasalaParatha()
        # self.roti_page.click_DetailsCornRoti()
        # self.roti_page.click_CancelDetailsCornRoti()
        # self.roti_page.click_AddToCart()
        # self.Payment()

    # def test_labelCategories(self):
    #     time.sleep(5)
    #     label = self.roti_page.get_attribute(RotiKit.categories, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual1, label)

    def test_labelWholeWheat(self):
        time.sleep(3)
        label = self.roti_page.get_attribute(RotiKit.wholewheatlabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelRoti(self):
        time.sleep(3)
        label = self.roti_page.get_attribute(RotiKit.rotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelMultiGrain(self):
        label = self.roti_page.get_attribute(RotiKit.MultiGrainLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelRotla(self):
        time.sleep(3)
        label = self.roti_page.get_attribute(RotiKit.RotlaLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelParatha(self):
        time.sleep(3)
        label = self.roti_page.get_attribute(RotiKit.ParathaLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual9, label)

    def test_labelSpecialRoti(self):
        label = self.roti_page.get_attribute(RotiKit.SpecialRotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelBakhri(self):
        time.sleep(3)
        self.roti_page.click_OrderRotiKit()
        self.BactToPage()
        time.sleep(3)
        label = self.roti_page.get_attribute(RotiKit.BakhriLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelWhatWeDeliver(self):
        label = self.roti_page.get_attribute(RotiKit.whatweDeliver, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelFresh(self):
        label = self.roti_page.get_attribute(RotiKit.FreshHomeMade, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelPremium(self):
        label = self.roti_page.get_attribute(RotiKit.Premium, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)
    #
    def test_labelFreeDelivery(self):
        label = self.roti_page.get_attribute(RotiKit.FreeDeivery, 'innerHTML')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_labelWhatAreRotis(self):
        label = self.roti_page.get_attribute(RotiKit.WhatareRotis, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_labelFreeDeliveryOnMinimumOrder(self):
        label = self.roti_page.get_attribute(RotiKit.FreeDeiveryOnMinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    # def test_weekly(self):
    #     time.sleep(3)
    #     self.BactToPage()
    #     time.sleep(3)
        # self.roti_page.click_weekly()
        # self.Payment()
        # thankYou = self.roti_page.get_attribute(RotiKit.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual22, thankYou)
    #
    # def test_clickbiweekly(self):
    #     time.sleep(3)
    #     self.BactToPage()
    #     time.sleep(3)
        # self.roti_page.click_Biweekly()
        # self.Payment()
        # thankYou = self.roti_page.get_attribute(RotiKit.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual22, thankYou)
    #
    # def test_monthly(self):
    #     time.sleep(3)
    #     self.BactToPage()
    #     time.sleep(3)
        # self.roti_page.click_Monthly()
        # self.Payment()
        # thankYou = self.roti_page.get_attribute(RotiKit.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual22, thankYou)

    # def test_once(self):
    #     time.sleep(3)
    #     self.BactToPage()
    #     time.sleep(3)
        # self.roti_page.click_Once()
        # self.Payment()
        # thankYou = self.roti_page.get_attribute(RotiKit.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual22, thankYou)

