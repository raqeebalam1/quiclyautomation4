from resources.config_methods import DataClass
from resources.locators import IndianMealKitAndSauces
from resources.page_objects.base_page import BasePage


class Sauces(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianMealKitAndSauces.enter_zip).clear()
        self.find_element(IndianMealKitAndSauces.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianMealKitAndSauces.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[1]/div/div/i[2]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]//img[@alt="Order Indian Meal Kit"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Oragnicsauces(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="Organic Meal Kits and Sauces by Seeti"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BayArea(self):
        self.click(IndianMealKitAndSauces.BayArea)

    def click_NationWide(self):
        self.click(IndianMealKitAndSauces.nationwide)

    def click_select(self):
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_select1(self):
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_backToPage(self):
        self.click(IndianMealKitAndSauces.backToPage)

    def click_Eat(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vegetarian(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vegan(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Nut(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bay(self):
        self.click(IndianMealKitAndSauces.clickBay)

    def click_Shahi(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div[2]/div/div[2]/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartShai(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div/div[2]/div[2]/a[2]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Chanamasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div[2]/div/div[6]/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Palakpanersauce(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div[2]/div/div[10]/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(IndianMealKitAndSauces.Email).clear()
        self.find_element(IndianMealKitAndSauces.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(IndianMealKitAndSauces.Pass).clear()
        self.find_element(IndianMealKitAndSauces.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(IndianMealKitAndSauces.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "proceedtopayment"]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Pay(self):
        self.click(IndianMealKitAndSauces.Pay)

    def click_quicklly(self):
        self.click(IndianMealKitAndSauces.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Sauces(self):
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)
