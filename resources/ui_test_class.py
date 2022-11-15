#!/usr/bin/env python

import unittest
import pprint
import time
from resources.config_methods import DataClass
from resources.common_methods import Common

from resources.page_objects.base_page import BasePage
from resources.page_objects.LogIn import Login
from resources.page_objects.diwali import DiwaliGift
from resources.page_objects.guest import guest
from resources.page_objects.needaccount import needanaccount
from resources.page_objects.forgetpassword import forgetpass
from resources.page_objects.cart import Cart
from resources.page_objects.eVoucher import evoucher
from resources.page_objects.department import Dept
from resources.page_objects.Zipcodes import Zip
from resources.page_objects.contact_us import contactUs
from resources.page_objects.signup import signUp
from resources.page_objects.refer import ReferAFriend
from resources.page_objects.category import GroceryCategories
from resources.page_objects.link import ContactUsLinks
from resources.page_objects.guestCheckout_page import CheckoutWithGuest
from resources.page_objects.invalid import InvalidZipcodes
from resources.page_objects.guestlogin import LoginAsGuest
from resources.page_objects.payment import Pay
from resources.page_objects.SignUpCheckout_page import SUC
from resources.page_objects.chaiDepartment import CACD
from resources.page_objects.mealkit import Meal
from resources.page_objects.indianseasoningkit import Indian
from resources.page_objects.indiangrocerybox import IndianGrocery
from resources.page_objects.rotikit import RotiBox
from resources.page_objects.indianmeal import IndianMeal
from resources.page_objects.IndianSauces import Sauces
from resources.page_objects.bbq import BBQKIT
from resources.page_objects.onetime_page import ONETIME
from resources.page_objects.weekly_page import WEEKLY
from resources.page_objects.biweekly_page import BIWEEKLY
from resources.page_objects.monthly_page import MONTHLY
from resources.page_objects.max_page import MAXIMUM
from resources.page_objects.edit_page import EDITITEM
from selenium.webdriver import Remote


# from client.auto_it_methods import AutoIt


class UIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    base_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIClass, cls).setUpClass()
        cls.base_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.base_page.get_browser_instance()
        cls.base_page.driver = cls.driver
        cls.maine_page = Login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIClass, cls).tearDownClass()


class UIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    guest_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIClass, cls).setUpClass()
        cls.guest_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.guest_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.guest_page.driver = cls.driver
        cls.guest_page = guest(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIClass, cls).tearDownClass()


class UIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    need_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIIClass, cls).setUpClass()
        cls.need_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.need_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.need_page.driver = cls.driver
        cls.need_page = needanaccount(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIIClass, cls).tearDownClass()


class UIIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    forget_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIIIClass, cls).setUpClass()
        cls.forget_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.forget_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.forget_page.driver = cls.driver
        cls.forget_page = forgetpass(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIIIClass, cls).tearDownClass()


class UVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    cart_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVClass, cls).setUpClass()
        cls.cart_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.cart_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.cart_page.driver = cls.driver
        cls.cart_page = Cart(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVClass, cls).tearDownClass()


class UVIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    eVoucher_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIClass, cls).setUpClass()
        cls.eVoucher_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.eVoucher_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.eVoucher_page.driver = cls.driver
        cls.eVoucher_page = evoucher(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIClass, cls).tearDownClass()


class UVIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    depart_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIIClass, cls).setUpClass()
        cls.depart_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.depart_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.depart_page.driver = cls.driver
        cls.depart_page = Dept(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        super(UVIIClass, cls).tearDownClass()


class UVIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    zip_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIIIClass, cls).setUpClass()
        cls.zip_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.zip_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.zip_page.driver = cls.driver
        cls.zip_page = Zip(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIIIClass, cls).tearDownClass()


class UVIXClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    contact_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIXClass, cls).setUpClass()
        cls.contact_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.contact_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.contact_page.driver = cls.driver
        cls.contact_page = contactUs(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIXClass, cls).tearDownClass()


class UVXClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    signup_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXClass, cls).setUpClass()
        cls.signup_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.signup_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.signup_page.driver = cls.driver
        cls.signup_page = signUp(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXClass, cls).tearDownClass()


class UVXIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    refer_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXIClass, cls).setUpClass()
        cls.refer_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.refer_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.refer_page.driver = cls.driver
        cls.refer_page = ReferAFriend(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXIClass, cls).tearDownClass()


class UVXIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    guestCheckout_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXIIClass, cls).setUpClass()
        cls.guestCheckout_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.guestCheckout_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.guestCheckout_page.driver = cls.driver
        cls.guestCheckout_page = CheckoutWithGuest(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXIIClass, cls).tearDownClass()


class UVXIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    category_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXIIIClass, cls).setUpClass()
        cls.category_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.category_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.category_page.driver = cls.driver
        cls.category_page = GroceryCategories(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXIIIClass, cls).tearDownClass()

class UVXIVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    link_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXIVClass, cls).setUpClass()
        cls.link_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.link_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.link_page.driver = cls.driver
        cls.link_page = ContactUsLinks(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXIVClass, cls).tearDownClass()

class UVXVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    invalid_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVClass, cls).setUpClass()
        cls.invalid_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.invalid_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.invalid_page.driver = cls.driver
        cls.invalid_page = InvalidZipcodes(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVClass, cls).tearDownClass()

class UVXVIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    guestLogin_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVIClass, cls).setUpClass()
        cls.guestLogin_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.guestLogin_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.guestLogin_page.driver = cls.driver
        cls.guestLogin_page = LoginAsGuest(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVIClass, cls).tearDownClass()

class UVXVIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    payment_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVIIClass, cls).setUpClass()
        cls.payment_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.payment_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.payment_page.driver = cls.driver
        cls.payment_page = Pay(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVIIClass, cls).tearDownClass()

class UVXVIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    signupcheckout_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVIIIClass, cls).setUpClass()
        cls.signupcheckout_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.signupcheckout_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.signupcheckout_page.driver = cls.driver
        cls.signupcheckout_page = SUC(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVIIIClass, cls).tearDownClass()

class UVXVIXClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    chai_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVIXClass, cls).setUpClass()
        cls.chai_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.chai_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.chai_page.driver = cls.driver
        cls.chai_page = CACD(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVIXClass, cls).tearDownClass()

class UVXVXClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    meal_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXClass, cls).setUpClass()
        cls.meal_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.meal_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.meal_page.driver = cls.driver
        cls.meal_page = Meal(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXClass, cls).tearDownClass()

class UVXVXIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    indian_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXIClass, cls).setUpClass()
        cls.indian_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.indian_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.indian_page.driver = cls.driver
        cls.indian_page = Indian(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXIClass, cls).tearDownClass()

class UVXVXIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    grocerybox_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXIIClass, cls).setUpClass()
        cls.grocerybox_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.grocerybox_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.grocerybox_page.driver = cls.driver
        cls.grocerybox_page = IndianGrocery(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXIIClass, cls).tearDownClass()

class UVXVXIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    roti_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXIIIClass, cls).setUpClass()
        cls.roti_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.roti_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.roti_page.driver = cls.driver
        cls.roti_page = RotiBox(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXIIIClass, cls).tearDownClass()

class UVXVVXIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    diwali_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVVXIIIClass, cls).setUpClass()
        cls.diwali_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.diwali_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.diwali_page.driver = cls.driver
        cls.diwali_page = DiwaliGift(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVVXIIIClass, cls).tearDownClass()


class UVXVXIVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    mealkit_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXIVClass, cls).setUpClass()
        cls.mealkit_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.mealkit_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.mealkit_page.driver = cls.driver
        cls.mealkit_page = IndianMeal(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXIVClass, cls).tearDownClass()

class UVXVXVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    sauces_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVClass, cls).setUpClass()
        cls.sauces_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.sauces_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.sauces_page.driver = cls.driver
        cls.sauces_page = Sauces(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVClass, cls).tearDownClass()

class UVXVXVIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    bbq_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVIClass, cls).setUpClass()
        cls.bbq_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.bbq_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.bbq_page.driver = cls.driver
        cls.bbq_page = BBQKIT(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVIClass, cls).tearDownClass()

class UVXVXVIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    one_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVIIClass, cls).setUpClass()
        cls.one_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.one_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.one_page.driver = cls.driver
        cls.one_page = ONETIME(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVIIClass, cls).tearDownClass()

class UVXVXVIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    weekly_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVIIIClass, cls).setUpClass()
        cls.weekly_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.weekly_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.weekly_page.driver = cls.driver
        cls.weekly_page = WEEKLY(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVIIIClass, cls).tearDownClass()

class UVXVXVIVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    biweekly_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVIVClass, cls).setUpClass()
        cls.biweekly_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.biweekly_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.biweekly_page.driver = cls.driver
        cls.biweekly_page = BIWEEKLY(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVIVClass, cls).tearDownClass()

class UVXVXVVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    monthly_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVVClass, cls).setUpClass()
        cls.monthly_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.monthly_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.monthly_page.driver = cls.driver
        cls.monthly_page = MONTHLY(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVVClass, cls).tearDownClass()

class UVXVXVVIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    max_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVVIClass, cls).setUpClass()
        cls.max_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.max_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.max_page.driver = cls.driver
        cls.max_page = MAXIMUM(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVVIClass, cls).tearDownClass()

class UVXVXVVIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    edit_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVXVXVVIIClass, cls).setUpClass()
        cls.edit_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.edit_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.edit_page.driver = cls.driver
        cls.edit_page = EDITITEM(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVXVXVVIIClass, cls).tearDownClass()

    @classmethod
    def login(cls):
        pass

    # return cls.login_page.login(cls.login_page.admin_user, cls.login_page.admin_password)

    @classmethod
    def logout(cls):
        pass

    # return cls.home_page.logout()

    @staticmethod
    def display_bug(_id, desc=None):
        if desc:
            print(desc)
            print('bug link{}'.format(_id))

    @staticmethod
    def pprint(arg):
        print(pprint.pformat(arg))

    @staticmethod
    def sleep(arg):
        time.sleep(arg)
