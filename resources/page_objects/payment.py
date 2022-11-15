from resources.config_methods import DataClass
from resources.locators import Payment
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pay(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Payment.enter_zip).clear()
        self.find_element(Payment.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Payment.submit_zip)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Payment.yourAccount)).click()

    def click_signin(self):
        self.scroll_to_element(Payment.SignInButton)
        self.click(Payment.SignInButton)

    def EnterEmail(self, email):
        self.find_elements(Payment.Email).clear()
        self.find_element(Payment.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Payment.Pass).clear()
        self.find_element(Payment.Pass).send_keys(password)

    def click_login(self):
        self.click(Payment.LoginButton)

    def click_fresh(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Payment.GoFresh)).click()

    def click_additem(self):
        self.scroll_to_element(Payment.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ADDLG(self):
        self.click(Payment.AddToCartLG)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        element = self.driver.find_element_by_id('lnkProceedToCheckout')
        self.driver.execute_script("arguments[0].click();", element)

    def click_payment1(self):
        self.scroll_to_element(Payment.payment)
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.driver.switch_to_default_content()
        # self.click(Payment.Pay)
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        self.click(Payment.checkout2)

    def click_paymentMethod(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.driver.find_element_by_css_selector('#braintree-dropin-frame')))
        self.click(Payment.choosePayment)

    def click_AddPaymentMethod(self):
        self.driver.switch_to_default_content()
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.driver.find_element_by_css_selector('#braintree-dropin-modal-frame')))
        element = self.driver.find_element_by_css_selector('body > div.modal-wrap > div > div > div.modal-container > div.list-payment-methods-view.modal-frame-view.render-in-assemble > div.modal-body-content > div.add-payment-method-item > span')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterCardNumber(self, card):
        self.find_element(Payment.cardNumber).send_keys(card)

    def EnterExpiry(self, expiry):
        self.find_element(Payment.expiry).send_keys(expiry)

    def EnterCVV(self, cvv):
        self.find_element(Payment.CVV).send_keys(cvv)

    def label(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.driver.find_element_by_css_selector('#braintree-dropin-modal-frame')))

    def click_AddMethod(self):
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

