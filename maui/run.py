# Filename: run.py
import datetime
import logging
from builtins import dict, type, Exception, str, list

from . import login
from way import http_method, sendWarning
from maui.models import MauiUrlCase
from maui.models import MauiUrl
from maui.models import MauiResult

logger = logging.getLogger(__name__)


def run_app(urlID='0'):
    # 查询urlid并确定登录环境和信息
    maui_url = MauiUrl.objects.filter(id=urlID, state='1')[0]
    environ = maui_url.environ
    url = maui_url.url
    login_name = maui_url.login_name
    login_pwd = maui_url.login_pwd
    method = maui_url.method
    is_warning = maui_url.is_warning
    url_desc = maui_url.url_desc
    emailto = maui_url.create_by

    if environ == 'qd':
        token_userToken = login.login_app_qd(login_name, login_pwd)
    elif environ == 'qa':
        token_userToken = login.login_app_qa(login_name, login_pwd)
    elif environ == 'dev':
        token_userToken = login.login_app_qa(login_name, login_pwd)

    logger.info("获取token" + token_userToken)
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    token = '&userToken=' + token_userToken
    # 插入数据库预计执行用例
    result = MauiResult.objects.filter(url_id__iexact=urlID)
    result.delete()
    # 查询urlid下所有的可执行的用例。
    maui_url_cases = MauiUrlCase.objects.filter(url_id=urlID, state='1')
    for case in maui_url_cases:
        resultCase = MauiResult(
            cases_id=case.id,
            url_id=case.url_id,
            url_desc=case.url_desc,
            case_desc=case.case_desc,
            request=url + '&' + case.data + token,
            run_time=runTime,
            result='0',  # 初始化状态
            return_req='going',  # 执行进行中
        )
        resultCase.save()
        result_id = resultCase.id
        # print(resultCase.id)
        try:
            if method == 'POST':
                datas = {}
                datas['body'] = case.data.split('=')[1]
                datas['userToken'] = token_userToken
                response = http_method.do_apppost(url, datas)
                logger.info("Post:" + i.url + i.data)
            elif method == 'GET':
                response = http_method.do_appget(url, case.data + token)
                # logger.info("GET:" + i.url + i.data)
            return_result = response.read().decode('utf-8')
            logger.info(case.id + case.url_desc + "返回结果：" + str(response.getcode()) + "：" + str(return_result))

        except Exception as e:
            logger.error(case + "接口：" + case.id + case.url_desc + "--截取异常——" + str(e))
        if '"code":500' in return_result or response.getcode() != 200:
            result = '2'
            # 如果失败，允许发送短信和pus执行，否则只执行邮件
            if is_warning == 'yes':
                sendWarning.sendEmail(runTime + url_desc + url + case.case_desc + ":崩溃",
                                      case.id + case.date + token + 'return_result:' + return_result,
                                      emailto)
            logger.error(runTime + url_desc + url + case.case_desc + ":崩溃",
                         case.id + case.date + token + 'return_result:' + return_result)
        else:

            if case.expect in return_result:
                result = '1'  # 执行验证成功
            else:
                result = '-1'  # 执行验证失败
                # 如果失败，允许发送短信和pus执行，否则只执行邮件
                if is_warning == 'yes':
                    # param = {"msg": "sniffer:异常;" + i.system + "用例名:" + i.casename + "; 责任人:" + str(
                    #     i.emailto) + ";时间:" + runTime + ";链接:" + i.url}
                    # sendWarning.sendWeixinMsg(param)
                    sendWarning.sendEmail(runTime + url_desc + url + case.case_desc + ":崩溃",
                                          case.id + case.date + token + 'return_result:' + return_result,
                                          emailto)

                logger.error("断言异常" + runTime + url_desc + url + case.case_desc + return_result)
        resultEnd = MauiResult.objects.get(id=result_id)
        resultEnd.result = result
        resultEnd.return_result = return_result
        resultEnd.save()  # 写入数据库


