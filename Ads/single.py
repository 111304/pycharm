import requests



url = "http://local.adspower.net:50325"
headers = {'Content-Type': 'application/json',
           'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.89 Safari/537.36',
           }

# 打开窗户
def openBrowser(user_id):  # 直接指定ID打开窗口，也可以使用 createBrowser 方法返回的ID
    res = requests.get(f"{url}/api/v1/browser/start?user_id={user_id}",
                      headers=headers).json()
    print(f'窗口:{user_id}打开成功。')
    return res

# 关闭窗户
def closeBrowser(user_id):  # 直接指定ID打开窗口，也可以使用 createBrowser 方法返回的ID
    res = requests.get(f"{url}/api/v1/browser/stop?user_id={user_id}",
                      headers=headers).json()
    return res



