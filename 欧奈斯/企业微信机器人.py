import requests

def send_wechat_message(key,information):  #发送消息
    '''
    发送企业微信消息
    :param key:机器人webhookurl中的key参数
    :param information:你要发送的消息内容
    '''
    try:
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        Header = {'Content-Type':"application/json",'charset':'UTF-8'}
        mbody = {
                "msgtype": "text",
                "text": {
                    "content": information,
                    "mentioned_list": ["吕晓凤"], #userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
	            	# "mentioned_mobile_list":["13800001111","@all"] #手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
                    }
            }
        response = requests.post(url,json=mbody,headers = Header)
        return_json = response.json()  # 返回转为json
        print(f'微信发送成功:\n{information}')

    except Exception as e:
        print('发送微信失败:',e)

if __name__ == '__main__':
    key = "5e433db5-56e2-4b21-aedc-6cd57aa18fc0"
    information = 'hello world'
    send_wechat_message(key,information)
