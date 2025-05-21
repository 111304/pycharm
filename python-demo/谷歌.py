from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Edge(options=chrome_options)

print(driver.title)




