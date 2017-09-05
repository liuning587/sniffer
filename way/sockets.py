import socket, logging,datetime
from . import sendWarning, weixin_msg

logger = logging.getLogger(__name__)

# mobile = '15001365242,15001239330'
# openid = ['o44s5uAEtFmRM2EvsdfavsQD6yvY','o44s5uIcjsmtRNhLo7o5ERBqHcL4']
#

mobile = '15001365242,18601210210,13810373436'
openid = ['o44s5uAEtFmRM2EvsdfavsQD6yvY','o44s5uKeVGVUyvTa41XUvdj2h2sA','o44s5uNL-HRdokdF5rRLs71aQ3kc']


def reply_socket():
    sk = socket.socket()
    # res = sk.connect_ex(("10.37.253.60", 9999))  # qaqd服务器端的连接
    # res = sk.connect_ex(("10.37.253.60", 9999))  # qaqd服务器端的连接
    res = sk.connect_ex(("111.207.61.194", 9999))  # qd与服务器端的连接
    sk.settimeout(500)
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    if res != 0:
        logger.error('reply——socket返回异常：' + str(res))
        tpl_value = {'#name#': 'reply', '#card#': 'socket链接服务', '#time#': runTime, '#money#': '异常：' + str(res)}
        sendWarning.sendMsg(tpl_value, mobile)

        msg = {'system': 'reply', 'rank': 'socket链接服务' + '：异常', 'info': '返回' + '异常：' + str(res),
               'time': runTime,
               'do': '赶紧解决吧'}
        weixin_msg.send_sms(openid, msg)
    else:
        logger.info('socket返回正常：' + str(res))
    sk.close()
    return res

