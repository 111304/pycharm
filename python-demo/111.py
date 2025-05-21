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
        openBrowser(i['id'])
        print('正在打开:' + i['id'])
        # time.sleep(20)
        if num == 5:
            break
    # bit_api.close_all_Browser()



