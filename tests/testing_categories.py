import time
from resources import ui_test_class
from resources.page_objects.category import Category
from resources.page_objects.category import GroceryCategories


class TesCATEGORIES(ui_test_class.UVXIIIClass):
    category_page: Category
    category_page: GroceryCategories

    expected = "Unbeatable Deals"
    expected1 = "Foods & Beverages"
    expected2 = "Go Fresh"
    expected3 = "Grocery"
    expected4 = "Household"
    expected5 = "Meat Products"
    expected6 = "Organic"
    expected7 = "Personal Care"
    actual3 = "Search for products..."

    @classmethod
    def setUpClass(cls):
        super(TesCATEGORIES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCATEGORIES, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipcode(self):
        self.category_page.EnterZip("60611")
        self.category_page.submit_zip()
        search = self.category_page.get_attribute(Category.SearchForProducts, 'placeholder')
        self.assertEqual(search, self.actual3)


    def test_udeals(self):
        time.sleep(2)
        self.category_page.click_unbeatable()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected)

    def test_fresh(self):
        time.sleep(5)
        self.category_page.click_GoFresh()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected2)

    def test_grocery(self):
        time.sleep(2)
        self.category_page.click_Grocery()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected3)

    def test_meat(self):
        time.sleep(2)
        self.category_page.click_Meat()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected5)

    def test_foodBeverages(self):
        time.sleep(2)
        self.category_page.click_Beverages()
        label = self.category_page.get_attribute(Category.StoreLabel, 'textContent')
        print(label)
        self.assertEqual(label, self.expected1)

    def test_organic(self):
        time.sleep(2)
        self.category_page.click_Organic()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected6)

    def test_personalCare(self):
        time.sleep(10)
        self.category_page.click_personalCare()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected7)

    def test_household(self):
        time.sleep(2)
        self.category_page.click_Household()
        label = self.category_page.get_attribute(Category.StoreLabel, 'innerHTML')
        print(label)
        self.assertEqual(label, self.expected4)
