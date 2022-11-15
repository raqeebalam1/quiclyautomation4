import time
from resources.config_methods import DataClass
from resources.locators import MiniCart
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterEmail(self, email):
        self.find_elements(MiniCart.Email).clear()
        self.find_element(MiniCart.Email).send_keys(email)

    def EnterSearch(self, search):
        self.find_elements(MiniCart.SearchForProducts).clear()
        self.find_element(MiniCart.SearchForProducts).send_keys(search)

    def EnterPass(self, password):
        self.find_elements(MiniCart.Pass).clear()
        self.find_element(MiniCart.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def zip(self, zipcode):
        self.find_elements(MiniCart.enter_zip).clear()
        self.find_element(MiniCart.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(MiniCart.submit_zip)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def Empty_cart(self):
        self.find_element(MiniCart.empty_cart).get_attribute('innerHTML')

    def click_CheckOut(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_AddToCart(self):
        self.scroll_to_element(MiniCart.Add1)
        self.click(MiniCart.Add1)

    def click_plus(self):
        element = self.driver.find_element_by_xpath('//*[@id="qty_cart_270"]/a[2]')
        self.driver.execute_script("arguments[0].click();", element)
        # button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#qty_cart_270 > ''a:nth-child(3)')))
        # button.click()

    def click_minus(self):
        element = self.driver.find_element_by_xpath('//*[@id="qty_cart_270"]/a[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_delete(self):
        self.click(MiniCart.delete_item)

    def click_Checkout(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_additem(self):
        self.scroll_to_element(MiniCart.additem)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div[2]/div/div/div[1]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Additem2(self):
        # self.scroll_to_element(MiniCart.additem2)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div[2]/div/div/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddItem1(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(MiniCart.additem2)).click()

    def click_order(self):
        self.click(MiniCart.orderFood)

    def click_express(self):
        self.click(MiniCart.express)

    def click_item(self):
        # self.scroll_to_element(MiniCart.item1)
        element = self.driver.find_element_by_xpath('//*[@id="filterresult"]/div[1]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_item2(self):
        # self.scroll_to_element(MiniCart.item1)
        element = self.driver.find_element_by_xpath('//*[@id="filterresult"]/div[1]/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem1(self):
        self.click(MiniCart.additem1)


    def click_rightArrow(self):
        self.click(MiniCart.right_arrow)

    def click_leftArrow(self):
        self.click(MiniCart.left_arrow)

    def click_dropDown1(self):
        self.scroll_to_element(MiniCart.drop_down1)
        element = self.driver.find_element_by_id('qty_270')
        self.driver.execute_script("arguments[0].click();", element)

    def click_dropDown2(self):
        element = self.driver.find_element_by_id('qty_51875')
        self.driver.execute_script("arguments[0].click();", element)

    def click_quantity(self):
        self.click(MiniCart.drop_quantity)

    def click_remove(self):
        element = self.driver.find_element_by_xpath('//*[@id="lnk_51875"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_eVoucher(self):
        self.scroll_to_element(MiniCart.eVoucher)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#vocherRewardWallet-1"))).click()

    def click_reward(self):
        self.scroll_to_element(MiniCart.reward)
        element = self.driver.find_element_by_xpath('//*[@id="vocherRewardWallet-2"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_wallet(self):
        element = self.driver.find_element_by_id('vocherRewardWallet-3')
        self.driver.execute_script("arguments[0].click();", element)

    def enter_eVoucher(self, evoucher):
        self.scroll_to_element(MiniCart.eVoucher_text)
        self.find_elements(MiniCart.eVoucher_text).clear()
        self.find_element(MiniCart.eVoucher_text).send_keys(evoucher)

    def enter_reward(self, reward):
        self.scroll_to_element(MiniCart.reward_text)
        self.wait_for_loader(10)
        self.find_elements(MiniCart.reward_text).clear()
        self.find_element(MiniCart.reward_text).send_keys(reward)

    def click_NoTIp(self):
        element = self.driver.find_element_by_id('tipzero')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tip5(self):
        element = self.driver.find_element_by_id('tipthree')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tip10(self):
        element = self.driver.find_element_by_id('tipfive')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tip15(self):
        element = self.driver.find_element_by_id('tipseven')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Tip20(self):
        element = self.driver.find_element_by_id('tipten')
        self.driver.execute_script("arguments[0].click();", element)

    def click_changeAddress(self):
        self.scroll_to_element(MiniCart.ChangeAddress)
        self.click(MiniCart.ChangeAddress)

    def click_Cross(self):
        self.click(MiniCart.clickCross)

    def enter_notes(self, notes):
        self.scroll_to_element(MiniCart.Notes_text)
        self.find_elements(MiniCart.Notes_text).clear()
        self.find_element(MiniCart.Notes_text).send_keys(notes)

    def click_payment(self):
        time.sleep(15)
        self.scroll_to_element(MiniCart.Payment)
        self.scroll_to(1653, 1050)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(MiniCart.Payment))
        element.click()

    def click_apply(self):
        element = self.driver.find_element_by_xpath('//*[@id="parRadioOne"]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_paypal(self):
        self.click(MiniCart.paypal)

    def click_SignIn(self):
        self.click(MiniCart.signIn)

    def click_ShopNow(self):
        self.click(MiniCart.shopNow)

    def click_Grocery(self):
        self.click(MiniCart.clickGrocery)

    def click_SecondShop(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#minicart > div > div.clsHead.basket > div > div > div > '
                                                         'a:nth-child(2)')))
        button.click()

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MiniCart.yourAccount)

    def click_changeMethod(self):
        time.sleep(15)
        element = self.driver.find_element_by_id('choose-payment-method')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Addmethod(self):
        self.click(MiniCart.AddPaymentMethod)

    def EnterCardNumber(self, credit):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(MiniCart.CreditCardNumber))
        self.find_elements(MiniCart.CreditCardNumber).clear()
        self.find_element(MiniCart.CreditCardNumber).send_keys(credit)

    def click_Credit(self):
        time.sleep(1)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(MiniCart.clickCredit)).click()

    def EnterExpiry(self, expiration):
        self.find_elements(MiniCart.Expiration).clear()
        self.find_element(MiniCart.Expiration).send_keys(expiration)

    def EnterCVV(self, Cvv):
        self.find_elements(MiniCart.CVV).clear()
        self.find_element(MiniCart.CVV).send_keys(Cvv)

    def click_Pay(self):
        self.click(MiniCart.Pay)

    def deliveryLabel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(MiniCart.DeliveryLabel))

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Department(self):
        self.click(MiniCart.Department)

    def click_ShopByGrocery(self):
        self.click(MiniCart.GroceryShop)

    def click_CrossButton(self):
        self.click(MiniCart.crossButton)

    def click_quicklly(self):
        self.click(MiniCart.quicklly)

    def checkLabel(self):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(MiniCart.shops_name))
        label3 = self.get_attribute(MiniCart.shops_name, 'src')
        print(label3)

    def click_fresh(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(MiniCart.GoFresh)).click()

    def click_Search(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchbtn"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MiniCart.HitSearch)

    def click_Checkout2(self):
        self.click(MiniCart.checkout2)

