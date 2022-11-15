from resources.config_methods import DataClass
from resources.locators import RotiKit
from resources.page_objects.base_page import BasePage


class RotiBox(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(RotiKit.enter_zip).clear()
        self.find_element(RotiKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(RotiKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[9]/div/div/div/div/a[13]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="Rotikaa Foods"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(RotiKit.BiWeekly)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_WholeWheat(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[1]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_roti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[2]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_multiGrain(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[3]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotla(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[4]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Paratha(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[5]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SpecialRoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[6]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bakhri(self):
        element = self.driver.find_element_by_css_selector('#searchhide > section.clsFoodStores.organicproductsection.rotikalandingpage.clsPgWidth > div.tabcontents > div > div:nth-child(7) > a > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OrderRotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[9]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddWheatBakhri(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            '  // *[ @ id = "load_data"] / div[6] / div[4] / a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_PlusMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            '   // *[ @ id = "load_data"] / div[6] / div[4] / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MinusMasalaParatha(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="load_data"]/div[6]/div[4]/p/a/span[1]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_DetailsCornRoti(self):
        element = self.driver.find_element_by_xpath(
             '//*[@id="load_data"]/div[12]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CancelDetailsCornRoti(self):
        element = self.driver.find_element_by_xpath(
             '//*[@id="dvDialog-Custom"]/div/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_AddRoti(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_plusRoti(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="v-bar-fixed"]/div[2]/button[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(RotiKit.Email).clear()
        self.find_element(RotiKit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(RotiKit.Pass).clear()
        self.find_element(RotiKit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(RotiKit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ProceedtoCheckout(self):
        self.click(RotiKit.ProceedtoCheckout)

    def click_Pay(self):
        self.click(RotiKit.Pay)

    def click_quicklly(self):
        self.click(RotiKit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)
