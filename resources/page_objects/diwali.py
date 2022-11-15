from resources.config_methods import DataClass
from resources.locators import Diwali_Kit
from resources.page_objects.base_page import BasePage

class DiwaliGift(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Diwali_Kit.enter_zip).clear()
        self.find_element(Diwali_Kit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        element = self.driver.find_element_by_id('zipsubmitbtn')
        self.driver.execute_script("arguments[0].click();", element)

    def submit_zip1(self):
        self.click(Diwali_Kit.submit_zip1)

    def GiftNow(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "searchhide"] / section[2] / div / div[2] / div / a / input')
        self.driver.execute_script("arguments[0].click();", element)

    def SmallPack(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "searchhide"] / div[2] / div / div[1] / div[1] / div[3] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def RectangleBox(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/div/div[1]/div[7]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def BurfiBox(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / div[2] / div / div[1] / div[14] / div[3] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def SubmitDeal(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "popupdelivery_date"] / div / div / center / button')
        self.driver.execute_script("arguments[0].click();", element)

    def PlusSmallBox(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / div[2] / div / div[1] / div[1] / div[3] / div / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def MinusSmallBox(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/div/div[1]/div[1]/div[3]/div/p/a/span[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def DetailsComboBox(self):
        element = self.driver.find_element_by_xpath(
            '  // *[ @ id = "searchhide"] / div[2] / div / div[1] / div[3] / div[2] / div[2] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def CloseDetailsComboBox(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "dvDialog-Custom"] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def Click_Next(self):
        element = self.driver.find_element_by_xpath('//*[@id="btnnext"]')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCart(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / div[2] / div / div[1] / div[1] / div[3] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_DiwaliGift(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[10]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_GiftNow(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "searchhide"] / section[2] / div / div[2] / div / a / input')
        self.driver.execute_script("arguments[0].click();", element)


    def click_LeftArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[10]/div/div/i[1]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_IMKS(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[1]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Diwali_Kit.Email).clear()
        self.find_element(Diwali_Kit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Diwali_Kit.Pass).clear()
        self.find_element(Diwali_Kit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(Diwali_Kit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)

    def click_quicklly(self):
        self.click(Diwali_Kit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/p/span[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectStore(self):
        self.click(Diwali_Kit.selectStore)

    def click_ProceedtoCheckout(self):
        self.click(Diwali_Kit.ProceedtoCheckout)

    def click_selectDate(self):
        self.click(Diwali_Kit.selectDate)

    def click_Date(self):
        self.click(Diwali_Kit.chooseDate)

    def RecipientEmail(self, email):
        self.find_elements(Diwali_Kit.Email1).clear()
        self.find_element(Diwali_Kit.Email1).send_keys(email)

    def RecipientFName(self, fname):
        self.find_elements(Diwali_Kit.FName).clear()
        self.find_element(Diwali_Kit.FName).send_keys(fname)

    def RecipientLName(self, lname):
        self.find_elements(Diwali_Kit.LName).clear()
        self.find_element(Diwali_Kit.LName).send_keys(lname)

    def RecipientPhone(self, Phone):
        self.find_elements(Diwali_Kit.PhoneNo).clear()
        self.find_element(Diwali_Kit.PhoneNo).send_keys(Phone)

    def RecipientAddress(self, address):
        self.find_elements(Diwali_Kit.Address).clear()
        self.find_element(Diwali_Kit.Address).send_keys(address)

    def RecipientApartment(self, Apartment):
        self.find_elements(Diwali_Kit.ApartmentNo).clear()
        self.find_element(Diwali_Kit.ApartmentNo).send_keys(Apartment)


    def click_Submit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="save_recipent"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Skipthistep(self):
        element = self.driver.find_element_by_xpath(
             '//*[@id="skip1"]/a')
        self.driver.execute_script("arguments[0].click();", element)