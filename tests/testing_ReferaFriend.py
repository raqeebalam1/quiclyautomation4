import time
from resources import ui_test_class
from resources.locators import Refer
from resources.page_objects.refer import ReferAFriend


class TesREFERAFRIEND(ui_test_class.UVXIClass):
    refer_page: Refer
    refer_page: ReferAFriend

    @classmethod
    def setUpClass(cls):
        super(TesREFERAFRIEND, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesREFERAFRIEND, cls).tearDownClass()
        cls.driver.quit()

    def test_clickRefer(self):
        self.refer_page.click_refer()
        self.refer_page.click_referLink()
        # time.sleep(30)

    def test_clickfacebook(self):
        time.sleep(10)
        self.refer_page.click_facebook()
        self.refer_page.click_facebookLink()
        time.sleep(10)

    def test_clickTwitter(self):
        self.refer_page.click_twitter()
        self.refer_page.click_twitterLink()
