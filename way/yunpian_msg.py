#!/usr/local/bin/python
#-*-coding:utf-8-*-

#author: jacky
# Time: 15-12-15
# Desc: 短信http接口的python代码调用示例
# https://www.yunpian.com/api/demo.html
# https访问，需要安装  openssl-devel库。apt-get install openssl-devel

# import httplib
import urllib,http.client,datetime

import json
#服务地址
sms_host = "sms.yunpian.com"
voice_host = "voice.yunpian.com"
#端口号
port = 443
apikey = "297340669946d1e09448bd33f1fbab8d"

#版本号
version = "v1"
#查账户信息的URI
user_get_uri = "/" + version + "/user/get.json"
#智能匹配模板短信接口的URI
sms_send_uri = "/" + version + "/sms/send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"
#语音短信接口的URI
sms_voice_send_uri = "/" + version + "/voice/send.json"
#语音验证码
voiceCode = 1234
def get_user_info():
    """
    取账户信息
    """
    conn = http.client.HTTPSConnection(sms_host , port=port)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request('POST',user_get_uri,urllib.parse.urlencode( {'apikey' : apikey}))
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def send_sms(text, mobile):
    """
    通用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def tpl_send_sms(tpl_id, tpl_value, mobile):
    """
    模板接口发短信
    """
    params = urllib.parse.urlencode({'apikey': apikey, 'tpl_id':tpl_id, 'tpl_value': urllib.parse.urlencode(tpl_value), 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_tpl_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def send_voice_sms(code, mobile):
    """
    通用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'code': code, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPSConnection(voice_host, port=port, timeout=30)
    conn.request("POST", sms_voice_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':
    #修改为您的apikey.可在官网（http://www.yunpian.com)登录后获取
    # apikey = "297340669946d1e09448bd33f1fbab8d"
    #修改为您要发送的手机号码，多个号码用逗号隔开
    mobile='15001365242,18010469086,13552488747,18801479233'

    #修改为您要发送的短信内容
    text = "您的验证码是1234【云片网】"
    #查账户信息
    print(get_user_info())
    runTime = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    #调用智能匹配模板接口发短信
    # print send_sms(apikey,text,mobile)
    #调用模板接口发短信
    tpl_id = 1627026 #【千丁互联】警告：服务#name#；业务#card#，于#time#出现异常：#money#，请及时处理
    #name#；业务#card#，于#time#出现异常：#money#
    tpl_value = {'#name#':'boss','#card#':'测试短信发送','#time#':runTime,'#money#':'崩溃'}
    print(tpl_send_sms(tpl_id, tpl_value, mobile))
    #调用模板接口发语音短信
    # print send_voice_sms(apikey,voiceCode,mobile)