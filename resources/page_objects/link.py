from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.config_methods import DataClass
from resources.locators import Links
from resources.page_objects.base_page import BasePage



class ContactUsLinks(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_Facebook(self):
        # element = self.driver.find_element_by_link_text('FACEBOOK')
        element = self.driver.find_element_by_xpath('/ html / body / footer / div / section[2] / ul / li[1] / a')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Links.fbLabel))

    def click_twitter(self):
        # element = self.driver.find_element_by_link_text('TWITTER')
        element = self.driver.find_element_by_xpath('/html/body/footer/div/section[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_linkedin(self):
        # element = self.driver.find_element_by_link_text('LINKEDIN')
        element = self.driver.find_element_by_xpath('/html/body/footer/div/section[2]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_youtubeLink(self):
        element = self.driver.find_element_by_link_text('YOUTUBE')
        self.driver.execute_script("arguments[0].click();", element)

    def click_instagramLink(self):
        # element = self.driver.find_element_by_link_text('INSTAGRAM')
        element = self.driver.find_element_by_xpath('/ html / body / footer / div / section[2] / ul / li[6] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_pinterest(self):
        # element = self.driver.find_element_by_link_text('PINTEREST')
        element = self.driver.find_element_by_xpath('/html/body/footer/div/section[2]/ul/li[8]/a')
        self.driver.execute_script("arguments[0].click();", element)
