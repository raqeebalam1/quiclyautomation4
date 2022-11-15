import time
from resources import ui_test_class
from resources.page_objects.edit_page import EDITITEM
from resources.page_objects.edit_page import Edit


class TesEDITITEM(ui_test_class.UVXVXVVIIClass):
    edit_page: Edit
    edit_page: EDITITEM

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "Indian Sweets & Snacks"
    text = ""
    actual5 = "Rajbhog Diwali Party Pack  "

    @classmethod
    def setUpClass(cls):
        super(TesEDITITEM, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesEDITITEM, cls).tearDownClass()
        cls.driver.quit()

    def edit(self):
        time.sleep(5)
        for i in range(10):
            time.sleep(3)
            self.edit_page.click_RightArrow()
        self.edit_page.click_NationWideShop()
        self.edit_page.click_indianSweet()
        # time.sleep(3)
        # search = self.edit_page.get_attribute(Edit.SearchForProducts1, 'placeholder')
        # print(search)
        # self.assertEqual(self.actual3, search)
        self.edit_page.click_Monthly()
        self.edit_page.click_buildABox()
        self.edit_page.click_addPistaGhari()
        self.edit_page.click_plusPistaGhari()
        time.sleep(5)
        self.edit_page.click_deleteItem()


    def test_EnterZipCode(self):
        self.edit_page.zip("60611")
        self.edit_page.submit_zip()
        search = self.edit_page.get_attribute(Edit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.edit_page.select_dropdown()
        self.edit_page.click_signin()
        self.edit_page.EnterEmail("testaccount@quicklly.com")
        self.edit_page.EnterPass("123456")
        self.edit_page.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        time.sleep(2)
        self.edit_page.select_dropdown()

    def test_labelRajbogh(self):
        label = self.edit_page.get_attribute(Edit.Rajbogh, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_editItem(self):
        time.sleep(3)
        self.edit()
