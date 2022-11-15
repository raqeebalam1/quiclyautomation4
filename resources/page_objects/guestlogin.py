import time
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.config_methods import DataClass
from resources.locators import GuestLogin
from resources.page_objects.base_page import BasePage


class LoginAsGuest(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterZip(self, zipcode):
        self.find_element(GuestLogin.enter_zip).clear()
        self.find_element(GuestLogin.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(GuestLogin.submit_zip)

    def click_food(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[3]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MakkiFood(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addTenders(self):
        self.scroll_to_element(GuestLogin.AddTenders)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartTenders(self):
        self.click(GuestLogin.TendersAddToCart)

    def click_submitTenders(self):
        self.click(GuestLogin.submitTenders)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        # self.click(Department.proceed_to_checkOut)
        element = self.driver.find_element_by_id('lnkProceedToCheckout')
        self.driver.execute_script("arguments[0].click();", element)

    def click_guestLogin(self):
        self.click(GuestLogin.guest)

    def Enter_Name(self, fname):
        self.find_element(GuestLogin.Fname).clear()
        self.find_element(GuestLogin.Fname).send_keys(fname)

    def Enter_Name2(self, lname):
        self.find_element(GuestLogin.Lname).clear()
        self.find_element(GuestLogin.Lname).send_keys(lname)

    def EnterAddress(self, add):
        self.find_element(GuestLogin.Address).clear()
        self.find_element(GuestLogin.Address).send_keys(add)
        time.sleep(5)
        self.find_element(GuestLogin.Address).send_keys(K.ARROW_DOWN)
        self.find_element(GuestLogin.Address).send_keys(K.ENTER)

    def EnterNumber(self, num):
        self.find_element(GuestLogin.number).clear()
        self.find_element(GuestLogin.number).send_keys(num)

    def Enter_email(self, mail):
        self.find_element(GuestLogin.email).clear()
        self.find_element(GuestLogin.email).send_keys(mail)

    def click_submit(self):
        self.click(GuestLogin.submit)

    def click_payment1(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(GuestLogin.Pay)

    def EnterCardNumber(self, card):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.driver.find_element_by_css_selector('#braintree-dropin-frame')))
        self.find_element(GuestLogin.cardNumber).send_keys(card)

    def EnterExpirationDate(self, expiry):
        self.find_element(GuestLogin.expirationDate).send_keys(expiry)

    def EnterCVV(self, cvv):
        self.find_element(GuestLogin.CVV).send_keys(cvv)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('/html/body/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_LeftArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/i[1]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Catering(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[14]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Hyderabad(self):
        element = self.driver.find_element_by_xpath('//*[@id="Catering"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBeef(self):
        self.scroll_to_element(GuestLogin.AddBeefFry)
        element = self.driver.find_element_by_css_selector('#searchhide > div.clsFoodStore > div > div > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBeef(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(GuestLogin.AddToCartBeef)).click()

    def click_Delivery(self):
        self.click(GuestLogin.delivery)

    def click_timeOfDelivery(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(GuestLogin.timeDelivery)).click()

    def Submit_Beef(self):
        self.click(GuestLogin.submitBeef)

    def click_Tiffin(self):
        self.click(GuestLogin.TiffinServices)

    def click_Chicago(self):
        element = self.driver.find_element_by_css_selector('#tiffin-services > div > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_VegThali(self):
        element = self.driver.find_element_by_xpath('//*[@id="TiffinServices"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartVT(self):
        self.click(GuestLogin.AddToCartVegThali)

    def submitVT(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(GuestLogin.submitVT)).click()
