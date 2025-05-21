import concurrent.futures
import datetime
import tkinter as tk
import single
import random
import multiprocessing
from multiprocessing import freeze_support
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




# 关闭所有窗口
def CLOSE_RESULT(id):
    CLOSE_RESULT = single.closeBrowser(id)
    # print(f'窗口:{id}关闭成功')
    # print(f'关闭结果:\n{CLOSE_RESULT}')


# 打开窗口并执行步骤
def kk(resp,send_keys,asins):
    # print(f'打开结果:\n{resp}')
    chrome_driver = resp["data"]["webdriver"]
    service = Service(executable_path=chrome_driver)
    chrome_options = Options()

    chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 标签页切换
    current_windows = driver.window_handles
    # print(current_windows)
    driver.switch_to.window(current_windows[0])
    # time.sleep(1)

    for asin in asins:
        for send_key in send_keys:
            # 搜索
            if  do(driver,send_key) == False:
                # 刷新
                driver.refresh()
                num = random.uniform(2,3)
                time.sleep(num)
                do(driver,send_key)
                time.sleep(3)
            # asin搜索
            if search_asin1(driver,asin) == False:
                # if search_asin2(driver,asin) == False:
                    continue
            time.sleep(1)
            # 使用JavaScript滚动到特定坐标
            driver.execute_script("window.scrollTo(0, 10000);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, -10000);")

            if search_asin2(driver) == False:
                continue



# 执行点击
def do(driver,send_key):
    try:
        num = random.uniform(2, 3)
        time.sleep(num)
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(f'{send_key}')
        num = random.uniform(2, 3)
        time.sleep(num)
        driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(Keys.ENTER)
        num = random.uniform(3, 4)
        time.sleep(num)
        # 使用JavaScript滚动到特定坐标
        driver.execute_script("window.scrollTo(0, 10000);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, -10000);")

    except:
        return False

# 执行search_asin1点击
def search_asin1(driver,asin):
    try:
        num = random.uniform(4, 5)
        time.sleep(num)
        driver.find_element(By.XPATH, f'//*[@data-asin="{asin}"]/div//span/div/div/div[2]/div[*]/a|//*[@data-asin="{asin}"]/div//span/div/div/div[*]/div[*]/span[@class="rush-component"]/div/a').click()
    except:
        return False



# 执行search_asin2点击
def search_asin2(driver):
    try:
        num = random.uniform(4, 5)
        time.sleep(num)
        driver.find_element(By.XPATH, f'//*[@id="add-to-cart-button"]').click()
    except:
        return False




def main(ID_lists,send_keys,asins):
    # 建立线程池
    pool = ThreadPoolExecutor(max_workers=10)
    resps = []
    start = time.time()

    for i in range(0, len(ID_lists), 5):
        A = False
        k = ID_lists[i:i + 5]
        # 打开
        for id in k:
            resp = single.openBrowser(id)
            resps.append(resp)
        futures = [pool.submit(lambda cxp:kk(*cxp),(resp,send_keys,asins)) for resp in resps]
        for future in futures:
            try:
                future_result = future.result(timeout=(330))
            except:
                # 关闭
                A = True
                for id in k:
                    CLOSE_RESULT(id)
        concurrent.futures.wait(futures) # 等待子线程完成不执行主线程
        resps = []
        if A == False:
            for id in k:
                CLOSE_RESULT(id)

    end = time.time()
    print('本次用时:', end - start)


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)



def Main():
    # 建立线程池
    # pool = ProcessPoolExecutor(max_workers=1)
    ID_lists = getEntry1()
    send_keys = getEntry2()
    asins = getEntry3()
    if len(ID_lists) == 0:
        insertEntry('\n请输入ID!')
    elif len(send_keys) > 5 or len(send_keys) == 0:
        insertEntry('\n搜索词空或大于5个!')
    elif len(asins) > 5 or len(send_keys) == 0:
        insertEntry('\nAsin空或大于5个！')
    else:
        insertEntry(datetime.datetime.now().strftime('\n%Y-%m-%d  %H:%M:%S'))
        insertEntry('\n*****正在打开*****')
        main(ID_lists, send_keys, asins)
    # pool.submit(main(ID_lists,send_keys,asins))

# UI 界面设计
def getEntry1():
    string = entry1.get('0.0', 'end')  # 获取Entry的内容
    return string.split()

def getEntry2():
    string = entry2.get('0.0', 'end')  # 获取Entry的内容
    k = string.split()
    return k

def getEntry3():
    string = entry3.get('0.0', 'end')  # 获取Entry的内容
    return string.split()


def insertEntry(massage):
    entry4.insert('end', f'{massage}')




font = ('微软雅黑', 12)

root = tk.Tk()

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 确定窗口位置，并设置大小
x_coordinate = (screen_width / 2) - 500  # 窗口宽度一半
y_coordinate = (screen_height / 2) - 350  # 窗口高度一半


# 确定窗口大小和位置
root.geometry(f'1000x700+{int(x_coordinate)}+{int(y_coordinate)}')
root.iconbitmap('bit.ico')
root.title('Management System')

label = tk.Label(root, text='输入窗口编号ID:', font=font, anchor="e", width=20)
label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = tk.Text(root, font=font, height=5, width=40, bd=3)
entry1.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label = tk.Label(root, text='输入搜索词:', font=font, anchor="e", width=20)
label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Text(root, font=font, height=5, width=40, bd=3)
entry2.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label = tk.Label(root, text='输入Asin:', font=font, anchor="e", width=20)
label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry3 = tk.Text(root, font=font, height=5, width=40, bd=3)
entry3.grid(row=2, column=1, padx=10, pady=5, sticky="w")

label = tk.Label(root, text='运行记录:', font=font, anchor="e", width=20)
label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry4 = tk.Text(root, font=font, height=5, width=40, bd=3)
entry4.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# 创建按钮
button01 = tk.Button(root, text='开始运行', font=font, command=lambda :MyThread(Main))
button01.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")  # 跨两列

# 设置行和列的权重，以便窗口调整大小时组件能自适应
for i in range(5):  # 5行
    root.grid_rowconfigure(i, weight=1)
for j in range(2):  # 2列
    root.grid_columnconfigure(j, weight=1)

root.mainloop()














