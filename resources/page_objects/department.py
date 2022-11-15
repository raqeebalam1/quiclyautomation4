from resources.config_methods import DataClass
from resources.locators import Department, AddRecipient
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dept(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Department.enter_zip).clear()
        self.find_element(Department.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Department.submit_zip)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)
        #self.click(Department.SignInButton)
        #WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.SignInButton)).click()
        #element = self.driver.find_element(Department.SignInButton)
        #self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Department.Email).clear()
        self.find_element(Department.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Department.Pass).clear()
        self.find_element(Department.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_css_selector('body > header > div.clsCart2 > a')
        self.driver.execute_script("arguments[0].click();", element)


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

    def click_Checkout(self):
        element = self.driver.find_element_by_css_selector('#lnkProceedToCheckout')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ProceedtoCheckout(self):
        self.click(Department.ProceedtoCheckout)

    def click_payment1(self):
        element = self.driver.find_element_by_xpath('//*[@id="proceedtopayment"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_payment2(self):
        element = self.driver.find_element_by_css_selector('#proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    # def click_Proceedtocheckout(self):
    #     element = self.driver.find_element_by_xpath(' // *[ @ id = "dvFoodSuggestPopup"] / div / div / a')
    #     self.driver.execute_script("arguments[0].click();", element)

    def click_additem(self):
        self.scroll_to_element(Department.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        element = self.driver.find_element_by_id('pay_amount')
        self.driver.execute_script("arguments[0].click();", element)

    def click_InstantPot(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[10]/div/div/div/div/a[17]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Department(self):
        self.click(Department.Department)

    def click_Department1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_select(self):
        # self.scroll_to_element(Department.select)
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.select))
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Oragnicsauces(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]//img[@alt="Organic Meal Kits and Sauces by Seeti"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Add(self):
        # self.scroll_to_element(Department.Add)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div[2]/div/div[2]/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Details(self):
       # self.scroll_to_element(Department.Add)
        element = self.driver.find_element_by_xpath('  // *[ @ id = "searchhide"] / div[3] / div[2] / div / div[2] / div[3] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        self.click(Department.AddToCart)

    def click_Sauces(self):
        self.click(Department.Sauces)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('/html/body/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_seeti(self):
        self.click(Department.Seeti)

    def click_rightArrow(self):
        self.click(Department.right_arrow)

    def click_remove(self):
        self.click(Department.delete)

    def click_fresh(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.GoFresh)).click()

    def click_ADDLG(self):
        self.click(Department.AddToCartLG)

    def click_addPotato(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_51875"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartPotato(self):
        self.click(Department.AddToCartP)

    def click_food(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[5]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MakkiFood(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[12]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addTenders(self):
        self.scroll_to_element(Department.AddTenders)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartTenders(self):
        self.click(Department.TendersAddToCart)

    def click_submitTenders(self):
        self.click(Department.submitTenders)

    def click_BBQ(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[9]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_TikkaImage(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_132523"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddChickenTikkaToCart(self):
        self.click(Department.AddTikkaToCart)

    def click_Catering(self):
        self.click(Department.Catering)

    def click_Hyderabad(self):
        element = self.driver.find_element_by_css_selector('#Catering > div > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBeef(self):
        self.scroll_to_element(Department.AddBeefFry)
        element = self.driver.find_element_by_css_selector('#searchhide > div.clsFoodStore > div > div > div:nth-child(1) > a')
        self.driver.execute_script("arguments[0].click();", element)
#//*[@id="searchhide"]/div[5]/div/div/div[1]/a
    def click_AddToCartBeef(self):
        self.click(Department.AddToCartBeef)

    def click_Medium(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "dvDialog-Custom"] / div / div[1] / div / div[1] / ul / li[2] / label / input')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SubmitBeef(self):
        # self.scroll_to_element(Department.MealPlan)
        element = self.driver.find_element_by_css_selector('#dvDialog-DateTime > div > div.clsFooter > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_mealBasket(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[11]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Qty1(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "ddlProdQty"]')
        self.driver.execute_script("arguments[0].click();", element)


    def click_3Qty(self):
        element = self.driver.find_element_by_xpath('  // *[ @ id = "ddlProdQty"] / option[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def select_mealPlan(self):
        self.scroll_to_element(Department.MealPlan)
        element = self.driver.find_element_by_xpath('//*[@id="meal-basket"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Korma(self):
        self.scroll_to_element(Department.AddKorma)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def Plus_Korma(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartCK(self):
        self.click(Department.AddToCartCK)

    def click_Tiffin(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.TiffinServices)).click()

    def click_Tiffin1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[9]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Chicago(self):
        element = self.driver.find_element_by_xpath('//*[@id="tiffin-services"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_KamdarTiffin(self):
        element = self.driver.find_element_by_xpath('//*[@id="tiffin-services"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_Submit4(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "dvDialog-DateTime"] / div / div[2] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_VegThali(self):
        element = self.driver.find_element_by_xpath('//*[@id="TiffinServices"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartVT(self):
        element = self.driver.find_element_by_css_selector('#dvDialog-Custom > div > div.clsFooter > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Roti(self):
        element = self.driver.find_element_by_xpath('//*[@id="OneTime"]/div[1]/ul/li[2]/label')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Date(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "ddlDeliveryDate"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Schedule(self):
        element = self.driver.find_element_by_xpath(' // *[ @ id = "ddlDeliveryDate"] / option[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChangeSlot(self):
        element = self.driver.find_element_by_xpath('  // *[ @ id = "selectDateTimeSlot"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Slot(self):
        element = self.driver.find_element_by_xpath('//*[@id="ddlDeliveryTime"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Time(self):
        element = self.driver.find_element_by_xpath('//*[@id="ddlDeliveryTime"]/option[3]')
        self.driver.execute_script("arguments[0].click();", element)








    def submitVT(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.submitVT)).click()

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[10]/div/div/div/div/a[16]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PremiumGiftBox(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[4]/div/a/div/div/h3')
        self.driver.execute_script("arguments[0].click();", element)


    def click_BuildBoxPremiumGiftBox(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath(' // *[ @ id = "searchhide"] / section[1] / div / div / div[2] / div[4] / div[6] / form / button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SpringCollection(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath(' // *[ @ id = "searchhide"] / div[4] / div / div / div[2] / div[3] / div / a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_NoorCollection(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath(
            ' //*[@id="searchhide"]/div[4]/div/div/div[3]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_10packNoorCollection(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[4]/div/div/div[3]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def select_MealPlan20(self):
        self.scroll_to_element(Department.selectMealKit)
        element = self.driver.find_element_by_css_selector('#meal-kit > div.clsSlider > div:nth-child(1) > form > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CuminCLub(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[4]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Papad(self):
        element = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def Plus_Papad(self):
        self.click(Department.plusPapad)

    def click_AddToCartPapad(self):
        self.click(Department.AddToCartPapad)

    def click_Recipes(self):
        self.click(Department.Recipes)

    def click_PalakPaneer(self):
        element = self.driver.find_element_by_xpath('//*[@id="45"]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Recipes1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul/li[8]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToBasket(self):
        self.scroll_to_element(Department.AddToBasket)
        element = self.driver.find_element_by_xpath('//*[@id="prd_118"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToBasket1(self):
        self.scroll_to_element(Department.AddToBasket)
        element = self.driver.find_element_by_xpath(' // *[ @ id = "prd_77021"] / span[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Delivery(self):
        element = self.driver.find_element_by_css_selector('#ddlDeliveryDate ')
        self.driver.execute_script("arguments[0].click();", element)


    def click_timeOfDelivery(self):
        element = self.driver.find_element_by_css_selector('#ddlDeliveryTime > option:nth-child(3)')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.timeDelivery)).click()

    def click_TickBox(self):
        self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath('//*[@id="flexCheckDefault"]')
        self.driver.execute_script("arguments[0].click();", element)



    def click_IndianCateringStore(self):
        # self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath(' //*[@id="searchhide"]/div[1]/div/div/i[2]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/i[2]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_RightArrow1(self):
        element = self.driver.find_element_by_css_selector(' # searchhide > div.grocerySpecialSlider.clsFoodSpl.clslowspace > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MomoFactory(self):
        # self.driver.execute_script("window.scrollTo(0,600)")
        # self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath('//*[@id="Catering"]/div/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMomo(self):
        # self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath('// *[ @ id = "searchhide"] / div[5] / div / div / div[1] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddGulabJamun(self):
        # self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath(' // *[ @ id = "searchhide"] / div[5] / div / div / div[5] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OrganicGrocery(self):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_LargeQuantity(self):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_xpath('// *[ @ id = "dvDialog-Custom"] / div / div[1] / div / div[1] / ul / li[3] / label')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BuildBox(self):
        self.scroll_to_element(Department.BuildABox)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddJowar(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartJowar(self):
        self.click(Department.AddToCartOrganic)

    def click_LeftArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/i[1]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotiKit(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.rotiKIt)).click()

    def click_RotiBox(self):
        self.scroll_to_element(Department.buildRotiBox)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddWholeWheatRoti(self):
        self.scroll_to_element(Department.AddWholeWheatRoti)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartRoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Liquor(self):
        self.click(Department.liquorStore)

    def click_beer(self):
        self.click(Department.Beer)

    def click_gin(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[2]/ul/div/div/li[7]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_classicLime(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_137860"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartLime(self):
        element = self.driver.find_element_by_xpath('//*[@id="storeproductlist"]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.AddToCartLime)

    def click_Becks12(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_137801"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Becks12p12(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[1]/div/div[2]/div/ul/li[2]/span[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBecks12(self):
        element = self.driver.find_element_by_xpath('//*[@id="storeproductlist"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AmsterdamGin(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="New Amsterdam Gin"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AmsterdamGin200ml(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[1]/div/div[2]/div/ul/li[1]/span[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartAmsterdamGin(self):
        element = self.driver.find_element_by_xpath('//*[@id="storeproductlist"]/div[1]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChaiAndCoffee(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ChaiBox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def AddKimbala(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/div/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)


    def click_IndianMealKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[11]/div/a/div/div/h3')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SelectProducts(self):
        element = self.driver.find_element_by_xpath('//*[@id="meal-kit"]/div[2]/div[3]/form/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MakkahCafe(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[7]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddAlooSam(self):
        element = self.driver.find_element_by_css_selector('#load_data > div:nth-child(2) > div > div.clsFoodProdCnt > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddtoCartAlooSam(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvDialog-Custom"]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_submitAlooSam(self):
        self.click(Department.submitAlooSam)

    def click_timeOfDeliveryAlooSam(self):
        element = self.driver.find_element_by_css_selector('#ddlDeliveryTime > option:nth-child(2)')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMixVegetable(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[3]/div/div/div[1]/div[1]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddMisalPav(self):
        element = self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[9]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)


    def click_PlusAddMisalPav(self):
        element = self.driver.find_element_by_xpath(' / html / body / div[12] / div / div / div[9] / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_PlusMixVegetable(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.clsFoodStores.clsMealSelect.clsPgWidth > div > div > div.clsFoodStoreCard.active > p > a > span.plusQty')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/p/span[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Methai(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_DalTadka(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[4]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_plusDalTadka(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[4]/div[3]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_legalCheckBox(self):
        element = self.driver.find_element_by_css_selector(
            '#dvDialog-DateTime > div > div.clsContent > p:nth-child(3) > label > input[type=checkbox]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.legalCheckBox)

    def click_elderCheckBox(self):
        element = self.driver.find_element_by_css_selector(
            '#dvDialog-DateTime > div > div.clsContent > p:nth-child(4) > label > input[type=checkbox]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.elderCheckBox)

    def click_submitAlcohol(self):
        element = self.driver.find_element_by_css_selector('#dvDialog-DateTime > div > div.clsFooter > a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.submitALcohol)

    def EnterElementForSearch(self, element):
        self.find_element(Department.searchBox).clear()
        self.find_element(Department.searchBox).send_keys(element)

    def click_SearchButton(self):
        self.click(Department.searchButton)

    def click_HouseHold(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[13]/div[1]/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddJiffyFoilPan(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div/div/div[1]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddHemVanilla(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[1]/div/div/div/div[2]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddCandle(self):
        element = self.driver.find_element_by_xpath('// *[ @ id = "load_data"] / div[2] / div / div / div / div[4] / div / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow2(self):
        element = self.driver.find_element_by_xpath(
            ' // *[ @ id = "load_data"] / div[4] / div / i[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddDawnFloz(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="load_data"]/div[4]/div/div/div/div[7]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Moments(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]//img[@alt="Moments - Celebrate Every Moment"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ExploreQuickllyMoments(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div/div[1]/a/input')
        self.driver.execute_script("arguments[0].click();", element)
    def click_Addtocart_Ganeshbox(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/div/div[1]/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Plus_Ganeshbox(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "searchhide"] / div[2] / div / div[1] / div[1] / div[3] / div / p / a / span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Shopbydepartment(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Department_Moments(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "searchhide"] / header / div[2] / div / div[1] / div[1] / div / div / ul / li[9] / a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Next(self):
        element = self.driver.find_element_by_xpath(
            '// *[ @ id = "btnnext"]')
        self.driver.execute_script("arguments[0].click();", element)

    def RecipientEmail(self, email):
        self.find_elements(AddRecipient.Email).clear()
        self.find_element(AddRecipient.Email).send_keys(email)

    def RecipientFName(self, fname):
        self.find_elements(AddRecipient.FName).clear()
        self.find_element(AddRecipient.FName).send_keys(fname)

    def RecipientLName(self, lname):
        self.find_elements(AddRecipient.LName).clear()
        self.find_element(AddRecipient.LName).send_keys(lname)

    def RecipientPhone(self, Phone):
        self.find_elements(AddRecipient.PhoneNo).clear()
        self.find_element(AddRecipient.PhoneNo).send_keys(Phone)

    def RecipientAddress(self, address):
        self.find_elements(AddRecipient.Address).clear()
        self.find_element(AddRecipient.Address).send_keys(address)

    def RecipientApartment(self, Apartment):
        self.find_elements(AddRecipient.ApartmentNo).clear()
        self.find_element(AddRecipient.ApartmentNo).send_keys(Apartment)

    def DelieveryType(self, DType):
        self.find_elements(AddRecipient.Delieverytype).clear()
        self.find_element(AddRecipient.Delieverytype).send_keys(DType)

    def click_Submit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="save_recipent"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Skipthistep(self):
        element = self.driver.find_element_by_xpath(
             '// *[ @ id = "searchhide"] / div[3] / div / p[3] / a')
        self.driver.execute_script("arguments[0].click();", element)
