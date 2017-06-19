#coding=utf8
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

action_flag = 0

@itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
def tuling_reply(msg):
    global action_flag
    defaultReply = 'I received: ' + msg['Text']
    user_name = msg['FromUserName']
    print 'user_name', user_name
    if msg['ActualNickName'] == 'Frank AK':
        # listen command
        Content = msg['Content']
        if Content == '图灵退下':
            action_flag = 1
        elif Content == '图灵上':
            action_flag == 0
        else:
            action_flag == 1

    if action_flag == 1:
        return

    for i, k in msg.items():
        print i, k
    reply = get_response(msg['Text'])
    print 'Group name', dir(msg)
    return reply or defaultReply

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
