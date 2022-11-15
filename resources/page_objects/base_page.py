# !/usr/bin/env python
import ftplib
import os
from datetime import datetime, timedelta

import time
from pathlib import Path

from lxml import html

import selenium
from common import env
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote

from resources.config_methods import DataClass
from resources.locators import CommonLocators


class BasePage:
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionality available to all pages."""

    admin_user = env.get_config_value('portal_ui', 'admin_user')
    admin_password = env.get_config_value('portal_ui', 'admin_password')
    base_url = env.get_config_value('portal_ui', 'base_url')
    # curr_user = env.get_config_value('portal_ui', 'curr_user')

    page_load_timeout = 200
    wait = 20
    driver: Remote = None

    # this function is called every time a new object of the base class is created.

    def __init__(self, driver):
        """

        :rtype: object
        """
        self.driver = driver

    @classmethod
    def get_browser_instance(cls):
        chrome_options = selenium.webdriver.ChromeOptions()
        for c in env.get_config_value('webdriver', 'options'):
            chrome_options.add_argument(c)
            chrome_options.add_argument("--no-sandbox")
            if os.environ.get('HEADLESS', False):
                chrome_options.add_argument("--headless")
        caps = selenium.webdriver.DesiredCapabilities.CHROME.copy()
        caps.update(env.get_config_value('webdriver', 'desired_capabilities'))
        driver = selenium.webdriver.Chrome(options=chrome_options, desired_capabilities=caps, executable_path="/root/Desktop/chromedriver_linux64/chromedriver")
        driver.implicitly_wait(20)
        driver.set_page_load_timeout(cls.page_load_timeout)
        driver.set_script_timeout(cls.page_load_timeout)
        return driver

    # @classmethod
    # def get_browser_instance(cls):
    #     chrome_options = selenium.webdriver.ChromeOptions()
    #     for c in env.get_config_value('webdriver', 'options'):
    #         chrome_options.add_argument(c)
    #         chrome_options.add_argument("--no-sandbox")
    #         if os.environ.get('HEADLESS', False):
    #             chrome_options.add_argument("--headless")
    #     caps = selenium.webdriver.DesiredCapabilities.CHROME.copy()
    #     caps.update(env.get_config_value('webdriver', 'desired_capabilities'))
    #     driver = selenium.webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
    #     driver.maximize_window()
    #     driver.implicitly_wait(20)
    #     driver.set_page_load_timeout(cls.page_load_timeout)
    #     driver.set_script_timeout(cls.page_load_timeout)
    #     return driver

    def capture_screen_shot(self):
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        name = datetime.strftime(datetime.now(), '%m-%d_%H-%M-%S')
        path = os.path.join('screenshots', f'screenshot{name}.png')
        print(path)
        self.driver.save_screenshot(path)

    # def capture_screen_shot(self):
    #     if not os.path.exists('screenshots'):
    #         os.makedirs('screenshots')
    #     name = datetime.strftime(datetime.now(), '%m-%d_%H-%M-%S')
    #     filename = os.path.join('screenshots', f'screenshot_{name}.png')
    #     print(filename)
    #     self.driver.save_screenshot(filename)
    #     #upload image
    #     file_path = Path(filename)
    #     FTP_HOST='anonymous'
    #     FTP_USER=''
    #     FTP_PASS=''
    #     ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    #     ftpfolderName=datetime.today().strftime('%Y%m%d')
    #     #create fodler if not exist
    #     if self.directory_exists(ftpfolderName, ftp) is False:
    #         ftp.mkd(ftpfolderName)
    #     with open(file_path, "rb") as file:
    #         ftp.storbinary(f"STOR /{ftpfolderName}/{file_path.name}", file)
    #     return f"http://www.dev.quicklly.com/automation_Images/{ftpfolderName}/{file_path.name}"

    def directory_exists(self, dir, ftp):
        filelist = []
        ftp.retrlines('LIST', filelist.append)
        return any(f.split()[-1] == dir and f.upper().startswith('D') for f in filelist)

    # this function performs click on web element whose locator is passed to it.
    def find_element(self, by_locator):
        try:
            # print (by_locator)
            WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))
            # time.sleep(2)
            # self.driver.switch_to
            return self.driver.find_element(*by_locator)
        except:
            print('@screenshot@')
            self.capture_screen_shot()
            raise

    def find_elements(self, by_locator):
        try:
            WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))
        except TimeoutException as e:
            print(e)

        # time.sleep(2)
        return self.driver.find_elements(*by_locator)

    def find_elements_by_xpath(self, by_locator):
        return self.find_elements(by_locator)

    def get_text(self, by_locator):
        return self.find_element(by_locator).text

    def get_text_from_list(self, by_locator, wait=False):
        element_list = self.find_elements(by_locator)
        element_text_list = []
        for element in element_list:
            element_text = element.text.strip('* \n')
            element_text_list.append(element_text)
            if wait:
                time.sleep(2)
        return element_text_list

    def get_attribute(self, by_locator, attr):
        return self.find_element(by_locator).get_attribute(attr)

    def get_text_field_value(self, by_locator):
        return self.find_element(by_locator).get_attribute('value')

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(by_locator)).click()
        except:
            self.capture_screen_shot()
            raise

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text, clear=False):
        element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator))
        if clear and element:
            element.clear()
        return element.send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_clickable(self, by_locator):
        return WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(by_locator))
        # return self.find_element(by_locator).is_enabled()

    def get_select(self, locator):
        return Select(self.find_element(locator))

    def select(self, by_locator, text):
        select = self.get_select(by_locator)
        # select by visible text
        return select.select_by_visible_text(text)

    def get_current_selected(self, by_locator):
        select = Select(self.find_element(by_locator))
        return select.first_selected_option.text.strip()

    def handle_alert_box(self):
        main_window = self.driver.current_window_handle
        # Switch the control to the Alert window
        obj = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        msg = obj.text.strip()
        print("Alert Message: " + msg)
        # use the accept() method to accept the alert
        obj.accept()
        print("Alert Accepted")
        self.driver.switch_to.window(main_window)
        return msg

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        try:
            elem = self.driver.find_element(*by_locator)
            return True
        except NoSuchElementException:
            print('Element with locator = "{}" is not available'.format(by_locator))
            return False

    def is_enabled(self, by_locator):
        if self.driver.find_element(*by_locator).is_enabled():
            return True
        else:
            print('Element with locator = "{}" is disabled'.format(by_locator))
            return False

    def is_displayed(self, by_locator):
        # elem = self.driver.find_element(*by_locator)
        # return elem.is_visi
        # return self.find_element(by_locator).is_displayed()
        return self.driver.find_element(by_locator).is_displayed()

    def is_selected(self, by_locator):
        return self.find_element(by_locator).is_selected()

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def make_function_for_table_data(self):
        pass

    def scroll_to(self, x, y):
        self.driver.execute_script("window.scrollTo(" + str(x) + "," + str(y) + ")")

    def scroll_to_element(self, by_locator):
        element = self.find_element(by_locator)
        location = element.location
        x = location['x'] / 2
        y = location['y'] / 2
        self.driver.execute_script("window.scrollTo(" + str(x) + "," + str(y) + ")")

    def hover(self, locator):
        try:
            element = self.find_element(locator)
            hov = ActionChains(self.driver).move_to_element(element)
            hov.perform()
        except BaseException as e:
            self.capture_screen_shot()
            raise

    def check_presence_of_element(self, by_locator):
        try:
            WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))
            return True
        except BaseException as e:
            return False

    def click_previous_page_button(self, by_locator):
        elem = self.check_presence_of_element(by_locator)
        if elem is True:
            self.click(by_locator)
            return True
        else:
            print("Previous page not found")
            return False

    def click_next_page_button(self, by_locator):
        elem = self.check_presence_of_element(by_locator)
        if elem:
            self.click(by_locator)
            return True
        else:
            print("Next page not found")
            return False

    def click_particular_page_button(self, page_no):
        locator = (By.XPATH, '//a[contains(@class, "ng-star-inserted") and child :: span[text()={}]]'.format(page_no))
        current_page = (By.XPATH, '//li[contains(@class, "current")]//span[not(contains(@class, "show-for"))]')
        current_page_no = self.get_text(current_page)
        elem = self.check_presence_of_element(locator)
        if str(page_no) == current_page_no:
            print("Already on required page")
            return
        else:
            if elem:
                self.click(locator)
            else:
                print("Required page not found")

    def get_toast_msg(self, by_locator):
        return self.get_text(by_locator)

    # this function will click on edit/delete/lock/unlock button for mentioned unique identifier
    def select_table_action_button(self, *identifiers, button, retries=5):
        required_row = ' and '.join('.//td[contains(., "{}")]'.format(v) for v in identifiers)
        required_button = '//tr[{}]'.format(required_row) + '//button[@popover="{}"]'.format(button)
        print(required_button)
        button_locator = (By.XPATH, required_button)
        for _ in range(retries):
            try:
                return self.click(button_locator)
            except BaseException as e:
                print(e)

    def select_table_checkbox(self, *identifiers, select, retries=5):
        """select may be True or False"""
        required_row = ' and '.join('.//td[contains(., "{}")]'.format(v) for v in identifiers)
        required_checkbox = '//tr[{}]'.format(required_row) + '//label//span'
        checkbox_locator = (By.XPATH, required_checkbox)
        # checkboxes = self.find_elements(checkbox_locator)
        # print(checkboxes)
        # for checkbox in checkboxes:
        # print(multiple)
        # if not multiple:
        for _ in range(retries):
            try:
                if select:
                    if not self.is_selected(checkbox_locator):
                        return self.click(checkbox_locator)
                else:
                    if self.is_selected(checkbox_locator):
                        return self.click(checkbox_locator)
            except BaseException as e:
                print(e)
        # else:
        #     select_all_locator = (By.XPATH, '//th//span')
        #     if select:
        #         if not self.is_selected(select_all_locator):
        #             return self.click(select_all_locator)
        #     else:
        #         if self.is_selected(select_all_locator):
        #             return self.click(select_all_locator)
        # self.click(select_all_locator)

    def select_all_table_checkboxes(self, select, retries=5):
        select_all_locator = (By.XPATH, '//th//span')
        # print(self.is_visible(select_all_locator))
        # print()
        if select:
            #     print(self.is_selected(select_all_locator))
            if not self.is_selected(select_all_locator):
                self.click(select_all_locator)
        #         print(self.is_selected(select_all_locator))
        else:
            if self.is_selected(select_all_locator):
                self.click(select_all_locator)
        # for _ in range(retries):
        #     try:
        #         if select:
        #             # if not self.is_selected(select_all_locator):
        #             while not self.is_selected(select_all_locator):
        #                 print(self.is_selected(select_all_locator))
        #                 return self.click(select_all_locator)
        #         else:
        #             if self.is_selected(select_all_locator):
        #                 return self.click(select_all_locator)
        #     except BaseException as e:
        #         print(e)

    # def select_from_table_ellipsis_menu(self, *identifiers, option, retries=5):
    def select_from_table_ellipsis_menu(self, *identifiers, retries=5):
        required_identifiers = ' and '.join('.//td[contains(., "{}")]'.format(v) for v in identifiers)
        required_row = '//tr[{}]'.format(required_identifiers)
        required_ellipsis_menu = required_row + '//span[contains(@class, "ellipsis")]//..'
        menu_open = required_ellipsis_menu + '/..'
        ellipsis_menu_locator = (By.XPATH, required_ellipsis_menu)
        menu_open_locator = (By.XPATH, menu_open)
        for _ in range(retries):
            try:
                self.click(ellipsis_menu_locator)
                attr = self.get_attribute(menu_open_locator, 'class')
                if 'open' in attr:
                    break
                time.sleep(3)
            except BaseException as e:
                print(e)
        # self.click(ellipsis_menu_locator)
        # option_locator = (
        #     By.XPATH, required_ellipsis_menu + '/following-sibling::ul//li[contains(.,"{}")]'.format(option)
        # )
        option_locator = (By.XPATH, '//popover-container//li')
        for _ in range(retries):
            try:
                if self.is_visible(option_locator):
                    return self.click(option_locator)
            except BaseException as e:
                print(e)

    def wait_for_loader(self, timeout=10, loader_locator=CommonLocators.main_loader):
        # start_time = datetime.now()
        # if not self.is_visible(loader_locator):
        #     end_time = start_time + timedelta(seconds=timeout-8)
        #     while datetime.now() < end_time:

        if loader_locator == CommonLocators.sub_page_loader:
            start_time = datetime.now()
            end_time = start_time + timedelta(seconds=timeout)
            while datetime.now() < end_time:
                attr = self.get_attribute(loader_locator, 'class')
                if 'hide' in attr:
                    return True
                time.sleep(0.5)
            return False
        if self.is_visible(loader_locator):
            self.wait_for_absence(loader_locator)

        # start_time = datetime.now()
        # end_time = start_time + timedelta(seconds=timeout)
        # if self.is_visible(loader_locator):
        #     while datetime.now() < end_time:
        #         if not self.is_visible(loader_locator):
        #             return True
        #         time.sleep(0.5)
        # if loader_locator == Database.spinner:
        #     while datetime.now() < end_time:
        #         attr = self.get_attribute(loader_locator, 'class')
        #         if 'hide' in attr:
        #             return True
        #         time.sleep(0.5)
        #     return False
        # self.wait_for_absence(loader_locator)
        #     attr = self.get_attribute(spinner_locator, 'class')
        #     if 'hide' in attr:
        #         return True

        # return False

        # while 'hide' not in attr:
        #     time.sleep(0.5)

        # if 'hide' in attr:
        #     return True
        # else:
        #     return False

    def wait_for_page_load(self, by_locator, timeout=60):
        # self.wait_for_absence((By.XPATH, '//button[@disabled]'))
        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=timeout)

        while not self.is_clickable(by_locator) and datetime.now() < end_time:
            time.sleep(0.5)

    def wait_for_presence(self, by_locator, wait=None, re_raise=True, screenshot=True):
        if wait is None:
            wait = self.wait
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException as e:
            print('Waited [{}s] for "{}"'.format(wait, by_locator))
            if screenshot:
                print(e)
                self.capture_screen_shot()
            if re_raise:
                raise
        return False

    def wait_for_absence(self, by_locator, wait=None):
        if wait is None:
            wait = self.wait
        try:
            WebDriverWait(self.driver, wait).until(EC.invisibility_of_element(by_locator))
            return True
        except BaseException as e:
            self.capture_screen_shot()
            raise
        # return False

    def upload_file(self, by_locator, path):
        return self.find_element(by_locator).send_keys(path)

        # if not self.find_elements(*by_locator):
        #     pass
        # else:
        #     if wait is None:
        #         wait = self.wait
        #     WebDriverWait(self.driver, wait).until(EC.invisibility_of_element(by_locator))
        # #
        # try:
        #     element = self.driver.find_element(*by_locator)
        #     if wait is None:
        #         wait = self.wait
        #     WebDriverWait(self.driver, wait).until(EC.invisibility_of_element(by_locator))
        # except NoSuchElementException:
        #     print("!!!")
        #     pass

    def close_popup_msg(self, retries=5):
        print('Closing Pop-up Messages')
        closed = 0
        for _ in range(retries):
            try:
                elems = self.find_elements(
                    (By.XPATH, '//*[local-name()="global-messages"]//button[@aria-label="Close"]//span')
                )
                if not elems:
                    break
                list(e.click() for e in elems)
                closed += len(elems)
            except BaseException as e:
                pass
        if closed:
            print('Closed Pop-ups: {}'.format(closed))

    def get_global_alert_msg(self):
        """
        Return tuple of all popup messages available on UI
        :return:
        """
        found = self.wait_for_presence(
            (By.XPATH, '//*[local-name()="global-messages"]//div[contains(@class,"alert-")]'), re_raise=False
        )
        if found:
            text = self.find_element((By.XPATH, '//*[local-name()="global-messages"]')).get_attribute('innerHTML')
            o = html.fromstring(text)
            m = o.xpath('//div[contains(@role,"alert")]')
            return tuple(''.join([y for y in x.itertext() if y.strip()]).strip('×\n') for x in m)
        return ()

    def get_ng_dropdown_panel(self, label=''):
        self._ng_open(label)
        locator = (By.XPATH, '//div[contains(@class, "ng-dropdown-panel-items")]')

        found = self.wait_for_presence(locator, re_raise=False)
        if found:
            o = html.fromstring(self.find_element(locator).get_attribute('innerHTML'))
            options = tuple(x.text for x in o.xpath('//div[@role="option"]//span'))
            print(type(options))
            return options
        return ()

    def ng_select(self, label, text):
        xp = (By.XPATH, '//label[contains(text(), "{}")]/following-sibling::div//ng-select'.format(label))
        print(xp)
        self.click(xp)
        text_xp = "//ng-dropdown-panel//span[contains(text(),'{}')]".format(text)
        print(text_xp)
        return self.click((By.XPATH, text_xp))

    def ng_select_without_label(self, placeholder, text):
        xp = (By.XPATH, '//ng-select[@placeholder="{}"]'.format(placeholder))
        print(xp)
        self.click(xp)
        text_xp = "//div[contains(@class,'ng-dropdown-pane')]//div//div//div[@title='{}']".format(text)
        print(text_xp)
        return self.click((By.XPATH, text_xp))
        # text_xp = "//div[contains(@class,'ng-dropdown-pane')]//div//div//div[@title='{}']".format(text)
        # print(text_xp)
        # return self.click((By.XPATH, text_xp))

    def ng_value(self, id):
        elem = (By.XPATH, '//ng-select[contains (@id,"{}")]//div[contains(@class, "ng-value")]//span[contains ('
                          '@class, "ng-value-label")]'.format(id))
        value = self.get_text(elem)
        print(value)
        return value

    def _ng_open(self, label='', retries=3):
        xp = "//div[text()='{}']//ancestor::div/*[local-name()='ng-select']".format(label)
        locator = (By.XPATH, xp)
        is_open = lambda: 'ng-select-opened' in self.find_element(locator).get_attribute('class')
        while not is_open() and retries > -1:
            self.click(locator)
            if is_open():
                break
            retries -= 1

    def wait_for_ui_stabilize(self, locator, timeout=10):
        now = datetime.now
        end_time = now() + timedelta(seconds=timeout)
        text = lambda: self.get_attribute(locator, 'innerHTML')
        _prev = text()
        while now() < end_time:
            time.sleep(0.5)
            _new = text()
            if _prev == _new:
                break
            _prev = _new
