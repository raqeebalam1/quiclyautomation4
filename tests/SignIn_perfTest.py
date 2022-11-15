import time
from selenium import  webdriver

def initiate_browser():
    print("starting")
    ZipCode=driver.find_element_by_xpath('//*[@id="zipcode"]')
    ZipCode.send_keys('60611')
    time.sleep(10)
    Submitbtn=driver.find_element_by_xpath('//*[@id="zipsubmitbtn"]')
    Submitbtn.click()
    print('ending')


def calc_performance():
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    # backendPerformance_calc = responseStart
    # frontendPerformance_calc = domComplete
    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)

    # driver.quit()

if __name__ == '__main__':
    hyperlink= "http://uat.goquicklly.com/"
    driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/pythonProject/chromedriver.exe")
    driver.get(hyperlink)

    initiate_browser()
    time.sleep(2)
    calc_performance()

    driver.quit()