import time
#from allure_commons.types import AttachmentType
from resources import ui_test_class
from resources.page_objects.bbq import BBQ
from resources.page_objects.bbq import BBQKIT
from selenium.webdriver.support.color import Color
#import allure

#@allure.severity(allure.severity_level.CRITICAL)
class TesINDIANBBQKIT(ui_test_class.UVXVXVIClass):
    bbq_page: BBQ
    bbq_page: BBQKIT

    actual1 = "Indian BBQ Kit"
    actual2 = "Chilling And Grilling"
    actual3 = "Search for products..."
    actual4 = "Grills menu"
    actual5 = "All Grills"
    actual6 = "Veg Grills"
    actual7 = "Non Veg Grills"
    actual8 = "Chicken Tikka Kebab BBQ Kit"
    actual9 = "Tandoori Veggie BBQ Kit "
    actual10 = "Reshmi Chicken BBQ Kit "
    actual11 = "Tandoori Aloo BBQ Kit "
    actual12 = "Hariyali Chicken BBQ Kit "
    actual13 = "Hariyali Paneer BBQ Kit "
    actual14 = "Paneer Tikka BBQ Kit "
    actual15 = "Tandoori Chicken BBQ Kit "
    actual16 = "Lamb Chops BBQ Kit "
    actual17 = "Boti Kabab BBQ Kit "
    actual18 = " Minimum Order Value: $10"
    actual19 = "#bb121a"
    actual20 = "$35$45"
    actual21 = "$49$65"
    actual22 = "Eat Everything"
    actual23 = "Vegetarian Meal Kit"
    actual24 = "Vegan Meal Kit"
    actual25 = "Nut Free Meal Kit"
    actual26 = "Bay Area"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANBBQKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANBBQKIT, cls).tearDownClass()
        cls.driver.quit()

    def Signin(self):
        self.bbq_page.select_dropdown()
        self.bbq_page.click_signin()
        self.bbq_page.EnterEmail("testaccount@quicklly.com")
        self.bbq_page.EnterPass("123456")
        self.bbq_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(5)

    def test_EnterZipCode(self):
        self.bbq_page.zip("60611")
        self.bbq_page.submit_zip()
        self.Signin()
        search = self.bbq_page.get_attribute(BBQ.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

#    @allure.severity(allure.severity_level.NORMAL)
    def test_clickIndian(self):
        time.sleep(10)
        # for i in range(10):
        #     time.sleep(2)
        #     self.bbq_page.click_RightArrow()

        self.bbq_page.click_MealKit()
        self.bbq_page.click_bbqKit()
        time.sleep(3)
        label = self.bbq_page.get_attribute(BBQ.bbqLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_labelChilling(self):
        label = self.bbq_page.get_attribute(BBQ.chilling, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelMenu(self):
        label = self.bbq_page.get_attribute(BBQ.menu, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelAllGrills(self):
        label = self.bbq_page.get_attribute(BBQ.AllGrills, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelVegGrills(self):
        label = self.bbq_page.get_attribute(BBQ.VegGrills, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelNonVegGrills(self):
        label = self.bbq_page.get_attribute(BBQ.NonVeg, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelReshmi(self):
        label = self.bbq_page.get_attribute(BBQ.reshmi, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_labelAloo(self):
        label = self.bbq_page.get_attribute(BBQ.Aloo, 'textContent')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelLamb(self):
        label = self.bbq_page.get_attribute(BBQ.Lamb, 'textContent')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_labelBotiKabaab(self):
        label = self.bbq_page.get_attribute(BBQ.BotiKabaab, 'textContent')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_clickallgrills(self):
        self.bbq_page.click_AllGrills()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(13) > div.divcustomtabpanels > ul > li.all.active').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_clickaveggrills(self):
        self.bbq_page.click_VegGrills()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(13) > div.divcustomtabpanels > ul > li.veg-grills').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        # self.assertEqual(self.actual19, hex)

    def test_clickanonVeggrills(self):
        self.bbq_page.click_NonVeg()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(13) > div.divcustomtabpanels > ul > li.non-veg-grills').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        # self.assertEqual(self.actual19, hex)

    def test_clicktandooriVeg(self):
        self.bbq_page.AddToCartVeggie()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clicktikkaKabeb(self):
        self.bbq_page.AddToCartTikka()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickreshmi(self):
        self.bbq_page.AddToCartReshmi()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickaLoo(self):
        self.bbq_page.AddToCartAloo()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickhariyaliChicken(self):
        self.bbq_page.AddToCartHariyaliChicken()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickhariyaliPaneer(self):
        self.bbq_page.AddToCartHariyaliPaneer()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickpaneerTikka(self):
        self.bbq_page.AddToCartPaneerTikka()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clicktandooriChicken(self):
        self.bbq_page.AddToCartTandooriChicken()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clicklamb(self):
        self.bbq_page.AddToCartLamb()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickboti(self):
        self.bbq_page.AddToCartBoti()
        self.bbq_page.click_MiniCart()
        label = self.bbq_page.get_attribute(BBQ.MinimumOrder, 'textContent')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickfive(self):
        self.bbq_page.click_five()
        label = self.bbq_page.get_attribute(BBQ.Price, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_clickten(self):
        self.bbq_page.click_eight()
        label = self.bbq_page.get_attribute(BBQ.Price, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_mpayment(self):
        time.sleep(2)
        self.bbq_page.click_MiniCart()
        self.bbq_page.click_Checkout()
        self.bbq_page.click_Checkout2()
        self.bbq_page.click_payment1()
        time.sleep(5)
        self.bbq_page.click_Pay()
        thankYou = self.bbq_page.get_attribute(BBQ.ThankYou, 'innerHTML')
        print(thankYou)
