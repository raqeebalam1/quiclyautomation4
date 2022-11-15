# import time
from resources import ui_test_class
from resources.page_objects.invalid import Invalid
from resources.page_objects.invalid import InvalidZipcodes


class TesIZ(ui_test_class.UVXVClass):
    invalid_page: Invalid
    invalid_page: InvalidZipcodes

    expected = "Please fill out this field."
    expected1 = "Please match the requested format."

    @classmethod
    def setUpClass(cls):
        super(TesIZ, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesIZ, cls).tearDownClass()
        cls.driver.quit()

    def test_EmptyZipcode(self):
        self.invalid_page.EnterZip("")
        self.invalid_page.submit_zip()
        alert = self.invalid_page.get_attribute(Invalid.enter_zip, 'validationMessage')
        print(alert)
        self.assertEqual(self.expected, alert)

    def test_ZipcodeLength(self):
        self.invalid_page.EnterZip("111")
        self.invalid_page.submit_zip()
        alert = self.invalid_page.get_attribute(Invalid.enter_zip, 'validationMessage')
        print(alert)
        self.assertEqual(self.expected1, alert)
