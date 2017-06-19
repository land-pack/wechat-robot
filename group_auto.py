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

@itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    user_name = msg['FromUserName']
    print 'user_name', user_name
    print msg['ActualNickName']
    print msg['Type']
    print msg['User']
    for i, k in msg.items():
        print i, k
    reply = get_response(msg['Text'])
    print 'Group name', dir(msg)
    return reply or defaultReply

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
