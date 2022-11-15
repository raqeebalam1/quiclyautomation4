from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.config_methods import DataClass
from resources.locators import Coupon
from resources.page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys as K


class evoucher(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterZipcode(self, zip):
        self.find_element(Coupon.zipCode).clear()
        self.find_element(Coupon.zipCode).send_keys(zip)

    def ClickSubmit(self):
        element = self.driver.find_element_by_xpath('//*[@id="zipsubmitbtn"]')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        self.scroll_to_element(Coupon.SignInButton)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Coupon.SignInButton)).click()

    def EnterEmail(self, email):
        self.find_elements(Coupon.Email).clear()
        self.find_element(Coupon.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Coupon.Pass).clear()
        self.find_element(Coupon.Pass).send_keys(password)

    def click_login(self):
        self.click(Coupon.LoginButton)

    def click_additem(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div/div/div[1]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Grocery(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[13]/div[1]/div/div/a[2]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddItem1(self):
        self.click(Coupon.additem2)

    def click_additem2(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div/div/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem3(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div/div/div[4]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem4(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div/div/div[1]/div/a')
        self.driver.execute_script("arguments[0].click();", element)





    def click_Plusitem(self):
        self.scroll_to_element(Coupon.additem)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[11]/div/section[2]/div/span/select')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        self.scroll_to_element(Coupon.click_cart)
        self.click(Coupon.click_cart)

    def click_Checkout(self):
        self.click(Coupon.proceed_to_checkOut)

    def EnterEvoucher(self, eVoucher):
        self.find_elements(Coupon.evoucher_text_box).clear()
        self.find_element(Coupon.evoucher_text_box).send_keys(eVoucher)

    def EnterEvoucher1(self, eVoucher):
        self.find_elements(Coupon.evoucher_text_box).clear()
        self.find_element(Coupon.evoucher_text_box).send_keys(eVoucher)
        self.find_element(Coupon.evoucher_text_box).send_keys(K.CONTROL, 'a')
        self.find_element(Coupon.evoucher_text_box).send_keys(K.CONTROL, 'x')
        self.find_element(Coupon.evoucher_text_box).send_keys(K.CONTROL, 'v')


    def click_apply(self):
        element = self.driver.find_element_by_xpath('//*[@id="parRadioOne"]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_grocery(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[12]/div[1]/div/div/a[3]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_item(self):
        self.scroll_to_element(Coupon.item1)
        self.click(Coupon.item1)

    def click_Additem2(self):
        self.click(Coupon.addToCart)

    def click_Checkout2(self):
        self.click(Coupon.checkout2)

    def zip(self, zipcode):
        self.find_elements(evoucher.enter_zip).clear()
        self.find_element(evoucher.enter_zip).send_keys(zipcode)
