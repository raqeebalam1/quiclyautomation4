import time
from resources import ui_test_class
from resources.page_objects.indiangrocerybox import IndianGrocery
from resources.page_objects.indiangrocerybox import IndianGroceryBox
from selenium.webdriver.support.color import Color


class TesINDIANGROCERY(ui_test_class.UVXVXIIClass):
    grocerybox_page: IndianGroceryBox
    grocerybox_page: IndianGrocery

    actual1 = "Organic Grocery Box Subscription"
    actual2 = "Organic Grocery Box Subscription"
    actual3 = "Search for products..."
    actual4 = "Shipping"
    actual5 = "Minimum Order"
    actual6 = "Free"
    actual7 = "$0.00"
    actual8 = "What we Deliver"
    actual9 = "Authentic Indian Products"
    actual10 = "Unbeatable Prices"
    actual11 = "Customized Grocery Box"
    actual12 = "How it works"
    actual13 = "1. Build your organic grocery box"
    actual14 = "2. Select products"
    actual15 = "3. Set your frequency"
    actual16 = "Order Customized Organic Grocery Box"
    actual17 = "#f9660d"
    actual18 = "Organic Products"
    actual19 = "Thank you"
    actual20 = "Flours"
    actual21 = "Millets"
    actual22 = "Pulses"
    actual23 = "Rice"
    actual24 = "Spices"
    actual25 = "Organic Finger Millet (Ragi)"
    actual26 = "Organic Finger Millet Flour (Ragi Atta)"
    actual27 = "Organic Foxtail Whole Millets"
    actual28 = "Organic Pearl Millet (Bajra)"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANGROCERY, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANGROCERY, cls).tearDownClass()
        cls.driver.quit()

    # def BactToPage(self):
    #     self.grocerybox_page.click_quicklly()
    #     time.sleep(5)
    #     self.grocerybox_page.zip("60611")
    #     self.grocerybox_page.submit_zip()
    #     time.sleep(8)
    #     for i in range(8):
    #         time.sleep(1)
    #         self.grocerybox_page.click_RightArrow()
    #     self.grocerybox_page.click_MealKit()
        # self.grocerybox_page.click_indianGrocery()

    def Payment(self):
        time.sleep(3)
        # self.grocerybox_page.click_buildABox()
        # self.grocerybox_page.click_AddRagi()
        # self.grocerybox_page.click_AddWholemillets()
        # self.grocerybox_page.click_AddToCart()
        # time.sleep(2)
        # self.grocerybox_page.click_OrganicIndianGrocery()
        # time.sleep(3)
        # self.test_clickweekly()
        # time.sleep(3)
        # self.test_clickbiweekly()
        # time.sleep(3)
        # self.test_clickmonthly()
        time.sleep(3)
        # self.grocerybox_page.click_OrganicIndianGrocery()
        self.grocerybox_page.click_MiniCart()
        self.grocerybox_page.click_Checkout()
        self.grocerybox_page.click_ProceedtoCheckout()
        time.sleep(3)
        self.grocerybox_page.click_payment1()
        time.sleep(5)
        self.grocerybox_page.click_Pay()
        time.sleep(3)
        thankYou = self.grocerybox_page.get_attribute(IndianGroceryBox.ThankYou, 'innerHTML')
        print(thankYou)
        self.assertEqual(self.actual19, thankYou)

    def Signin(self):
        self.grocerybox_page.select_dropdown()
        self.grocerybox_page.click_signin()
        self.grocerybox_page.EnterEmail("testaccount@quicklly.com")
        self.grocerybox_page.EnterPass("123456")
        self.grocerybox_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)

    def test_EnterZipCode(self):
        self.grocerybox_page.zip("60611")
        self.grocerybox_page.submit_zip()
        self.Signin()
        search = self.grocerybox_page.get_attribute(IndianGroceryBox.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        time.sleep(5)
        for i in range(7):
            time.sleep(1)
            self.grocerybox_page.click_RightArrow()
        #self.grocerybox_page.click_MealKit()
        self.grocerybox_page.click_indianGrocery()
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.indianGroceryLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelSubscription(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.subscription, 'textContent')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_labelFlours(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelFlour, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_labelMillets(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelMillets, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelPulses(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelPulses, 'textContent')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelRice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelRice, 'textContent')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelSpices(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelSpices, 'textContent')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelRaggi(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelRaggi, 'textContent')
        print(label)
        self.assertEqual(self.actual25, label)

    def test_labelAtta(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelAtta, 'textContent')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_labelMillets2(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelMillets2, 'textContent')
        print(label)
        self.assertEqual(self.actual27, label)

    def test_labelBajra(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.labelBajra, 'textContent')
        print(label)
        self.assertEqual(self.actual28, label)

    # def test_labelShipping(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.shipping, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual4, label)
    #
    # def test_labelMinimum(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.minimum, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual5, label)
    #
    # def test_labelFree(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.free, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual6, label)
    #
    # def test_labelPrice(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.cost, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual7, label)
    #
    # def test_labelWhatWeDeliver(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.whatwedeliver, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual8, label)
    #
    # def test_labelAuthentic(self):
    #     self.BactToPage()
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.Authentic, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual9, label)
    #
    # def test_labelUnbeatable(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.Unbeatable, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual10, label)
    #
    # def test_labelCustomized(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.customized, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual11, label)
    #
    # def test_labelHowItWorks(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.HowItWorks, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual12, label)
    #
    # def test_labelBuild(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.build, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual13, label)
    #
    # def test_labelSelectProducts(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.selectProducts, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual14, label)
    #
    # def test_labelSelectFrequency(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.frequency, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual15, label)
    #
    # def test_labelOrderCustomizedBox(self):
    #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.order, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual16, label)

    # def test_clickweekly(self):
    #     self.BactToPage()
        # self.grocerybox_page.click_quicklly()
        # time.sleep(5)
        # self.grocerybox_page.zip("60611")
        # self.grocerybox_page.submit_zip()
        # time.sleep(8)
        # for i in range(8):
        #     time.sleep(1)
        #     self.grocerybox_page.click_RightArrow()
        # self.grocerybox_page.click_indianGrocery()
        # self.test_clickIndian()
        # time.sleep(3)
        # self.grocerybox_page.click_buildABox()
        # label = self.grocerybox_page.get_attribute(IndianGroceryBox.organicProducts, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual18, label)
        # self.grocerybox_page.click_AddRagi()
        # self.grocerybox_page.click_AddWholemillets()
        # self.grocerybox_page.click_AddToCart()
        # self.grocerybox_page.click_OrganicIndianGrocery()
        # self.Payment()

    def test_clickbiweekly(self):
        time.sleep(3)
        # self.BactToPage()
        # self.grocerybox_page.click_quicklly()
        # time.sleep(5)
        # self.grocerybox_page.zip("60611")
        # self.grocerybox_page.submit_zip()
        # time.sleep(8)
        # for i in range(8):
        #     time.sleep(1)
        #     self.grocerybox_page.click_RightArrow()
        # self.grocerybox_page.click_indianGrocery()
        self.grocerybox_page.click_Biweekly()
        self.grocerybox_page.click_buildABox()
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.organicProducts, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)
        self.grocerybox_page.click_AddWholemillets()
        self.grocerybox_page.click_AddToCart()
        # self.grocerybox_page.click_OrganicIndianGrocery()
        # self.test_clickmonthly()
        time.sleep(5)
        # self.Payment()

    # def test_clickmonthly(self):
    #     time.sleep(3)
    #     self.BactToPage()
    #     self.grocerybox_page.click_quicklly()
        # time.sleep(5)
        # self.grocerybox_page.zip("60611")
        # self.grocerybox_page.submit_zip()
        # time.sleep(8)
        # for i in range(8):
        #     time.sleep(1)
        #     self.grocerybox_page.click_RightArrow()
        # self.grocerybox_page.click_indianGrocery()
        # self.test_clickweekly()
        # self.grocerybox_page.click_Monthly()
        # self.grocerybox_page.click_buildABox()
        # label = self.grocerybox_page.get_attribute(IndianGroceryBox.organicProducts, 'innerHTML')
        # print(label)
        # self.assertEqual(self.actual18, label)
        # self.grocerybox_page.click_AddBajra()
        # self.grocerybox_page.click_AddToCart()
        # self.grocerybox_page.click_OrganicIndianGrocery()
        # self.Payment()


    # def test_clickbiweekly(self):
    #     self.grocerybox_page.click_Biweekly()
    #     self.Payment()
    #     thankYou = self.grocerybox_page.get_attribute(IndianGroceryBox.ThankYou, 'innerHTML')
    #     print(thankYou)
    #     self.assertEqual(self.actual19, thankYou)
    #
    # def test_clickmonthly(self):
        # self.grocerybox_page.click_OIG()
        # self.BactToPage()
        # self.grocerybox_page.click_quicklly()
        # time.sleep(5)
        # self.grocerybox_page.zip("60611")
        # self.grocerybox_page.submit_zip()
        # time.sleep(8)
        # for i in range(8):
        #     time.sleep(1)
        #     self.grocerybox_page.click_RightArrow()
        # self.grocerybox_page.click_indianGrocery()
        # self.grocerybox_page.click_Monthly()
        # self.Payment()
        # thankYou = self.grocerybox_page.get_attribute(IndianGroceryBox.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual19, thankYou)
    #
    # def test_clickonce(self):
    #     self.BactToPage()
    #     self.grocerybox_page.click_quicklly()
        # time.sleep(5)
        # self.grocerybox_page.zip("60611")
        # self.grocerybox_page.submit_zip()
        # time.sleep(8)
        # for i in range(8):
        #     time.sleep(1)
        #     self.grocerybox_page.click_RightArrow()
        # self.grocerybox_page.click_indianGrocery()
        # self.grocerybox_page.click_Once()
        # self.Payment()
        # thankYou = self.grocerybox_page.get_attribute(IndianGroceryBox.ThankYou, 'innerHTML')
        # print(thankYou)
        # self.assertEqual(self.actual19, thankYou)

    # # def test_clickbuildABox(self):
    # #     time.sleep(2)
    # #     self.BactToPage()
    # #     time.sleep(3)
    # #     self.grocerybox_page.click_buildABox()
    # #     label = self.grocerybox_page.get_attribute(IndianGroceryBox.organicProducts, 'innerHTML')
    # #     print(label)
    # #     self.assertEqual(self.actual18, label)

