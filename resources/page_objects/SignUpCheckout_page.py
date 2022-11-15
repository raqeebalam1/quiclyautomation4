import time
from resources.config_methods import DataClass
from resources.locators import SignUpCheckout
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys as K


class SUC(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_food(self):
        self.click(SignUpCheckout.food)

    def click_MakkiFood(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addTenders(self):
        self.scroll_to_element(SignUpCheckout.AddTenders)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartTenders(self):
        self.click(SignUpCheckout.TendersAddToCart)

    def click_submitTenders(self):
        self.click(SignUpCheckout.submitTenders)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        element = self.driver.find_element_by_id('lnkProceedToCheckout')
        self.driver.execute_script("arguments[0].click();", element)

    def click_needAccount(self):
        self.click(SignUpCheckout.needAccount)

    def firstName(self, fname):
        self.find_element(SignUpCheckout.firstName).clear()
        self.find_element(SignUpCheckout.firstName).send_keys(fname)

    def lastName(self, lname):
        self.find_element(SignUpCheckout.lastName).clear()
        self.find_element(SignUpCheckout.lastName).send_keys(lname)

    def Address(self, add):
        self.find_element(SignUpCheckout.Address).clear()
        self.find_element(SignUpCheckout.Address).send_keys(add)
        time.sleep(5)
        self.find_element(SignUpCheckout.Address).send_keys(K.ARROW_DOWN)
        self.find_element(SignUpCheckout.Address).send_keys(K.ENTER)

    def Phone(self, ph):
        self.find_element(SignUpCheckout.Phone).clear()
        self.find_element(SignUpCheckout.Phone).send_keys(ph)

    def emailAddress(self, email):
        self.find_element(SignUpCheckout.email).clear()
        self.find_element(SignUpCheckout.email).send_keys(email)

    def Password(self, password):
        self.find_element(SignUpCheckout.password).clear()
        self.find_element(SignUpCheckout.password).send_keys(password)

    def ConfirmPassword(self, cpass):
        self.find_element(SignUpCheckout.confirmpassword).clear()
        self.find_element(SignUpCheckout.confirmpassword).send_keys(cpass)

    def click_Register(self):
        self.click(SignUpCheckout.register)

    def click_payment1(self):
        self.scroll_to_element(SignUpCheckout.payment)
        # self.click(SignUpCheckout.payment)
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterElementForSearch(self, element):
        self.find_element(SignUpCheckout.searchBox).clear()
        self.find_element(SignUpCheckout.searchBox).send_keys(element)

    def click_SearchButton(self):
        self.click(SignUpCheckout.searchButton)

    def click_additem(self):
        self.scroll_to_element(SignUpCheckout.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ADDLG(self):
        self.click(SignUpCheckout.AddToCartLG)

    def click_addPotato(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_51875"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartPotato(self):
        self.click(SignUpCheckout.AddToCartP)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('/html/body/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def submit_zip(self):
        self.click(SignUpCheckout.submit_zip)

    def zip(self, zipcode):
        self.find_elements(SignUpCheckout.enter_zip).clear()
        self.find_element(SignUpCheckout.enter_zip).send_keys(zipcode)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_LeftArrow(self):
        self.click(SignUpCheckout.LeftArrow)

    def click_Catering(self):
        self.click(SignUpCheckout.Catering)

    def click_Hyderabad(self):
        element = self.driver.find_element_by_xpath('//*[@id="Catering"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBeef(self):
        self.scroll_to_element(SignUpCheckout.AddBeefFry)
        element = self.driver.find_element_by_css_selector('#searchhide > div.clsFoodStore > div > div > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBeef(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(SignUpCheckout.AddToCartBeef)).click()

        # self.click(SignUpCheckout.AddToCartBeef)

    def Submit_Beef(self):
        self.click(SignUpCheckout.submitBeef)

    def click_Delivery(self):
        self.click(SignUpCheckout.delivery)

    def click_timeOfDelivery(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(SignUpCheckout.timeDelivery)).click()

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tiffin(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(SignUpCheckout.TiffinServices)).click()

    def click_Chicago(self):
        element = self.driver.find_element_by_xpath('//*[@id="tiffin-services"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_VegThali(self):
        element = self.driver.find_element_by_xpath('//*[@id="TiffinServices"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartVT(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvDialog-Custom"]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def submitVT(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(SignUpCheckout.submitVT)).click()

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_IndianMealKit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="home"]/div/div[2]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SelectProducts(self):
        element = self.driver.find_element_by_xpath('//*[@id="meal-kit"]/div[2]/div[1]/form/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMixVegetable(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[1]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMisalPav(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[2]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusMixVegetable(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[1]/div[3]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartNW(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[2]/button')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterCardNumber(self, card):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.driver.find_element_by_css_selector('#braintree-dropin-frame')))
        self.find_element(SignUpCheckout.cardNumber).send_keys(card)

    def EnterExpirationDate(self, expiry):
        self.find_element(SignUpCheckout.expirationDate).send_keys(expiry)

    def EnterCVV(self, cvv):
        self.find_element(SignUpCheckout.CVV).send_keys(cvv)

    def click_Pay1(self):
        self.driver.switch_to_default_content()
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)




