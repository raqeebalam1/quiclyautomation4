from resources.config_methods import DataClass
from resources.locators import BiWeekly
from resources.page_objects.base_page import BasePage


class BIWEEKLY(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(BiWeekly.enter_zip).clear()
        self.find_element(BiWeekly.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(BiWeekly.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[5]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addPistaGhari(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_plusPistaGhari(self):
        element = self.driver.find_element_by_css_selector(
            '#load_data > div > div:nth-child(5) > p > a > span.plusQty.plusQty195540')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addToCartPistaGhari(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="v-bar-fixed"]/div[2]/button[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Cart(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(BiWeekly.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(BiWeekly.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(BiWeekly.Email).clear()
        self.find_element(BiWeekly.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(BiWeekly.Pass).clear()
        self.find_element(BiWeekly.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Laumire(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "selctProductStore"] / option[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SelectDate(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "ddlDeliveryDateChange"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SelectDate1(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "ddlDeliveryDateChange"] / option[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChangeSlot(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "dvDialog-Slot-DateTime"] / div / div / div[3] / a[1]')
        self.driver.execute_script("arguments[0].click();", element)




    def click_biweekly(self):
        self.click(BiWeekly.BiWeekly)
