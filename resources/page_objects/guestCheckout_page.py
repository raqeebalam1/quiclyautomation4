import time
from resources.config_methods import DataClass
from resources.locators import GuestCheckout
from resources.page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys as K


class CheckoutWithGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def enterZip(self, zip):
        self.find_element(GuestCheckout.enter_zip).clear()
        self.find_element(GuestCheckout.enter_zip).send_keys(zip)

    def click_Fresh(self):
        self.click(GuestCheckout.goFresh)

    def click_Potato(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[11]/div/section[2]/div/a[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Cart(self):
        self.click(GuestCheckout.Cart)

    def click_Checkout(self):
        self.click(GuestCheckout.checkout)

    def click_guestLogin(self):
        element = self.driver.find_element_by_id('gustusrlogin')
        self.driver.execute_script("arguments[0].click();", element)

    def Enter_Name(self, fname):
        self.find_element(GuestCheckout.Fname).clear()
        self.find_element(GuestCheckout.Fname).send_keys(fname)

    def Enter_Name2(self, lname):
        self.find_element(GuestCheckout.Lname).clear()
        self.find_element(GuestCheckout.Lname).send_keys(lname)

    def EnterAddress(self, add):
        self.find_element(GuestCheckout.Address).clear()
        self.find_element(GuestCheckout.Address).send_keys(add)
        time.sleep(5)
        self.find_element(GuestCheckout.Address).send_keys(K.ARROW_DOWN)
        self.find_element(GuestCheckout.Address).send_keys(K.ENTER)

    def EnterNumber(self, num):
        self.find_element(GuestCheckout.number).clear()
        self.find_element(GuestCheckout.number).send_keys(num)

    def Enter_email(self, mail):
        self.find_element(GuestCheckout.email).clear()
        self.find_element(GuestCheckout.email).send_keys(mail)

    def click_submit(self):
        self.click(GuestCheckout.submit)

    def click_SubmitZip(self):
        self.click(GuestCheckout.submit_zip)

    def click_checkout2(self):
        self.click(GuestCheckout.checkout2)

    def EnterElementForSearch(self, element):
        self.find_element(GuestCheckout.searchBox).clear()
        self.find_element(GuestCheckout.searchBox).send_keys(element)

    def click_SearchButton(self):
        self.click(GuestCheckout.searchButton)



