from resources.config_methods import DataClass
from resources.locators import IndianMealKit
from resources.page_objects.base_page import BasePage


class IndianMeal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianMealKit.enter_zip).clear()
        self.find_element(IndianMealKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        element = self.driver.find_element_by_id('zipsubmitbtn')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[10]/div/div/div/div/a[16]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit1(self):
        element = self.driver.find_element_by_css_selector(
            '  # searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > div > div > a:nth-child(16) > img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_indianMealKitSub(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[11]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_LeftArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[10]/div/div/i[1]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_5mealkit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[3]/form/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="meal-kit"]/div[2]/div[3]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[3]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[3]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[3]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly3(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "meal-kit"] / div[2] / div[1] / ul / li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly3(self):
        element = self.driver.find_element_by_xpath(
            '  // *[ @ id = "meal-kit"] / div[2] / div[1] / ul / li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once3(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "meal-kit"] / div[2] / div[1] / ul / li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[1]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[5]/form/button')
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
        self.find_elements(IndianMealKit.Email).clear()
        self.find_element(IndianMealKit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(IndianMealKit.Pass).clear()
        self.find_element(IndianMealKit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_css_selector('body > header > div.clsCart2 > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(IndianMealKit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)

    def click_quicklly(self):
        self.click(IndianMealKit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddDaalChawal(self):
        element = self.driver.find_element_by_css_selector('body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div.clsFoodStoreCard.active > div:nth-child(6) > div:nth-child(3)')
        self.driver.execute_script("arguments[0].click();", element)

    def plusDaalChawal(self):
        element = self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/p/span[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart2(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.clsCateringDeliveryInfo.clsMealSelectAlert > p > span:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Indianmealkitdelivery(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "searchhide"] / div[1] / div[1] / ul / li[3] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Indianmealkitdelivery2(self):
        element = self.driver.find_element_by_css_selector(
            '# searchhide > div.clsFoodStoreBanner > div.clsPgWidth.clsBreadcrumb > ul > li:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectStore(self):
        self.click(IndianMealKit.selectStore)

    def click_ProceedtoCheckout(self):
        self.click(IndianMealKit.ProceedtoCheckout)

    def click_CurryBox(self):
        self.click(IndianMealKit.curryBox)

    def click_selectDate(self):
        self.click(IndianMealKit.selectDate)

    def click_Date(self):
        self.click(IndianMealKit.chooseDate)

    def click_ChangeSlot(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="dvDialog-Slot-DateTime"]/div/div/div[3]/a[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bisibelebath(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusBisibelebath(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[1]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MinusBisiblebath(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[1]/p/a/span[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MasalaBhindi(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[6]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pudinarice(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[25]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_DalFry(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[3]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_DetailsMisalpav(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[9]/div[3]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CloseDetailsMisalpav(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="dvDialog-Custom"]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddGajarhalwa(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[5]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusGajarhalwa(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[5]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bisibelebath2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(1) > div:nth-child(6) > div:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusBisibelebath2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div.clsFoodStoreCard.active > p > a > span.plusQty')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MinusBisiblebath2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div.clsFoodStoreCard.active > p > a > span.minusQty')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MasalaBhindi2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(6) > div:nth-child(6) > div:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pudinarice2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(25) > div:nth-child(6) > div:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_DalFry2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(3) > div:nth-child(6) > div:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_DetailsMisalpav2(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[13]/div/div/div[9]/div[3]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CloseDetailsMisalpav2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="dvDialog-Custom"]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddGajarhalwa2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(5) > div:nth-child(6) > div:nth-child(3) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusGajarhalwa2(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div:nth-child(5) > p > a > span.plusQty')
        self.driver.execute_script("arguments[0].click();", element)

    def click_10mealkit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[2]/form/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_20mealkit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="meal-kit"]/div[2]/div[1]/form/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Palakpanneer(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[11]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusPalakpanneer(self):
        element = self.driver.find_element_by_xpath(
            '/ html / body / div[12] / div / div / div[11] / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)
