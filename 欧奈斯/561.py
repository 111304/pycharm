from selenium import webdriver
import time

driver = webdriver.Chrome()  # 根据选项创建浏览器实例

driver.get('http://www.baidu.com')  # 访问 URL

time.sleep(5)

print(driver.title)



driver.quit()  # 关闭浏览器