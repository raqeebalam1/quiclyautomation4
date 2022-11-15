import time
from resources import ui_test_class
from resources.page_objects.indianseasoningkit import Indian
from resources.page_objects.indianseasoningkit import IndianSeasoningKit
from selenium.webdriver.support.color import Color


class TesINDIANSEASONING(ui_test_class.UVXVXIClass):
    indian_page: Indian
    indian_page: IndianSeasoningKit

    actual1 = " CHOOSE YOUR MENU"
    actual2 = " Indian Seasoning Kit"
    actual3 = "Search for products..."
    actual4 = "Flavors so familiar, Yet so different."
    actual5 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2014.png"
    actual6 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2013.png"
    actual7 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2015.png"
    actual8 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2017.png"
    actual9 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2020.png"
    actual10 = "https://www.uat.goquicklly.com/images/seasoning_kit/Assets/image%2016.png"
    actual11 = "Indian Seasoning"
    actual12 = "Easy Indie Bowls"
    actual13 = "#f9660d"
    actual14 = "Seasonings Kit"
    actual15 = "Easy Indie Bowl Kit"
    actual16 = " Order Seasoning Kit"
    actual17 = " Easy Indie Bowl"
    actual18 = "Thank you"
    actual19 = "Seasoning Kit"
    actual20 = "Easy Indie Bowls"
    actual21 = "Signature Blends"
    actual22 = "Pure Spices"
    actual23 = "Whole Spices"
    actual24 = "Red Hot Chilli Powder Mirch"
    actual25 = "Kashmiri Mirch Powder"
    actual26 = "Curry Powder"
    actual27 = "Cumin Powder"
    actual28 = "Spicy Chicken"


    @classmethod
    def setUpClass(cls):
        super(TesINDIANSEASONING, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANSEASONING, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.indian_page.click_quicklly()
    #     self.indian_page.zip("60611")
    #     self.indian_page.submit_zip()
    #     time.sleep(2)
    #     for i in range(10):
    #         time.sleep(1)
    #         self.indian_page.click_RightArrow()
    #     self.indian_page.click_MealKit()
    #     self.indian_page.click_indianSeasoning()

    def Payment(self):
        # self.indian_page.click_selectProduct()
        # self.indian_page.click_redHotChilli()
        # time.sleep(2)
        self.indian_page.click_MiniCart()
        time.sleep(3)
        self.indian_page.click_Checkout()
        time.sleep(3)
        # self.indian_page.click_Checkout2()
        # time.sleep(3)
        self.indian_page.click_ProceedtoCheckout()
        time.sleep(5)
        self.indian_page.click_payment1()
        time.sleep(5)
        self.indian_page.click_Pay()
        time.sleep(3)
        thankYou = self.indian_page.get_attribute(IndianSeasoningKit.ThankYou, 'innerHTML')
        print(thankYou)

    def Signin(self):
        self.indian_page.select_dropdown()
        self.indian_page.click_signin()
        self.indian_page.EnterEmail("testaccount@quicklly.com")
        self.indian_page.EnterPass("123456")
        self.indian_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.indian_page.zip("60611")
        self.indian_page.submit_zip()
        self.Signin()
        time.sleep(5)
        search = self.indian_page.get_attribute(IndianSeasoningKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(11):
            time.sleep(1)
            self.indian_page.click_RightArrow()
        time.sleep(2)
        self.indian_page.click_MealKit()
        time.sleep(2)
        self.indian_page.click_indianSeasoning()
        time.sleep(2)
        label = self.indian_page.get_attribute(IndianSeasoningKit.IndianSeasoningLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)
        time.sleep(5)
        self.indian_page.click_Seasoningkit()
        label = self.indian_page.get_attribute(IndianSeasoningKit.OrderSeasoningKit, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)
        time.sleep(3)
        self.indian_page.click_AddRedMirch()
        self.indian_page.click_Addchatmasala()
        self.indian_page.click_AddkashmiriMirch()
        self.indian_page.click_Pluschatmasala()
        self.indian_page.click_Minuschatmasala()
        self.indian_page.click_DetailsKitchenKing()
        self.indian_page.click_CancelDetailsKitchenKing()
        self.indian_page.click_AddToCart()
        time.sleep(10)
        # self.Payment()

    def test_labelSeasoning(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelSeasoning, 'innerHTML')
        print(label)
        self.assertEqual(self.actual19, label)

    def test_labelIndieBowl(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelEasybowl, 'innerHTML')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_labelSignatureBlend(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelSignature, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelPureSpicees(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelSpices, 'innerHTML')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelWholeSpices(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelWholespices, 'innerHTML')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelChilli(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelChilipowder, 'innerHTML')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelKashmiri(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelKashmiri, 'innerHTML')
        print(label)
        self.assertEqual(self.actual25, label)

    def test_labelCurry(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelCurrypowder, 'innerHTML')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_labelCumin(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelCuminpowder, 'innerHTML')
        print(label)
        self.assertEqual(self.actual27, label)

    def test_labelSpicyChicken(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelSpicycchicken, 'innerHTML')
        print(label)
        self.assertEqual(self.actual28, label)

    # def test_SeasoningsKit(self):
    #     time.sleep(3)
        # self.indian_page.click_indianSeasoning()
        # label = self.indian_page.get_attribute(IndianSeasoningKit.IndianSubscription, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual2, label)
        # self.indian_page.click_Seasoningkit()
        # label = self.indian_page.get_attribute(IndianSeasoningKit.OrderSeasoningKit, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual16, label)
        # time.sleep(3)

    # def test_Addtocart(self):
    #     self.test_SeasoningsKit()
        # time.sleep(5)
        # self.indian_page.click_Seasoningkit()
        # self.indian_page.click_AddRedMirch()
        # self.indian_page.click_Addchatmasala()
        # self.indian_page.click_AddkashmiriMirch()
        # self.indian_page.click_Pluschatmasala()
        # self.indian_page.click_Minuschatmasala()
        # self.indian_page.click_DetailsKitchenKing()
        # self.indian_page.click_CancelDetailsKitchenKing()
        # self.indian_page.click_AddToCart()
        # self.Payment()

    # def test_labelchooseyourmenu(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.chooseyourmenu, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual1, label)
    #
    # def test_flavour(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.flavours, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual4, label)
    #
    # def test_imageBlackPepper(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.blackPepperImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual5, image)
    #
    # def test_imageStarFlower(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.startFLowerImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual6, image)
    #
    # def test_imageElaichi(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.ElaichiImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual7, image)
    #
    # def test_imageTurmeric(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.turmericImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual8, image)
    #
    # def test_imageNutmeg(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.nutmegImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual9, image)
    #
    # def test_imageCuminSeed(self):
    #     image = self.indian_page.get_attribute(IndianSeasoningKit.CuminSeedImage, 'src')
    #     print(image)
    #     self.assertEqual(self.actual10, image)
    #
    # def test_labelIndianSeasoning(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.ISL, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual11, label)
    #
    # def test_labelEasyIndieBowls(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.easyIndieBowls, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual12, label)
    #
    # def test_labelSeasoningKit(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.seasoningKitLabel, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual14, label)
    #
    # def test_labelEasyIndianBowlKit(self):
    #     label = self.indian_page.get_attribute(IndianSeasoningKit.EasyIndianLabel, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual15, label)
    #
    # def test_clickweekly(self):
    #     self.indian_page.click_ISK()
    #     self.BactToPage()
    #     self.indian_page.click_weekly()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#seasn1 > div:nth-child(1) > center > ul > li:nth-child(2)').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickbiweekly(self):
    #     self.BactToPage()
        # self.indian_page.click_quicklly()
        # self.indian_page.zip("60611")
        # self.indian_page.submit_zip()
        # time.sleep(2)
        # for i in range(10):
        #     time.sleep(1)
        #     self.indian_page.click_RightArrow()
        # self.indian_page.click_MealKit()
        # self.indian_page.click_indianSeasoning()
        # self.indian_page.click_Biweekly()
        # self.Payment()
        # thankYou = self.indian_page.get_attribute(IndianSeasoningKit.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickmonthly(self):
    #     self.BactToPage()
    #     self.indian_page.click_Monthly()
    #     self.Payment()
    #     thankYou = self.indian_page.get_attribute(IndianSeasoningKit.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickonce(self):
    #     self.indian_page.click_quicklly()
    #     self.indian_page.zip("60611")
    #     self.indian_page.submit_zip()
    #     time.sleep(2)
    #     for i in range(10):
    #         time.sleep(1)
    #         self.indian_page.click_RightArrow()
    #     self.indian_page.click_MealKit()
    #     self.indian_page.click_indianSeasoning()
    #     self.indian_page.click_Once()
    #     self.Payment()
    #     thankYou = self.indian_page.get_attribute(IndianSeasoningKit.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual18, thankYou)
    #
    # def test_clickweekly1(self):
    #     self.indian_page.click_weekly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(2)').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickbiweekly2(self):
    #     self.BactToPage()
    #     self.indian_page.click_Biweekly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(3)').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickmonthly2(self):
    #     self.BactToPage()
    #     self.indian_page.click_Monthly2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#seasn1 > div:nth-child(2) > center > ul > li.active').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
    #
    # def test_clickonce2(self):
    #     self.BactToPage()
    #     self.indian_page.click_Once2()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(1)').value_of_css_property('background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual13, hex)
#
#
#