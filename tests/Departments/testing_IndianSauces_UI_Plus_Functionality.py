import time
from resources import ui_test_class
from resources.page_objects.IndianSauces import IndianMealKitAndSauces
from resources.page_objects.IndianSauces import Sauces
from selenium.webdriver.support.color import Color

class TesINDIANSAUCES(ui_test_class.UVXVXVClass):
    sauces_page: IndianMealKitAndSauces
    sauces_page: Sauces

    actual1 = "EXPLORE OUR MENUS"
    actual2 = "Sauces"
    actual3 = "Search for products..."
    actual4 = "Meal Kit"
    actual5 = "Sauces"
    actual6 = "EFFORTLESS COOKING: HOW IT WORKS?"
    actual7 = "Step 1."
    actual8 = "Step 2."
    actual9 = "Step 3."
    actual10 = "Step 4."
    actual11 = "From Fridge to Pot: 2 - 3 mins"
    actual12 = "Set Pot to Cook: 1 min"
    actual13 = "Relax: 15+ mins"
    actual14 = "Enjoy!"
    actual15 = "OUR FOOD PHILOSOPHY"
    actual16 = " Indian Food Subscription Box"
    actual17 = "Nationwide"
    actual18 = "Bay Area"
    actual19 = "#000000"
    actual20 = "Meal Kit"
    actual21 = "Sauces"
    actual22 = "Eat Everything"
    actual23 = "Nut Free Meal Kit"
    actual24 = "Vegan Meal Kit"
    actual25 = "Vegan Meal Kit"
    actual26 = "Indian Instant Pot"
    actual27 = "Thank you"
    actual28 = "Shop Seeti"
    actual29 = "Chicken Biryani Sauce"
    actual30 = "Shahi Paneer Sauce"
    actual31 = "Mas Meat Curry Sauce"
    actual32 = "Palak Paneer Sauce"
    actual33 = "Chana Masala Sauce"
    actual34 = "Better Butter Chicken Sauce"
    actual35 = "Mistress of Sauces Pack"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANSAUCES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANSAUCES, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.sauces_page.click_quicklly()
    #     self.sauces_page.zip("60611")
    #     self.sauces_page.submit_zip()
    #     time.sleep(2)
    #     for i in range(9):
    #         time.sleep(1)
    #         self.sauces_page.click_RightArrow()
    #     self.sauces_page.click_MealKit()
    #     self.sauces_page.click_Oragnicsauces()

    def Payment(self):
        # self.sauces_page.click_Shahi()
        # self.sauces_page.click_AddToCartShai()
        # self.test_Addtocart()
        time.sleep(2)
        self.sauces_page.click_MiniCart()
        self.sauces_page.click_Checkout()
        self.sauces_page.click_Checkout2()
        self.sauces_page.click_payment1()
        time.sleep(5)
        self.sauces_page.click_Pay()
        thankYou = self.sauces_page.get_attribute(IndianMealKitAndSauces.ThankYou, 'innerHTML')
        print(thankYou)

    def Signin(self):
        self.sauces_page.select_dropdown()
        self.sauces_page.click_signin()
        self.sauces_page.EnterEmail("testaccount@quicklly.com")
        self.sauces_page.EnterPass("123456")
        self.sauces_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.sauces_page.zip("60611")
        self.sauces_page.submit_zip()
        self.Signin()
        search = self.sauces_page.get_attribute(IndianMealKitAndSauces.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(9):
            time.sleep(2)
            self.sauces_page.click_RightArrow()
        self.sauces_page.click_MealKit()
        self.sauces_page.click_Oragnicsauces()
        self.sauces_page.click_Sauces()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.instantPot, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)
        self.sauces_page.click_Shahi()
        self.sauces_page.click_Shahi()
        self.sauces_page.click_Chanamasala()
        self.sauces_page.click_Palakpanersauce()
        time.sleep(10)
        # self.Payment()

    def test_labelSeeti(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Shopseeti, 'innerHTML')
        print(label)
        self.assertEqual(self.actual28, label)

    def test_labelBiryani(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Biryani, 'innerHTML')
        print(label)
        self.assertEqual(self.actual29, label)

    def test_labelPaneer(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Paneer, 'innerHTML')
        print(label)
        self.assertEqual(self.actual30, label)

    def test_labelMasMeat(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.MasMeat, 'innerHTML')
        print(label)
        self.assertEqual(self.actual31, label)

    def test_labelPalak(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Palak, 'innerHTML')
        print(label)
        self.assertEqual(self.actual32, label)

    def test_labelChana(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.ChannaMasala, 'innerHTML')
        print(label)
        self.assertEqual(self.actual33, label)

    def test_labelButterChicken(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.ButterChicken, 'innerHTML')
        print(label)
        self.assertEqual(self.actual34, label)

    def test_labelMistress(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Mistress, 'innerHTML')
        print(label)
        self.assertEqual(self.actual35, label)


    # def test_labelSauces(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.sauces, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual5, label)

    # def test_labelMealKit(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.mealKit, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual5, label)
    #
    # def test_labelEffortless(self):
    #     self.sauces_page.click_NationWide()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.effortless, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual6, label)
    #
    # def test_labelStep1(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step1, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual7, label)
    #
    # def test_labelStep2(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step2, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual8, label)
    #
    # def test_labelStep3(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step3, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual9, label)
    #
    # def test_labelStep4(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step4, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual10, label)
    #
    # def test_labelFridge(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.fromFridge, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual11, label)
    #
    # def test_labelSetPan(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.setPan, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual12, label)
    #
    # def test_labelRelax(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.relax, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual13, label)
    #
    # def test_labelEnjoy(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.enjoy, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual14, label)
    #
    # def test_labelPhilosophy(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.OurFoodPhilosophy, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual15, label)
    #
    # def test_labelDelivery(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.delivery, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual16, label)
    #
    # def test_labelNationWide(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.nationwide, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual17, label)
    #
    # def test_labelBayArea(self):
    #     self.sauces_page.click_backToPage()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.BayArea, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual18, label)

    # def test_clickbayArea(self):
    #     time.sleep(3)
    #     self.sauces_page.click_backToPage()
    #     self.sauces_page.click_BayArea()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > div.clsTiffinMenus > ul > li:nth-child(2) > a').value_of_css_property(
    #         'background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual19, hex)
    #
    # def test_clicknationWide(self):
    #     self.sauces_page.click_Bay()
    #     self.sauces_page.click_NationWide()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > div.clsTiffinMenus > ul > li.selected > a').value_of_css_property(
    #         'background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual19, hex)
    #
    # def test_clickselect(self):
    #     self.sauces_page.click_backToPage()
    #     self.sauces_page.click_select()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.mealKitLabel, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual20, label)
    #
    # def test_Addtocart(self):
    #     time.sleep(5)
    #     label1 = self.sauces_page.get_attribute(IndianMealKitAndSauces.Shopseeti, 'innerHTML')
    #     print(label1)
    #     self.assertEqual(self.actual28, label1)
    #     time.sleep(5)
    #     self.sauces_page.click_Shahi()
    #     self.sauces_page.click_Shahi()
    #     self.sauces_page.click_Chanamasala()
    #     self.sauces_page.click_Chickenpilafsauce()
    #     self.Payment()


    #def test_clickselect1(self):
    #    self.sauces_page.click_backToPage()
    #    self.sauces_page.click_select1()
    #    self.Payment()
    #    thankYou = self.sauces_page.get_attribute(IndianMealKitAndSauces.ThankYou, 'innerHTML')
    #    print(thankYou)
    #    self.assertEqual(self.actual27, thankYou)


    # def test_labelEatEverything(self):
    #     self.sauces_page.click_BayArea()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Eat, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual22, label)
    #
    # def test_labelVegetarian(self):
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.vegetarian, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual23, label)
    #
    # def test_labelNutFree(self):
    #     self.sauces_page.click_BayArea()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.NutFree, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual25, label)
    #
    # def test_clickeat(self):
    #     self.sauces_page.click_backToPage()
        # self.sauces_page.click_Eat()
        # label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual26, label)
    #
    # def test_clickvegetarian(self):
    #     self.sauces_page.click_Bay()
    #     self.sauces_page.click_BayArea()
    #     self.sauces_page.click_Vegetarian()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual26, label)
    #
    #def test_clickvegan(self):
    #    self.sauces_page.click_BayArea()
    #    self.sauces_page.click_Vegan()
    #    label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
    #    print(label)
    #    self.assertEqual(self.actual26, label)

    # def test_clicknut(self):
    #     self.sauces_page.click_BayArea()
    #     self.sauces_page.click_Nut()
    #     label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual26, label)


