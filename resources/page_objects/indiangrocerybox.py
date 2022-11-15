from resources.config_methods import DataClass
from resources.locators import IndianGroceryBox
from resources.page_objects.base_page import BasePage


class IndianGrocery(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianGroceryBox.enter_zip).clear()
        self.find_element(IndianGroceryBox.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianGroceryBox.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(13) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianGrocery(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="Customize Organic Indian Grocery Box"]')
        # self.scroll_to_element(IndianGroceryBox.indianGrocery)
        # element = self.driver.find_element_by_css_selector('#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > div > div > a:nth-child(13) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "searchhide"] / section[1] / div / div / div[2] / div[2] / ul / li[2] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OIG(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(IndianGroceryBox.Email).clear()
        self.find_element(IndianGroceryBox.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(IndianGroceryBox.Pass).clear()
        self.find_element(IndianGroceryBox.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(IndianGroceryBox.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(IndianGroceryBox.Pay)

    def click_quicklly(self):
        self.click(IndianGroceryBox.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddRagi(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddWholemillets(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "searchhide"] / div[2] / div[3] / div / div[3] / div[3] / div[1] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBajra(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "searchhide"] / div[2] / div[3] / div / div[4] / div[3] / div[1] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBajra1(self):
        element = self.driver.find_element_by_css_selector(
            '   # searchhide > div.clsFoodStores.clsMealSelect.clsPgWidth > div.tabcontents.clsWeeklyTabs.grillproductlistpage > div > div.clsFoodStoreCard.include-calculation.productcatBox.prodcust134190.catdetail4670 > div:nth-child(4) > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ProceedtoCheckout(self):
        self.click(IndianGroceryBox.ProceedtoCheckout)

    def click_OrganicIndianGrocery(self):
        element = self.driver.find_element_by_xpath('  // *[ @ id = "searchhide"] / div[1] / div / ul / li[3] / a')
        self.driver.execute_script("arguments[0].click();", element)