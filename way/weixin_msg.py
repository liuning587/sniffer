import urllib, http.client, datetime, logging, urllib.request

import json
from . import sendWarning

# 服务地址
TEMPLATE_ID = 'ltW2G3LlTkGR9bSME2HZOHfkmhkvJ4HIUbg8vMo287c'
# ltW2G3LlTkGR9bSME2HZOHfkmhkvJ4HIUbg8vMo287c

# {{first.DATA}}
# 报警类型：{{keyword1.DATA}}
# 报警内容：{{keyword2.DATA}}
# 报警时间：{{keyword3.DATA}}
# {{remark.DATA}}
# 在发送时，需要将内容中的参数（{{.DATA}}内为参数）赋值替换为需要的信息
# 内容示例
# 企业名称：abc公司
# 报警类型：紧急提醒
# 报警内容：污水排放量已超标
# 报警时间：2016-7-26 8:00:00


logger = logging.getLogger(__name__)


def send_sms(openids, msg):
    try:
        data = 'publicsId=241&appId=wxd23d0632ad28c805'
        url = 'http://boss.qdingnet.com/weixin_admin/web/publics/getAccessToken'
        token = urllib.request.urlopen(url + '?%s' % data)
        token = token.read().decode("utf-8")
    except Exception as e:
        tpl_value = {'#name#': '获取微信token异常', '#card#': '获取微信token异常', '#time#': runTime, '#money#': '崩溃'}
        sendWarning.sendMsg(tpl_value, '15001365242')
        logger.error("获取token异常" + str(e))
    if (len(token) < 3):
        logger.error("获取token异常null" + str(e))
        tpl_value = {'#name#': '获取微信token==null', '#card#': '获取微信token异常', '#time#': runTime, '#money#': '崩溃'}
        sendWarning.sendMsg(tpl_value, '15001365242')
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % token
    for openid in openids:
        data = {'touser': openid,
                'template_id': 'ltW2G3LlTkGR9bSME2HZOHfkmhkvJ4HIUbg8vMo287c',
                'data': {
                    'first': {
                        'value': 'sniffer：' + msg['system']
                    },
                    'keyword1': {
                        'value': msg['time']
                    },
                    'keyword2': {
                        'value': msg['rank']
                    },
                    'keyword3': {
                        'value': msg['info']
                    },
                    "remark": {
                        "value": msg['do'],
                        "color": "#173177"
                    }
                }
                }
        json_data = json.dumps(data)
        json_data = json_data.encode('utf-8')
        req = urllib.request.Request(url, json_data)
        response = urllib.request.urlopen(req)
        logger.info(response.read())


if __name__ == '__main__':
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    msg = {'system': 'i.system', 'rank': 'i.casename + 异常', 'info': '返回 + return_result', 'time': runTime,
           'do': '可看邮件解决吧'}
    send_sms('o44s5uAEtFmRM2EvsdfavsQD6yvY', msg)
