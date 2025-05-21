import requests
import json
import time

# 官方文档地址
# https://doc2.bitbrowser.cn/jiekou/ben-di-fu-wu-zhi-nan.html

# 此demo仅作为参考使用，以下使用的指纹参数仅是部分参数，完整参数请参考文档

url = "http://127.0.0.1:54345"
headers = {'Content-Type': 'application/json',
           'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.89 Safari/537.36',
           'x-api-key':'0b6abb6cbbd3481686bb0f14142803d0'}



def createBrowser():  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
    json_data = {
        'name': 'google',  # 窗口名称
        'remark': '',  # 备注
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'proxyType': 'noproxy',
        'host': '',  # 代理主机
        'port': '',  # 代理端口
        'proxyUserName': '',  # 代理账号
        "browserFingerPrint": {  # 指纹对象
            'coreVersion': '124'  # 内核版本，注意，win7/win8/winserver 2012 已经不支持112及以上内核了，无法打开
        }
    }

    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    browserId = res['data']['id']
    print(browserId)
    return browserId


def updateBrowser():  # 更新窗口，支持批量更新和按需更新，ids 传入数组，单独更新只传一个id即可，只传入需要修改的字段即可，比如修改备注，具体字段请参考文档，browserFingerPrint指纹对象不修改，则无需传入
    json_data = {'ids': ['93672cf112a044f08b653cab691216f0'],
                 'remark': '我是一个备注', 'browserFingerPrint': {}}
    res = requests.post(f"{url}/browser/update/partial",
                        data=json.dumps(json_data), headers=headers).json()
    print(res)


def openBrowser(id):  # 直接指定ID打开窗口，也可以使用 createBrowser 方法返回的ID
    json_data = {"id": f'{id}'
                 }
    res = requests.post(f"{url}/browser/open",
                        data=json.dumps(json_data), headers=headers).json()
    return res


def closeBrowser(id):  # 关闭窗口
    json_data = {'id': f'{id}'}
    requests.post(f"{url}/browser/close",
                  data=json.dumps(json_data), headers=headers).json()


def close_all_Browser():  # 关闭所有窗口
    res = requests.post(f"{url}/browser/close/all",
                  headers=headers).json()
    return res


def Browser_list():  # 关闭窗口
    json_data = {
  "page": 0,
  "pageSize":300
}
    res = requests.post(f"{url}/browser/list",
                  data=json.dumps(json_data), headers=headers).json()
    data = json.dumps(res['data']['list'])
    with open('窗口列表.html','w',encoding='utf-8') as f:
        f.write(data)
    return res

if __name__ == '__main__':
    # browser_id = createBrowser()
    browser_id = "d0e66fb3535a405f9e4be1e351d432cc"
    print(openBrowser(browser_id))
    # print(Browser_list())


    # time.sleep(10)  # 等待10秒自动关闭窗口

    # closeBrowser(browser_id)




