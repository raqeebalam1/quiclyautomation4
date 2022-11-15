# import time
from selenium.webdriver.support.wait import WebDriverWait

from resources import ui_test_class
from resources.page_objects.link import Links
from resources.page_objects.link import ContactUsLinks


class TesLINKS(ui_test_class.UVXIVClass):
    link_page: Links
    link_page: ContactUsLinks

    expected = "Facebook"
    expected1 = "https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png"
    expected2 = "Join LinkedIn"
    expected3 = "Tweets"
    expected4 = "None"
    expected5 = "https://i.pinimg.com/originals/98/96/4b/98964b8ab629eb3c8f3773c2d3d59291.jpg"

    @classmethod
    def setUpClass(cls):
        super(TesLINKS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesLINKS, cls).tearDownClass()
        cls.driver.quit()

    def test_facebookLink(self):
        self.link_page.click_Facebook()
        self.driver.get("https://www.facebook.com/quickllyfoodandgroceries/")
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))
        label = self.link_page.get_attribute(Links.fbLabel, 'innerHTML')
        self.driver.get("https://www.quicklly.com/")
        self.assertEqual(label, self.expected)

    def test_twitterLink(self):
        self.link_page.click_twitter()
        self.driver.get("https://twitter.com/QuickllyIt")
        label1 = self.link_page.get_attribute(Links.tweetLabel, 'textContent')
        self.driver.get("https://www.quicklly.com/")
        self.assertEqual(label1, self.expected3)

    def test_linkedinLink(self):
        self.link_page.click_linkedin()
        self.driver.get("https://in.linkedin.com/company/myvalue365-e-commerce-pvt-ltd-")
        label2 = self.link_page.get_attribute(Links.linkedinLabel, 'innerHTML')
        label2.strip()
        print(label2)
        self.driver.get("https://www.quicklly.com/")
        self.assertEqual(label2, self.expected2)

    def test_instagramLink(self):
        self.link_page.click_instagramLink()
        self.driver.get("https://www.instagram.com/quickllyit/")
        label4 = self.link_page.get_attribute(Links.instagramSRC, 'src')
        self.driver.get("https://www.quicklly.com/")
        self.assertEqual(label4, self.expected1)

    def test_pinterestLink(self):
        self.link_page.click_pinterest()
        self.driver.get("https://in.pinterest.com/QuickllyIt/")
        label5 = self.link_page.get_attribute(Links.pinterestLabel, 'src')
        print(label5)
        self.driver.get("https://www.quicklly.com/")
        self.assertEqual(label5, self.expected5)
