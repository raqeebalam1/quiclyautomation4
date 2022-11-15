import time
from resources import ui_test_class
from resources.page_objects.mealkit import MealKit
from resources.page_objects.mealkit import Meal
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException


class TesMEALKIT(ui_test_class.UVXVXClass):
    meal_page: Meal
    meal_page: MealKit

    actual1 = "Meal Kit Stores"
    actual2 = "EXPLORE STORES"
    actual3 = "Search for products..."
    actual4 = "#ffffff"
    actual5 = "Indian Seasoning Kit"
    actual6 = "WHY CHOOSE OUR KITS"
    actual7 = "Authentic Indian Taste"
    actual8 = "Subscribe and Save"
    actual9 = "Free Shipping"
    actual10 = "Can't get enough of us!"
    actual11 = "Indian Grocery Delivery Chicago IL"
    actual12 = "Indian Food Delivery Chicago IL"
    actual13 = "Indian Catering Chicago IL"
    actual14 = "Chicago Tiffinwala"
    actual15 = "Indian Tiffin Chicago IL"
    actual16 = "Meal Kit Stores"
    actual17 = "Instant Pot Chicago IL"
    actual18 = "Recipes"
    actual19 = " Organic Indian Grocery"
    actual20 = "Chai Tea & Coffee Kit"
    actual21 = " Indian Meal Kit Subscription"

    label = ""
    label1 = ""
    label2 = ""

    @classmethod
    def setUpClass(cls):
        super(TesMEALKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesMEALKIT, cls).tearDownClass()
        cls.driver.quit()

    def home(self):
        self.meal_page.submit_zip()
        for i in range(4):
            time.sleep(1)
            self.meal_page.click_RightArrow()
        self.meal_page.click_MealKit()

    def test_EnterZipCode(self):
        self.meal_page.zip("60611")
        self.meal_page.submit_zip()
        search = self.meal_page.get_attribute(MealKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickMealKit(self):
        for i in range(9):
            time.sleep(1)
            self.meal_page.click_RightArrow()
        self.meal_page.click_MealKit()
        label = self.meal_page.get_attribute(MealKit.MealKitLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    # def test_clickBuildabox(self):


    def test_explore(self):
        label = self.meal_page.get_attribute(MealKit.Explore, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_popular(self):
        self.meal_page.click_popular()
        colorLabel = self.driver.find_element_by_css_selector('#profile-tab').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual4, hex)

    def test_new(self):
        self.meal_page.click_new()
        label = self.meal_page.get_attribute(MealKit.IndianSeasoningLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_whyChooseUs(self):
        label = self.meal_page.get_attribute(MealKit.whyChooseLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelAuthentic(self):
        elements = self.driver.find_elements_by_css_selector('#myTabContent > div.card-container.row.why-choose-us-box.slick-initialized.slick-slider > div > div')
        for element in elements:
            try:
                link = element.find_element_by_xpath('//*[@id="myTabContent"]/div[4]/div/div/div[1]/div/div/div/h3')
                self.label = link.get_attribute('innerHTML')
                print(self.label)
            except NoSuchElementException:
                print('No Data Available!')
        self.assertEqual(self.actual7, self.label)

    def test_subscribe(self):
        elements = self.driver.find_elements_by_css_selector(
            '#myTabContent > div.card-container.row.why-choose-us-box.slick-initialized.slick-slider > div > div')
        for element in elements:
            try:
                link = element.find_element_by_xpath('//*[@id="myTabContent"]/div[4]/div/div/div[2]/div/div/div/h3')
                self.label1 = link.get_attribute('innerHTML')
                print(self.label1)
            except NoSuchElementException:
                print('No Data Available!')
        self.assertEqual(self.actual8, self.label1)

    def test_freeShipping(self):
        elements = self.driver.find_elements_by_css_selector(
            '#myTabContent > div.card-container.row.why-choose-us-box.slick-initialized.slick-slider > div > div')
        for element in elements:
            try:
                link = element.find_element_by_xpath('//*[@id="myTabContent"]/div[4]/div/div/div[3]/div/div/div/h3')
                self.label2 = link.get_attribute('innerHTML')
                print(self.label2)
            except NoSuchElementException:
                print('No Data Available!')
        self.assertEqual(self.actual9, self.label2)

    def test_enough(self):
        self.meal_page.click_home()
        self.home()
        label = self.meal_page.get_attribute(MealKit.CantGetEnough, 'textContent')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_clickgroceries(self):
        self.meal_page.click_home()
        self.home()
        self.meal_page.click_grocery()
        label = self.meal_page.get_attribute(MealKit.indianGrocery, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_clickfood(self):
        self.meal_page.click_home1()
        self.home()
        self.meal_page.click_food()
        label = self.meal_page.get_attribute(MealKit.indianFood, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_clickcatering(self):
        self.meal_page.click_catering()
        label = self.meal_page.get_attribute(MealKit.indianCatering, 'innerHTML')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_clicktiffin(self):
        self.meal_page.click_home4()
        self.home()
        self.meal_page.click_tiffin()
        label = self.meal_page.get_attribute(MealKit.indianTiffin, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_clickmealKit(self):
        self.meal_page.click_home()
        self.home()
        self.meal_page.click_mealKit()
        label = self.meal_page.get_attribute(MealKit.mealStores, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_clickinstant(self):
        self.meal_page.click_home1()
        self.home()
        self.meal_page.click_instant()
        label = self.meal_page.get_attribute(MealKit.instantLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_clickrecipes(self):
        self.meal_page.click_home1()
        self.home()
        self.meal_page.click_recipes()
        label = self.meal_page.get_attribute(MealKit.recipesLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickorganic(self):
        self.meal_page.click_organic()
        label = self.meal_page.get_attribute(MealKit.organicLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual19, label)

    def test_clickchai(self):
        self.meal_page.click_home()
        self.home()
        self.meal_page.click_chai()
        label = self.meal_page.get_attribute(MealKit.chaiLabel, 'textContent')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_clickindianmeal(self):
        self.meal_page.click_home2()
        self.home()
        self.meal_page.click_indianMeal()
        label = self.meal_page.get_attribute(MealKit.indianMeal, 'textContent')
        print(label)
        self.assertEqual(self.actual21, label)