# 非app业务均可执行
def runOther():

    sniffer = SnifferCases.objects.filter(state='1').exclude(system__endswith="app").order_by('system')
    whichSystem = 'foo'
    return_result = 'NK'
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    result = SnifferResult.objects.exclude(system__endswith="app")
    result.delete()
    for i in sniffer:
        resultCase = SnifferResult(
            cases_id=i.id,
            casename=i.casename,
            create_by=i.create_by,
            system=i.system,
            request=i.url + '&' + i.data,
            method=i.method,
            create_at=runTime,
            result='0',  # 初始化状态
            return_result='going',  # 执行进行中
        )
        resultCase.save()
        result_id = resultCase.id
        if i.system != whichSystem:
            if i.system == 'boss':
                login.loginBoss()
                whichSystem = i.system
            elif i.system == 'shanghu':
                login.loginShanghu()
                whichSystem = i.system
            elif i.system == 'm2':
                login.loginM2()
                whichSystem = i.system
            elif i.system == 'property':
                login.loginProperty()
                whichSystem = i.system
            elif i.system == 'finance':
                login.loginFinance()
                whichSystem = i.system
        try:
            if i.method == 'POST':
                response = http_method.do_pcpost(i.url, i.data)
            elif i.method == 'GET':
                response = http_method.do_pcget(i.url, i.data)
            return_result = response.read().decode('utf-8')
            logger.info(i.system + i.casename + "返回结果：" + str(response.getcode()) + "：" + str(return_result))
        except Exception as e:
            logger.error(i + "接口：" + i.system + i.casename + "--截取异常——" + str(e))
        if '"code":500' in return_result or response.getcode() != 200:
            result = '2'

            # 如果失败，允许发送短信和pus执行，否则只执行邮件
            if i.is_warning == 'yes':
                tpl_value = {'#name#': i.system, '#card#': i.casename, '#time#': runTime, '#money#': '崩溃'}
                sendWarning.sendMsg(tpl_value, mobile)
                logger.info("已经短信通知：" + mobile + str(tpl_value))
                # param = {"msg": "sniffer:崩溃" + i.system + "接口:" + i.casename + "; 责任人:" + str(
                #     i.emailto) + ";时间:" + runTime + ";链接:" + i.url}
                # sendWarning.sendWeixinMsg(param)
                msg = {'system': i.system, 'rank': i.casename + '崩溃', 'info': '返回' + return_result[0:150],
                       'time': runTime,
                       'do': '赶紧解决吧'}
                weixin_msg.send_sms(openid, msg)
            sendWarning.sendEmail(runTime + i.system + i.casename + ":崩溃",
                                  i.method + i.url + '&' + i.data + 'return_result:' + return_result, i.emailto)
            logger.error(
                i.system + i.casename + "执行报错了！崩溃级别" + i.method + i.url + '&' + i.data + 'return_result:' + return_result)
        else:
            if i.expect in return_result:
                result = '1'  # 执行验证成功
                # logger.info("执行成功" + i.system + i.casename)
            else:
                result = '-1'  # 执行验证失败

                # 如果失败，允许发送短信和pus执行，否则只执行邮件logger.error("断言异常" + i.system + i.casename + return_result)
                if i.is_warning == 'yes':
                    # param = {"msg": "sniffer:监控异常;" + i.system + "接口:" + i.casename + "; 责任人:" + str(
                    #     i.emailto) + ";时间:" + runTime + ";链接:" + i.url}
                    # sendWarning.sendWeixinMsg(param)
                    msg = {'system': i.system, 'rank': i.casename + '异常', 'info': '返回' + return_result[0:150],
                           'time': runTime,
                           'do': '看邮件解决吧!'}
                    weixin_msg.send_sms(openid, msg)
                sendWarning.sendEmail(runTime + i.system + i.casename + ":异常",
                                      i.method + i.url + '&' + i.data + 'return_result:' + return_result, i.emailto)

        resultEnd = SnifferResult.objects.get(id=result_id)
        resultEnd.result = result
        resultEnd.return_result = return_result
        resultEnd.save()  # 写入数据库
