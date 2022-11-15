from resources.config_methods import DataClass
from resources.locators import Edit
from resources.page_objects.base_page import BasePage


class EDITITEM(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Edit.enter_zip).clear()
        self.find_element(Edit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Edit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_NationWideShop1(self):
        element = self.driver.find_element_by_css_selector('# searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > div > div > a:nth-child(8) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "home"] / div / div[5] / div / a / div / div / h3')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_monthly(self):
        self.click(Edit.Monthly)

    def click_addPistaGhari(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_plusPistaGhari(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[1]/div[4]/p/a/span[3]')
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
        self.click(Edit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Edit.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Edit.Email).clear()
        self.find_element(Edit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Edit.Pass).clear()
        self.find_element(Edit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_deleteItem(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div/div[4]/p/a/span[1]')
        self.driver.execute_script("arguments[0].click();", element)

