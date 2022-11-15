import time
from resources import ui_test_class
from resources.locators import ZipCode
from resources.page_objects.Zipcodes import Zip
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TesZIPCODES(ui_test_class.UVIIIClass):
    zip_page: Zip
    zip_page: ZipCode
    depart = {}
    dict = {}

    @classmethod
    def setUpClass(cls):
        super(TesZIPCODES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesZIPCODES, cls).tearDownClass()
        cls.driver.quit()

    def Excel_Data(self):
        arr1 = []

        data = pd.read_excel('Data/123.xls')
        dict = data.to_dict()
        print(dict)

        # for x in range(24):
        #     df = pd.DataFrame(data, columns=['ZipCodes']).values[x]
        #     text9 = df
        #     self.zip_page.zip(df)
        #     self.zip_page.submit_zip()

            # try:
            #     WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            #     alert = self.driver.switch_to.alert
            #     alert.accept()
            #     print("alert Exists in page")
            # except TimeoutException:
            #     print("alert does not Exist in page")
            # time.sleep(2)
            # self.zip_page.click_department()
            # html_list = self.driver.find_element_by_xpath(
            #     '//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/div/div/ul')
            # items = html_list.find_elements_by_xpath("li")
            # for item in items:
            #     text = item.get_attribute('textContent')
            #     my_list2 = {text: 'depart'}
            #     my_list2 = {k.translate({32: None}): v for k, v in my_list2.items()}
            #     my_list2 = {key.strip(): item.strip() for key, item in my_list2.items()}
            #     lis = list(my_list2.keys())
            #     arr1.append(lis)
            #
            # if len(arr1) == 8:
            #     join = arr1[0] + arr1[1] + arr1[2] + arr1[3] + arr1[4] + arr1[5] + arr1[6] + arr1[7]
            # else:
            #     join = arr1[0] + arr1[1] + arr1[2] + arr1[3] + arr1[4] + arr1[5] + arr1[6]
            # print(join)
            #
            # value1 = pd.DataFrame(data, columns=['Shops']).values[x]
            # list1 = [value1][0]
            # string_version = "".join(list1)
            # txt = string_version.split(",")
            # print(txt)
            # if join == txt:
            #     text9 = "".join(text9)
            #     self.depart[text9] = True
            # else:
            #     text9 = "".join(text9)
            #     self.depart[text9] = False
            #
            # print(self.depart)
            # self.assertTrue(all(self.depart.values()), self.depart)
            # self.assertEqual( {'60070': False}, self.depart)
            # self.depart = {}
            # arr1 = []
            # self.zip_page.click_quicklly()



    def test_EnterZipCode(self):
        self.Excel_Data()
