from resources.config_methods import DataClass
from resources.locators import ChaiAndCoffee
from resources.page_objects.base_page import BasePage


class CACD(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(ChaiAndCoffee.enter_zip).clear()
        self.find_element(ChaiAndCoffee.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(ChaiAndCoffee.submit_zip)

    def click_ChaiAndCoffee(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[18]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_LeftArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/i[1]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]//img[@alt="Order Indian Meal Kit"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChaiTeaKit(self):
        element = self.driver.find_element_by_xpath('/ html / body / div[10] / ul / li[3] / a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_BiWeekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox1(self):
        element = self.driver.find_element_by_css_selector(
            ' # searchhide > section.productsection > div > div > div.organicproductcontent > div.divbuildbox > form > button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_backToPage(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddKimbala(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/div[3]/div/div/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pluskimbala(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/div[3]/div/div/div[1]/div[3]/div/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_AddKimbala1(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(5) > div:nth-child(16) > div > div > div.clsFoodStoreCard.include-calculation.productcatBox.prodcust138763.catdetail4732.parentcat4728 > div:nth-child(6) > div > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pluskimbala1(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(5) > div:nth-child(16) > div > div > div.clsFoodStoreCard.include-calculation.productcatBox.prodcust138763.catdetail4732.parentcat4728.active > div:nth-child(6) > div > p > a > span.plusQty.plusQty138763')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(ChaiAndCoffee.Email).clear()
        self.find_element(ChaiAndCoffee.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(ChaiAndCoffee.Pass).clear()
        self.find_element(ChaiAndCoffee.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    # def click_MiniCart(self):
    #     element = self.driver.find_element_by_xpath(
    #         '/html/body/header/div[4]/a')
    #     self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(ChaiAndCoffee.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(ChaiAndCoffee.Pay)

    def click_quicklly(self):
        self.click(ChaiAndCoffee.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Chaiassamica(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "searchhide"] / div[1] / div[2] / ul / div / div / li[2] / a / img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Addchaiassmica(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/div[3]/div/div/div[9]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pluschaiassmica(self):
         element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/div[3]/div/div/div[9]/div[3]/div/p/a/span[3]')
         self.driver.execute_script("arguments[0].click();", element)

    def click_Addchaiassmica1(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(5) > div:nth-child(16) > div > div > div.clsFoodStoreCard.include-calculation.productcatBox.prodcust138718.catdetail4729.parentcat4728 > div:nth-child(6) > div > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pluschaiassmica1(self):
         element = self.driver.find_element_by_css_selector(
            '#searchhide > div:nth-child(5) > div:nth-child(16) > div > div > div.clsFoodStoreCard.include-calculation.productcatBox.prodcust138718.catdetail4729.parentcat4728.active > div:nth-child(6) > div > p > a > span.plusQty.plusQty138718')
         self.driver.execute_script("arguments[0].click();", element)

    def click_DetailsChaiConcentrate(self):
        element = self.driver.find_element_by_xpath(
            ' //*[@id="searchhide"]/div[3]/div[3]/div/div/div[8]/div[1]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CloseDetailsChaiConcentrate(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="dvDialog-Custom"]/div/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Allchai(self):
         element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / div[1] / div[2] / ul / div / div / li[1] / a / img')
         self.driver.execute_script("arguments[0].click();", element)