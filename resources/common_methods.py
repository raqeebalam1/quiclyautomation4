import os
import platform
import shutil
import time
import pprint
from datetime import datetime, timedelta
from glob import glob
from zipfile import ZipFile
from lxml import html

from resources.page_objects.base_page import BasePage
import psutil

from resources.page_objects.privacy_error import PrivacyError
from resources.locators import CommonLocators
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By

class Common:

    driver: Remote = None

    def __init__(self, driver):
        self.driver = driver
        self.basePage = BasePage(driver)

    def in_case_of_fire(self, driver):
        privacyError = PrivacyError(driver)
        privacyError.click_advanced_button()
        privacyError.open_proceed_link()

    def get_path_cwd(self, file_name):
        return os.path.join(os.getcwd() + file_name)

    def get_downloads_directory(self):
        os_platform = platform.system()
        if os_platform == 'Windows' or os_platform == 'Linux':
            return os.path.expanduser(os.path.join('~', 'Downloads'))
        elif os_platform == 'Darwin':
            pass
        else:
            print('Unrecognized operating system.')

    def get_executable_path(self, executable_name=''):
        if platform.system() == 'Windows':
            if platform.architecture()[0] == '64bit':
                return os.path.join(os.path.expandvars('%programfiles(x86)%'), 'Invisily', executable_name)
            elif platform.architecture()[0] == '32bit':
                return os.path.join(os.path.expandvars('%programfiles%'), 'Invisily', executable_name)
        elif platform.system() == 'Linux':
            pass
        elif platform.system() == 'Darwin':
            pass
        else:
            print('Unrecognized operating system.')

    def get_file_from_directory(self, dir_path, substring):
        files_in_dir = [f for f in os.listdir(dir_path) if os.path.exists(os.path.join(dir_path, f))]
        req_files = []
        for each_file in files_in_dir:
            if substring in each_file:
                req_files.append(os.path.join(dir_path, each_file))
        return req_files

    def delete_file_or_folder(self, items):
        if not items:
            pass
        else:
            for item in items:
                if os.path.isfile(item):
                    os.remove(item)
                elif os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    raise ValueError(f'file {item} is not a file or dir')

    def check_for_existence(self, path, timeout, substr):
        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=timeout)
        while datetime.now() < end_time:
            if self.get_file_from_directory(path, substr):
                return True
            time.sleep(0.5)
        return False

    def check_for_absence(self, path, timeout, substr):
        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=timeout)
        while datetime.now() < end_time:
            if not self.check_for_existence(path, timeout, substr):
                return True
            time.sleep(0.5)
            # if self.check_for_existence(path, timeout, substr):
            #     pass
            # else:
            #     return True
        return False

    def check_file_by_substring(self, dir_path, substring, action=None):

        # time.sleep(1)
        if action == 'remove':
            items = self.get_file_from_directory(dir_path, substring)
            self.delete_file_or_folder(items)
        else:
            return self.check_for_existence(dir_path, 30, substring)
        return False

    def get_newest_file_in_downloads_dir(self):
        path = os.path.join(self.get_downloads_directory(), '*')
        # print(path)
        files = glob(path)
        # print(files)
        latest_file = max(files, key=os.path.getctime)
        # print(latest_file)
        return latest_file


    def get_table_headings(self, by_locator):
        return self.basePage.get_text_from_list(by_locator)

    def get_table_rows(self, by_locator):
        # def chunks(lst, n):
        #     """Yield successive n-sized chunks from lst."""
        #     for i in range(0, len(lst), n):
        #         yield tuple(lst[i:i + n])
        #         yield '<br />'

        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        headings = len(self.get_table_headings(by_locator))
        # print len(headings)
        time.sleep(2)
        elements = self.basePage.get_text_from_list(by_locator)
        list_of_rows = list(chunks(elements, headings))
        return list_of_rows

    def get_table_data(self, by_locator_headings, by_locator_rows):
        headings = self.get_table_headings(by_locator_headings)
        # time.sleep(2)
        rows = self.get_table_rows(by_locator_rows)
        print('headings', pprint.pformat(headings))
        print('rows', pprint.pformat(rows))
        return rows

    def fetch_table_data(self, is_visible=True, multiple_tables=False, table_no=None):
        all_data = []
        # Get headings
        if multiple_tables:
            # elems = self.basePage.find_elements(CommonLocators.heading_xpath.format(index))
            elems = self.basePage.find_elements_by_xpath((By.XPATH, CommonLocators.heading_xpath.format(table_no)))
            # print(elems)
        else:
            elems = self.basePage.find_elements_by_xpath(CommonLocators.xpath_head)
        heads = tuple(x.text for x in elems)
        # print(heads)
        col_len = len(heads)
        # print(col_len)

        is_vsble = is_visible
        if multiple_tables:
            table_locator = (By.XPATH, CommonLocators.table_xpath.format(table_no))
            # print(table_locator)
        else:
            table_locator = CommonLocators.table
        self.basePage.wait_for_ui_stabilize(table_locator, 5)
        if is_vsble:
            while is_vsble:
                self.basePage.wait_for_ui_stabilize(table_locator, 5)
                if multiple_tables:
                    tr_xpath = '(.//tbody)[{}]//tr[not(contains(@class, "fallback-text"))]'.format(table_no)
        #             # print(tr_xpath)
                else:
                    tr_xpath = './/tbody//tr[not(contains(@class, "fallback-text"))]'
                rows = self.get_rows(table_locator, col_len, tr=tr_xpath)
                # print(rows)
                for row in rows:
                    fields = row
                    di = {}
                    for key, val in zip(heads, fields):
                        di[key] = val.strip()
                    all_data.append(di)
                if multiple_tables:
                    next_page_locator = (By.XPATH, CommonLocators.next_page_xpath.format(table_no))
        #             # print(next_page_locator)
                else:
                    next_page_locator = CommonLocators.next_page
                is_vsble = (bool(self.basePage.find_elements_by_xpath(next_page_locator))
                            and self.basePage.is_visible(next_page_locator))
                print(is_vsble)
                if is_vsble:
                    self.basePage.click(next_page_locator)
                    # time.sleep(1)
        else:
            self.basePage.wait_for_ui_stabilize(table_locator, 5)
            rows = self.get_rows(table_locator, col_len)
            # print(' !!! ')
            # print(rows)
            # print(' !!! ')
            for row in rows:
                fields = row
                di = {}
                for key, val in zip(heads, fields):
                    di[key] = val.strip()
                all_data.append(di)
        return all_data

    def get_rows(self, xpath, col_len, tr='.//tr', td='.//td'):
        obj = html.fromstring(self.basePage.find_element(xpath).get_attribute('innerHTML'))
        rows = ()
        for row in obj.xpath(tr):
            tds = row.xpath(td)
            if len(tds) != col_len:
                continue
            rows += tuple(' '.join(y.strip() for y in x .itertext()).strip() for x in tds),

        return rows

    def get_heading(self):
        return self.basePage.get_text(CommonLocators.main_heading)
