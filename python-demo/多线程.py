import threading,multiprocessing
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



res_list = []
def open_brower(i):
    # /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
    res = openBrowser(i)  # 窗口ID从窗口配置界面中复制，或者api创建后返回
    res_list.append(res)

    print(res)
    # print(res_list)



def print_numbers():
    for i in range(1,10000):
        print('第一')
        # time.sleep(2)

# 窗口打开
with open('窗口列表.html','r')as f:
    k = f.read()
    import json
    from bit_api import openBrowser
    import bit_api
    import time
    k = json.loads(k)
    num = 0
    process = []
    for i in k:
        num += 1
        # print('正在打开:' + i['id'])

        thread1 = threading.Thread(target=open_brower(i['id']), daemon=True)
        # thread1 = multiprocessing.Process(target=open_brower(i['id']))
        # thread1 = threading.Thread(target=print_numbers)
        # thread1 = multiprocessing.Process(target=print_numbers)
        process.append(thread1)
        thread1.start()
        if num == 1:
            break

    for p in process:
        p.join()


# 浏览器自动操作
def auto_brower(res):
    driverPath = res['data']['driver']
    debuggerAddress = res['data']['http']

    # selenium 连接代码
    chrome_options = webdriver.ChromeOptions()
    # chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)


    chrome_service = Service(driverPath)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # time.sleep(20)
    # time.sleep(2)

    current_windows = driver.window_handles
    print(current_windows)
    driver.switch_to.window(current_windows[0])

    driver.refresh()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(Keys.CONTROL,'a')
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('magnesium gummies')
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    time.sleep(3)
    # driver.refresh()
    #设置等待时间
    wait = WebDriverWait(driver,100)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@data-asin="B0CBVZ9B2G"]/div//span/div/div/div[2]/div[*]/a')))
        # element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@data-asin="B078KJLT6G"]/div//span/div/div/div[2]/div[1]/a')))
    except NameError as e:
        # print('未找到元素')
        print(e)
        driver.close()
        exit()
    driver.find_element(By.XPATH, '//*[@data-asin="B0CBVZ9B2G"]/div//span/div/div/div[2]/div[1]/a').click()
    time.sleep(3)



print('打开VPN------')
time.sleep(3)
process_brower = []
for res in res_list:
    thread1 = threading.Thread(target=auto_brower(res), daemon=True)
    process_brower.append(thread1)
    thread1.start()




# for i in range(2):
#     thread1 = threading.Thread(target=print_numbers,daemon=True)
#     thread1.start()
#


