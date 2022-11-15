import time
from resources import ui_test_class
from resources.page_objects.chaiDepartment import ChaiAndCoffee
from resources.page_objects.chaiDepartment import CACD
from selenium.webdriver.support.color import Color


class TesCHAIDEPARTMENT(ui_test_class.UVXVIXClass):
    chai_page: CACD
    chai_page: ChaiAndCoffee

    actual1 = "Chai Tea & Coffee Kit"
    actual2 = "Weekly"
    actual3 = "Search for products..."
    actual4 = "#333333"
    actual5 = " Indian Chai & Coffee"
    actual6 = "Kimbala Chai & Coffee Subscription"
    actual7 = "Our Collection"
    actual8 = " Chai Assamica "
    actual9 = " Coffee a la Jaggery "
    actual10 = " Coffee Neat "
    actual11 = " Chai Concentrate "
    actual12 = " Dirty Chai Concentrate "
    actual13 = "Ready-to-Drink Chai"
    actual14 = "Ready-to-Drink Coffee"
    actual15 = "Kimbala Intro 6 Pack"
    actual16 = "Thank you"
    actual17 = " Minimum Order Value: $30"
    actual18 = "Kimbala Mixed RTD Pack"
    actual19 = "Kimbala Dirty Chai Concentrate 12 Pack"
    actual20 = "Kimbala Chai Concentrate 12 Pack"
    actual21 = "Kimbala Intro 12 Pack"
    actual22 = "Kimbala RTD Coffee Jaggery"
    actual23 = "Kimbala Mixed RTD Pack"


    @classmethod
    def setUpClass(cls):
        super(TesCHAIDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCHAIDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.chai_page.click_quicklly()
    #     time.sleep(3)
    #     self.chai_page.zip("60611")
    #     self.chai_page.submit_zip()
    #     time.sleep(5)
    #     for i in range(12):
    #         time.sleep(1)
    #         self.chai_page.click_RightArrow()
    #     self.chai_page.click_ChaiAndCoffee()

    # def Payment(self):
    #     self.chai_page.click_buildABox()
    #     time.sleep(3)
    #     self.chai_page.click_AddKimbala()
    #     self.chai_page.click_MiniCart()
    #     self.chai_page.click_Checkout()
    #     self.chai_page.click_Checkout2()
    #     self.chai_page.click_payment1()
    #     time.sleep(5)
    #     self.chai_page.click_Pay()
    #

    def test_EnterZipCode(self):
        self.chai_page.zip("60611")
        self.chai_page.submit_zip()
        time.sleep(2)
        self.test_Signin()
        time.sleep(5)
        search = self.chai_page.get_attribute(ChaiAndCoffee.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_Signin(self):
        self.chai_page.select_dropdown()
        self.chai_page.click_signin()
        self.chai_page.EnterEmail("testaccount@quicklly.com")
        self.chai_page.EnterPass("123456")
        self.chai_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)


    def test_clickChaiDepartment(self):
        time.sleep(5)
        for i in range(5):
         time.sleep(2)
         self.chai_page.click_LeftArrow()
         time.sleep(3)
        # self.chai_page.click_MealKit()
        # time.sleep(3)
        self.chai_page.click_ChaiAndCoffee()
        headingLabel = self.chai_page.get_attribute(ChaiAndCoffee.heading1, 'textContent')
        print(headingLabel)
        self.assertEqual(self.actual1, headingLabel)


    # def test_clickbuildABox(self):
    #     self.chai_page.click_buildABox()
    #     indianLabel = self.chai_page.get_attribute(ChaiAndCoffee.indianChaiLabel, 'textContent')
    #     print(indianLabel)
    #     self.assertEqual(self.actual5, indianLabel)
    #
    # def test_subscriptionLabel(self):
    #     Slabel = self.chai_page.get_attribute(ChaiAndCoffee.subscription, 'textContent')
    #     print(Slabel)
    #     self.assertEqual(self.actual6, Slabel)
    #
    # def test_ourCollection(self):
    #     time.sleep(2)
    #     self.BackToPage()
        # Label = self.chai_page.get_attribute(ChaiAndCoffee.collection, 'innerHTML')
        # print(Label)
        # self.assertEqual(self.actual7, Label)
    #
    def test_labelchaiAssamica(self):
        Label = self.chai_page.get_attribute(ChaiAndCoffee.ChaiAssamica, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual8, Label)

    def test_labelcoffeeJaggery(self):
        time.sleep(5)
        Label = self.chai_page.get_attribute(ChaiAndCoffee.CoffeeJaggery, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual9, Label)

    def test_labelcoffeeNeat(self):
        time.sleep(5)
        Label = self.chai_page.get_attribute(ChaiAndCoffee.coffeeNeat, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual10, Label)

    def test_labelchaiConcentrate(self):
        time.sleep(5)
        Label = self.chai_page.get_attribute(ChaiAndCoffee.ChaiConcentrate, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual11, Label)

    def test_labeldirtyChai(self):
        time.sleep(5)
        Label = self.chai_page.get_attribute(ChaiAndCoffee.DirtyChai, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual12, Label)

    def test_labelkimbala(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutKimbala, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelRTD(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutRTD, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_labelDirty(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutDirty, 'textContent')
        print(label)
        self.assertEqual(self.actual19, label)

    def test_labelConcrete(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutConcrete, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_labelkimbala2(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutKimbala2, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelRTD2(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutRTD2, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelRTD3(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutRTD3, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)

    # def test_readyToDrinkChai(self):
    #     label = self.chai_page.get_attribute(ChaiAndCoffee.readyChai, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual13, label)
    #
    # def test_readyToDrinkCoffee(self):
    #     label = self.chai_page.get_attribute(ChaiAndCoffee.readyCoffee, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual14, label)
    #
    # def test_Allchai(self):
    #     self.chai_page.click_Allchai()
    #
    # def test_AddChaikimbala(self):
    #     self.chai_page.click_AddKimbala()
    #     self.chai_page.click_Pluskimbala()
    #     self.chai_page.click_MiniCart()
    #     label = self.chai_page.get_attribute(ChaiAndCoffee.MinimumOrder, 'textContent')
    #     print(label)
    #     self.assertEqual(self.actual17, label)

    # def test_mpayment(self):
    #     time.sleep(2)
    #     self.test_AddChaikimbala()
        # self.chai_page.click_MiniCart()
        # self.chai_page.click_Checkout()
        # self.chai_page.click_Checkout2()
        # self.chai_page.click_payment1()
        # time.sleep(5)
        # self.chai_page.click_Pay()
        # thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
        # print(thankYou)

    # def Chaiassamica(self):
    #    self.test_labelchaiAssamica()
        # self.chai_page.click_Chaiassamica()
        # self.chai_page.click_Addchaiassmica()
        # self.chai_page.click_Pluschaiassmica()
        # self.chai_page.click_MiniCart()
        #  self.chai_page.click_Checkout2()
        #  self.chai_page.click_payment1()
        #  self.chai_page.click_Pay()
    #
    # def test_Chaiassamica(self):
    #     time.sleep(3)
    #     self.Chaiassamica()
    #

    # def test_weekly(self):
    #     time.sleep(2)
    #     self.chai_page.click_ChaiTeaKit()
    #     self.chai_page.click_weekly()
    #     time.sleep(2)
    #     self.Payment()
    #     thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual16, thankYou)
    #
    # def test_monthly(self):
    #     time.sleep(2)
    #     self.BactToPage()
    #     self.chai_page.click_Monthly()
    #     self.Payment()
    #     thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual16, thankYou)
    #
    def test_once(self):
        time.sleep(5)
        self.chai_page.click_buildABox1()
        time.sleep(10)
        indianLabel = self.chai_page.get_attribute(ChaiAndCoffee.indianChaiLabel, 'textContent')
        print(indianLabel)
        self.assertEqual(self.actual5, indianLabel)
        # Label = self.chai_page.get_attribute(ChaiAndCoffee.ChaiAssamica, 'innerHTML')
        # print(Label)
        # self.assertEqual(self.actual8, Label)
        time.sleep(5)
        self.chai_page.click_AddKimbala1()
        self.chai_page.click_Pluskimbala1()
        self.chai_page.click_Addchaiassmica1()
        self.chai_page.click_Pluschaiassmica1()
        # self.chai_page.click_DetailsChaiConcentrate()
        # self.chai_page.click_CloseDetailsChaiConcentrate()
        time.sleep(5)
        self.chai_page.click_MiniCart()
        self.chai_page.click_Checkout()
        self.chai_page.click_Checkout2()
        self.chai_page.click_payment1()
        # self.test_AddChaikimbala()
        # self.chai_page.click_ChaiTeaKit()
        # self.test_mpayment()
        # thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual16, thankYou)

    # def test_clickmeal20(self):
    #     time.sleep(3)
        # self.mealkit_page.click_Biweekly3()
        # self.mealkit_page.click_Monthly3()
        # self.mealkit_page.click_Once3()
        # self.chai_page.click_buildABox()
        # time.sleep(5)
        # label = self.chai_page.get_attribute(ChaiAndCoffee.indianChaiLabel, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual5, label)

    # def test_AddCart(self):
    #     time.sleep(5)
    #     self.chai_page.click_AddKimbala()
    #     self.chai_page.click_Pluskimbala()
    #     self.chai_page.click_Addchaiassmica()
    #     self.chai_page.click_Pluschaiassmica()
    #     self.chai_page.click_DetailsChaiConcentrate()
    #     self.chai_page.click_CloseDetailsChaiConcentrate()
        # self.chai_page.click_ChaiTeaKit()
        # self.mealkit_page.click_AddToCart()
        # self.Payment()

    # def Payment(self):
        # self.mealkit_page.click_selectProduct()
        # time.sleep(2)
        # self.mealkit_page.click_AddDaalChawal()
        # time.sleep(2)
        # for i in range(5):
        #     time.sleep(1)
        #     self.mealkit_page.plusDaalChawal()
        # self.mealkit_page.click_AddToCart()
        # time.sleep(2)
        # self.mealkit_page.click_MiniCart()
        # self.mealkit_page.click_Checkout()
        # time.sleep(5)
        # self.mealkit_page.click_ProceedtoCheckout()
        # time.sleep(5)
        # self.mealkit_page.click_CurryBox()
        # time.sleep(5)
        # self.mealkit_page.click_selectDate()
        # time.sleep(5)
        # self.mealkit_page.click_Date()
        # time.sleep(5)
        # self.mealkit_page.click_ChangeSlot()
        # time.sleep(2)
        # self.mealkit_page.click_MiniCart()
        # self.mealkit_page.click_Checkout()
        # self.mealkit_page.click_Checkout2()
        # time.sleep(5)
        # self.mealkit_page.click_payment1()
        # time.sleep(5)
        # self.mealkit_page.click_Pay()
        # time.sleep(3)
        # thankYou = self.mealkit_page.get_attribute(IndianMealKit.ThankYou, 'innerHTML')
        # print(thankYou)