# Filename: sendWarning.py
from builtins import Exception, str

from django.apps import AppConfig
import requests,logging,urllib.request,json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from . import yunpian_msg

logger = logging.getLogger(__name__)
def sendEmail(casename,url,to):
    to=to.split(';')
    user = 'qding@qding.me'
    pwd = 'abc123c'
    msg = MIMEMultipart()
    msg['Subject'] = 'sniffer监控的接口异常： '+casename
    msg['From'] = user
    msg['To'] = ",".join(to)
    content1 = MIMEText('异常接口名称：<br>' + casename +' <br>。  url  接口链接 :<br>  ' +url , 'plain', 'utf-8')
    msg.attach(content1)
    s = smtplib.SMTP('smtp.exmail.qq.com')
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    logger.info("发送邮件成功"+str(to))
    s.close()

def howDay():
    birthday=date(1986,6,4)
    now = date.today()
    age=now-birthday
    logger.info(age.days)
    return age.days


def sendWeixinMsg(reqData):

	wxUrl = "http://sniffer.iqdnet.cn/alarm/"
	try :
		requests.post(wxUrl,reqData)
	except Exception as e:
		logging.info("微信发送失败"+str(e))


# yunpian

# 警告：服务#name#；业务#card#，于#time#出现异常：#money#，请及时处理。

def sendMsg(tpl_value,sedMobile):
    #修改为您要发送的短信内容
    #查账户信息
    yunpian_msg.get_user_info()
    # print()
    #调用智能匹配模板接口发短信
    #调用模板接口发短信
    tpl_id = 1627026 #【千丁互联】警告：服务#name#；业务#card#，于#time#出现异常：#money#，请及时处理
    #name#；业务#card#，于#time#出现异常：#money#
    # tpl_value = {'#name#':'boss','#card#':'支付','#time#':'time','#money#':'崩溃'}
    # tpl_value={'#name#':i.system,'#card#: ':i.casename,'#time#':runTime,'#money#':'崩溃'}
    # tpl_value=str(tpl_value)
    logger.info("发送短信内容:"+str(tpl_value))
    yunpian_msg.tpl_send_sms(tpl_id, tpl_value, sedMobile)