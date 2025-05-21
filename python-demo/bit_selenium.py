import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


with open('窗口列表.html','r')as f:
    k = f.read()
    import json
    from bit_api import openBrowser
    import bit_api
    import time
    k = json.loads(k)
    num = 0
    for i in k:
        num += 1
        # openBrowser(i['id'])

        # /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
        res = openBrowser(i['id'])  # 窗口ID从窗口配置界面中复制，或者api创建后返回

        print(res)

        driverPath = res['data']['driver']
        debuggerAddress = res['data']['http']

        # selenium 连接代码
        chrome_options = webdriver.ChromeOptions()
        # chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)

        chrome_service = Service(driverPath)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        time.sleep(20)

        current_windows = driver.window_handles
        print(current_windows)
        driver.switch_to.window(current_windows[0])

        driver.refresh()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('magnesium gummies')
        driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

        driver.find_element(By.XPATH, '//*[@data-asin="B0BZNSXNZV"]/div//span/div/div/div[2]/div[1]/a').click()

        time.sleep(80)

        print('正在打开:' + i['id'])
        # time.sleep(20)
        if num == 5:
            break







# # 以下为PC模式下，打开baidu，输入 BitBrowser，点击搜索的案例
# driver.get('https://www.baidu.com/')
#
# input = driver.find_element(By.CLASS_NAME, 's_ipt')
# input.send_keys('BitBrowser')
#
# print('before click...')
#
# btn = driver.find_element(By.CLASS_NAME, 's_btn')
# btn.click()
#
# print('after click')


