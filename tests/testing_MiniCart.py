import time
from resources import ui_test_class
from resources.page_objects.cart import MiniCart
from resources.page_objects.cart import Cart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TesCART(ui_test_class.UVClass):
    cart_page: Cart
    cart_page: MiniCart
    actual1 = "Your cart is empty"
    actual2 = "Checkout with Quicklly $1.78"
    actual3 = '2 items'
    actual4 = " Minimum Order Value: $30"
    actual5 = "	Lemon Grass "
    actual6 = "1"
    actual7 = "$0.59"
    actual8 = "Fresh Farms Total: $0.59"
    actual9 = "$1.18"
    actual10 = "https://www.uat.goquicklly.com/upload_images/product/thumb/1495539333-lemon-grass.jpg"
    actual11 = "Fresh Farms"
    actual12 = "20"
    actual13 = "Your Shopping Carts"
    actual14 = "Seeti"
    actual15 = "$0.29"
    actual16 = "3"
    actual17 = "$1.78"
    actual18 = "Curbside Pickup"
    actual19 = "Delivery"
    actual20 = "eVoucher"
    actual21 = "/images/allstores.png"
    actual22 = "https://www.uat.goquicklly.com/upload_images/product/thumb/1495539333-lemon-grass.jpg"
    actual23 = "https://www.uat.goquicklly.com/upload_ima[41 chars].jpg"
    actual24 = "(2 item)"
    actual25 = "Items in your  cart"
    actual26 = "Remove"
    actual27 = "eVoucher"
    actual28 = "Reward Point (1000)"
    actual29 = "My Wallet (100)"
    actual30 = "Your e-voucher Code option"
    actual31 = " * A maximum of one voucher is applicable for an order"
    actual32 = "Your Reward Point (optional)*"
    actual34 = "Your Wallet Balance"
    actual33 = " * Reward Point applicable"
    actual35 = "Your Wallet is empty"
    actual36 = "Order Summary"
    actual37 = "(2 items)"
    actual38 = "Groceries Subtotal (2 items)"
    actual39 = "Food Subtotal (0 item)"
    actual40 = "(0 item)"
    actual41 = "$0.00"
    actual42 = "Estimated Tax"
    actual43 = "Estimated Shipping"
    actual44 = "$4.99"
    actual45 = "Estimated Minimum Charges"
    actual46 = "$4.99"
    actual47 = "Packaging Handling"
    actual48 = "$2.99"
    actual49 = "Tip"
    actual50 = "$0.09"
    actual51 = "Estimated Shipping"
    actual52 = "10.93"
    actual53 = "Shipping Address:"
    actual54 = "Change Address"
    actual55 = "$0.59"
    actual56 = "1"
    actual57 = "Estimated delivery:<br>"
    actual58 = "Delivery Notes"
    actual59 = "Please be on time"
    actual60 = "Proceed to Payment"
    actual61 = "(2 items)"
    actual62 = "$0.88"
    actual63 = "QD1100306"
    actual64 = "POTATO -  RED POTATOES"
    actual65 = "$1.19"
    actual66 = "1"
    actual67 = "$0.00"
    actual68 = "Hello, User"
    actual69 = "Campus Market"
    actual70 = "12345"
    actual71 = "10.75"
    actual72 = "10.84"
    actual73 = "10.93"
    actual74 = "11.02"
    actual75 = "11.11"
    actual76 = ""
    actual77 = "Thank you"

    @classmethod
    def setUpClass(cls):
        super(TesCART, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCART, cls).tearDownClass()
        cls.driver.quit()

    def AddItem(self):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        if alert:
            alert.accept()
        self.cart_page.EnterSearch("lemon grass")
        self.cart_page.click_Search()
        time.sleep(5)
        self.cart_page.click_item()
        time.sleep(5)
        # self.cart_page.click_additem()
        # self.cart_page.click_AddItem1()
        # time.sleep(2)
        # self.cart_page.click_Additem2()
        self.cart_page.EnterSearch("potato")
        self.cart_page.click_Search()
        time.sleep(5)
        self.cart_page.click_item2()
        time.sleep(2)


    def AddItem1(self):
        time.sleep(5)
        self.cart_page.EnterSearch("lemon grass")
        self.cart_page.click_Search()
        time.sleep(5)
        # self.cart_page.click_additem()
        self.cart_page.click_item()
        self.cart_page.EnterSearch("potato")
        self.cart_page.click_Search()
        time.sleep(5)
        self.cart_page.click_item2()
        time.sleep(2)
        # self.cart_page.click_Additem2()
        self.cart_page.click_MiniCart()
        self.cart_page.click_Checkout()

    def clickQuicklly(self):
        self.cart_page.click_quicklly()
        self.cart_page.submit_zip()
        self.AddItem()
        self.cart_page.click_MiniCart()
        self.cart_page.click_Checkout()

    def Addmethod(self):
        self.cart_page.click_Addmethod()
        self.cart_page.EnterCardNumber("4005519200000004")
        self.cart_page.EnterExpiry("0226")
        self.cart_page.EnterCVV("158")

    def test_ZsignIN(self):
        self.cart_page.select_dropdown()
        self.cart_page.click_signin()
        self.cart_page.EnterEmail("testaccount@quicklly.com")
        self.cart_page.EnterPass("123456")
        self.cart_page.click_login()
        name = self.cart_page.get_attribute(MiniCart.accountName, 'innerHTML')
        print(name)
        self.assertEqual(self.actual68, name)

    def test_ZipCode(self):
        self.cart_page.zip("60611")
        self.cart_page.submit_zip()
        self.cart_page.click_MiniCart()
        empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
        print(empty)
        self.assertEqual(self.actual1, empty)

    def test_addItem(self):
        self.AddItem()
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_plus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual12, ItemQuantity)

    def test_checkout(self):
        check = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
        print(check)
        self.assertEqual(self.actual2, check)

    def test_name(self):
        self.cart_page.click_MiniCart()
        NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'textContent')
        print(NameOfItem)
        self.assertEqual(self.actual5, NameOfItem)

    def test_quantity_price(self):
        self.cart_page.click_MiniCart()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        self.assertEqual(self.actual55, price)

    def test_quantity(self):
        self.cart_page.click_MiniCart()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual6, ItemQuantity)

    def test_minimum(self):
        self.cart_page.click_MiniCart()
        MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
        print(MinimumOrder)
        self.assertEqual(self.actual4, MinimumOrder)


    def test_two_shops(self):
        self.cart_page.click_MiniCart()
        ShopName = self.cart_page.get_attribute(MiniCart.shop_name, 'innerHTML')
        print(ShopName)
        self.assertEqual(self.actual11, ShopName)
    #
    def test_check_updated_price(self):
        self.cart_page.click_Checkout()
        self.cart_page.click_Checkout2()
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        self.cart_page.click_minus()
        self.assertEqual(self.actual9, price)

    def test_bmin(self):
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        print("Item with minimum quantity is added")
        self.assertEqual(self.actual6, ItemQuantity)



    def test_bmax(self):
        time.sleep(5)
        self.cart_page.click_MiniCart()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual12, ItemQuantity)
        print("Item with maximum quantity is added")

    def test_shopping(self):
        label = self.cart_page.get_attribute(MiniCart.shopping_carts, 'innerHTML')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_label(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(MiniCart.shops_name))
        label3 = self.cart_page.get_attribute(MiniCart.shops_name, 'src')
        label4 = self.cart_page.get_attribute(MiniCart.shops_name1, 'src')
        print(label3)
        print(label4)
        self.assertEqual(self.actual22, label3)
        # self.assertEqual(self.actual23, label4)

    def test_pickup(self):
        pickup_label = self.cart_page.get_attribute(MiniCart.CurbsidePickup, 'innerHTML')
        print(pickup_label)
        self.assertEqual(self.actual18, pickup_label)

    def test_cidelivery(self):
        delivery_label = self.cart_page.get_attribute(MiniCart.Delivery, 'innerHTML')
        print(delivery_label)
        self.assertEqual(self.actual19, delivery_label)


    def test_items(self):
        itemsInCart = self.cart_page.get_attribute(MiniCart.ItemInCart, 'innerHTML')
        print(itemsInCart)
        self.assertEqual(self.actual25, itemsInCart)

    def test_dropdown1(self):
        self.cart_page.click_dropDown1()

    def test_dropdown2(self):
        time.sleep(10)
        # self.cart_page.click_dropDown2()
        itemsInCart = self.cart_page.get_attribute(MiniCart.ItemInCart, 'innerHTML')
        print(itemsInCart)
        self.assertEqual(self.actual25, itemsInCart)

    def test_remove(self):
        RemoveLabel1 = self.cart_page.get_attribute(MiniCart.remove1, 'innerHTML')
        RemoveLabel2 = self.cart_page.get_attribute(MiniCart.remove2, 'innerHTML')
        print(RemoveLabel1, RemoveLabel2)
        self.assertEqual(self.actual26, RemoveLabel2)
        self.assertEqual(self.actual26, RemoveLabel1)

    def test_dropdown_quantity(self):
        time.sleep(10)
        # self.cart_page.click_dropDown2()
        # self.cart_page.click_quantity()
        itemsInCart = self.cart_page.get_attribute(MiniCart.ItemInCart, 'innerHTML')
        print(itemsInCart)
        self.assertEqual(self.actual25, itemsInCart)

    def test_remove_item(self):
        self.cart_page.click_remove()
        ItemTotal = self.cart_page.get_attribute(MiniCart.groceriesItemTotal, 'innerHTML')
        print(ItemTotal)
        # self.cart_page.click_Department()
        # self.cart_page.click_ShopByGrocery()
        # self.AddItem1()
        self.assertEqual(self.actual61, ItemTotal)

    def test_eVoucher_label(self):
        e_label = self.cart_page.get_attribute(MiniCart.eVoucher_label, 'innerHTML')
        print(e_label)
        self.assertEqual(self.actual27, e_label)

    def test_reward(self):
        self.cart_page.click_reward()
        RewardPointLAbel = self.cart_page.get_attribute(MiniCart.rewardPoint, 'innerHTML')
        print(RewardPointLAbel)
        self.assertEqual(self.actual32, RewardPointLAbel)

    def test_reward_label(self):
        reward_label = self.cart_page.get_attribute(MiniCart.reward_label, 'innerHTML')
        print(reward_label)
        self.assertEqual(self.actual28, reward_label)



    def test_wallet_label(self):
        wallet_label = self.cart_page.get_attribute(MiniCart.wallet_label, 'innerHTML')
        print(wallet_label)
        self.assertEqual(self.actual29, wallet_label)

    def test_label_codeOption(self):
        CodeOption = self.cart_page.get_attribute(MiniCart.codeOption, 'innerHTML')
        print(CodeOption)
        self.assertEqual(self.actual30, CodeOption)

    def test_eVoucher_text(self):
        time.sleep(15)
        self.cart_page.enter_eVoucher("12345")
        textvalue = self.cart_page.get_attribute(MiniCart.eVoucher_text_value, 'value')
        print(textvalue)
        self.assertEqual(self.actual70, textvalue)

    def test_max_eVoucher(self):
        maximum_eVoucher = self.cart_page.get_attribute(MiniCart.maximum_eVoucher, 'innerHTML')
        print(maximum_eVoucher)
        self.assertEqual(self.actual31, maximum_eVoucher)

    def test_rewardPoint(self):
        self.cart_page.click_reward()
        RewardPointLAbel = self.cart_page.get_attribute(MiniCart.rewardPoint, 'innerHTML')
        print(RewardPointLAbel)
        self.assertEqual(self.actual32, RewardPointLAbel)

    def test_rewardPointApplicable(self):
        self.cart_page.click_reward()
        RPA_label = self.cart_page.get_attribute(MiniCart.rewardPointApplicable, 'innerHTML')
        print(RPA_label)
        self.assertEqual(self.actual33, RPA_label)

    def test_walletBalance(self):
        time.sleep(15)
        self.cart_page.scroll_to_element(MiniCart.wallet)
        balance = self.cart_page.get_attribute(MiniCart.walletBalance, 'innerHTML')
        print(balance)
        self.assertEqual(self.actual34, balance)


    def test_order_summary(self):
        self.cart_page.scroll_to_element(MiniCart.orderSummary)
        summary = self.cart_page.get_attribute(MiniCart.orderSummary, 'innerHTML')
        print(summary)
        self.assertEqual(self.actual36, summary)

    def test_groceries_total(self):
        SubTotal = self.cart_page.get_text(MiniCart.groceriesSubTotal)
        print(SubTotal)
        self.assertEqual(self.actual38, SubTotal)

    def test_groceries_items(self):
        ItemTotal = self.cart_page.get_attribute(MiniCart.groceriesItemTotal, 'innerHTML')
        print(ItemTotal)
        self.assertEqual(self.actual37, ItemTotal)

    def test_grocery_price(self):
        groceriesPrice = self.cart_page.get_attribute(MiniCart.groceriesPrice, 'innerHTML')
        print(groceriesPrice)
        self.assertEqual(self.actual17, groceriesPrice)

    def test_food_total(self):
        subtotal = self.cart_page.get_text(MiniCart.FoodSubTotal)
        print(subtotal)
        self.assertEqual(self.actual39, subtotal)

    def test_food_itemTotal(self):
        ItemTotal = self.cart_page.get_attribute(MiniCart.FoodItemTotal, 'innerHTML')
        print(ItemTotal)
        self.assertEqual(self.actual40, ItemTotal)

    def test_food_price(self):
        FoodPrice = self.cart_page.get_attribute(MiniCart.FoodPrice, 'innerHTML')
        print(FoodPrice)
        self.assertEqual(self.actual41, FoodPrice)

    def test_tax_label(self):
        Estimated = self.cart_page.get_attribute(MiniCart.EstimatedTax, 'innerHTML')
        print(Estimated)
        self.assertEqual(self.actual42, Estimated)

    def test_tax_price(self):
        EstimatedPrice = self.cart_page.get_attribute(MiniCart.EstimatedTaxPrice, 'innerHTML')
        print(EstimatedPrice)
        self.assertEqual(self.actual67, EstimatedPrice)

    def test_shipping_estimated(self):
        EstimatedShipping_label = self.cart_page.get_attribute(MiniCart.EstimatedShipping, 'innerHTML')
        print(EstimatedShipping_label)
        self.assertEqual(self.actual43, EstimatedShipping_label)

    def test_shipping_price(self):
        ShippingPrice = self.cart_page.get_attribute(MiniCart.EstimatedShippingPrice, 'innerHTML')
        print(ShippingPrice)
        self.assertEqual(self.actual44, ShippingPrice)

    def test_minimum_charge(self):
        Minimum = self.cart_page.get_attribute(MiniCart.MinimumCharge, 'innerHTML')
        print(Minimum)
        self.assertEqual(self.actual45, Minimum)

    def test_minimum_price(self):
        MinimumPrice = self.cart_page.get_attribute(MiniCart.MinimumChargePrice, 'innerHTML')
        print(MinimumPrice)
        self.assertEqual(self.actual46, MinimumPrice)

    def test_package_handling(self):
        Package = self.cart_page.get_attribute(MiniCart.PackageHandling, 'innerHTML')
        print(Package)
        self.assertEqual(self.actual47, Package)

    def test_package_price(self):
        PackagePrice = self.cart_page.get_attribute(MiniCart.PackageHandlingPrice, 'innerHTML')
        print(PackagePrice)
        self.assertEqual(self.actual48, PackagePrice)

    def test_tip_label(self):
        Tip_label = self.cart_page.get_attribute(MiniCart.Tip, 'innerHTML')
        print(Tip_label)
        self.assertEqual(self.actual49, Tip_label)

    def test_tip_price(self):
        TipPrice = self.cart_page.get_attribute(MiniCart.TipPrice, 'innerHTML')
        print(TipPrice)
        self.assertEqual(self.actual50, TipPrice)

    def test_tipzero(self):
        self.cart_page.click_NoTIp()
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual71, OrderPrice)

    def test_tip5(self):
        self.cart_page.click_Tip5()
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual72, OrderPrice)

    def test_tipten(self):
        self.cart_page.click_Tip10()
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual73, OrderPrice)

    def test_tip15(self):
        self.cart_page.click_Tip15()
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual74, OrderPrice)

    def test_tip20(self):
        self.cart_page.click_Tip20()
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual75, OrderPrice)

    def test_estimated_order(self):
        self.cart_page.scroll_to_element(MiniCart.EstimatedOrder)
        EstimatedOrder = self.cart_page.get_attribute(MiniCart.EstimatedOrder, 'innerHTML')
        print(EstimatedOrder)
        self.assertEqual(self.actual51, EstimatedOrder)

    def test_estimated_order_price(self):
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual52, OrderPrice)

    def test_delivery_label(self):
        deliveryLabel = self.cart_page.get_attribute(MiniCart.DeliveryLabel, 'innerHTML')
        print(deliveryLabel)
        self.assertEqual(self.actual53, deliveryLabel)

    def test_ckhangeAddressLabel(self):
        ChangeAddress = self.cart_page.get_attribute(MiniCart.ChangeAddress, 'innerHTML')
        print(ChangeAddress)
        self.assertEqual(self.actual54, ChangeAddress)

    def test_estimatedDelivery(self):
        estimatedDelivery_label = self.cart_page.get_attribute(MiniCart.EstimatedDelivery, 'innerHTML')
        print(estimatedDelivery_label)
        self.assertEqual(self.actual57, estimatedDelivery_label)

    def test_label_delivery_notes(self):
        self.cart_page.scroll_to_element(MiniCart.DeliveryNotes)
        notes = self.cart_page.get_attribute(MiniCart.DeliveryNotes, 'innerHTML')
        print(notes)
        self.assertEqual(self.actual58, notes)

    def test_notes(self):
        self.cart_page.enter_notes("Please be on time")
        enternote = self.cart_page.get_attribute(MiniCart.Notes_text, 'value')
        print(enternote)
        self.assertEqual(self.actual59, enternote)

    def test_proceedToPayment(self):
        payment = self.cart_page.get_attribute(MiniCart.Payment, 'innerHTML')
        print(payment)
        self.assertEqual(self.actual60, payment)

    def test_eVoucher_invalid_coupon(self):
        self.cart_page.enter_eVoucher("12345")
        time.sleep(15)
        self.cart_page.click_apply()
        Invalid = self.cart_page.get_attribute(MiniCart.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual76, Invalid)


    def test_click_secondItemName(self):
        ItemName = self.cart_page.get_attribute(MiniCart.SecondItemName, 'innerHTML')
        print(ItemName)
        self.assertEqual(self.actual64, ItemName)

    def test_click_secondItemPrice(self):
        ItemPrice = self.cart_page.get_attribute(MiniCart.SecondItemPrice, 'innerHTML')
        print(ItemPrice)
        self.assertEqual(self.actual65, ItemPrice)

    def test_click_secondItemQuantity(self):
        self.cart_page.click_MiniCart()
        quantity = self.cart_page.get_attribute(MiniCart.SecondItemQuanitity, 'innerHTML')
        print(quantity)
        self.assertEqual(self.actual66, quantity)

    def test_paymentMethod1(self):
        self.cart_page.click_payment1()
        self.cart_page.click_Pay()
        ThankYouLabel = self.cart_page.get_attribute(MiniCart.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual77, ThankYouLabel)
        self.cart_page.click_quicklly()
        self.cart_page.submit_zip()
        # self.AddItem()
        time.sleep(5)
        self.cart_page.EnterSearch("lemon grass")
        self.cart_page.click_Search()
        time.sleep(5)
        self.cart_page.click_item()
        time.sleep(5)
        self.cart_page.EnterSearch("potato")
        self.cart_page.click_Search()
        time.sleep(5)
        self.cart_page.click_item2()
        time.sleep(2)
        self.cart_page.click_MiniCart()
        self.cart_page.click_Checkout()
        self.cart_page.click_Checkout2()
