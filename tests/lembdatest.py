import time
from selenium import  webdriver

def initiate_browser():
    print("starting")
    time.sleep(1)
    sign_in=driver.find_element_by_xpath('//*[@id="procedcheckoutBtn"]')
    sign_in.click()
    email=driver.find_element_by_xpath('//*[@id="user_email"]')
    email.send_keys('testaccount@quicklly.com')
    password=driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('123456')
    LogInbtn=driver.find_element_by_xpath('//*[@id="btn-login"]')
    LogInbtn.click()

    print('ending')


def calc_performance():
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)

    # driver.quit()

if __name__ == '__main__':
    hyperlink= "http://www.quicklly.com/"
    driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/pythonProject/chromedriver.exe")
    driver.get(hyperlink)

    initiate_browser()
    time.sleep(2)
    calc_performance()

    driver.quit()