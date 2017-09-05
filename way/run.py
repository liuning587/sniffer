# Filename: run.py
import datetime
import logging

from builtins import dict, type, Exception, str, list
from concurrent.futures import ThreadPoolExecutor

from . import login, http_method, sendWarning, weixin_msg
from result.models import SnifferResult, SnifferResultLog
from rail.models import SnifferCases
from way.models import SnifferWarning

logger = logging.getLogger(__name__)

# mobile = '15001365242'  # 多个用,号隔开
# openid = 'o44s5uAEtFmRM2EvsdfavsQD6yvY'
executor = ThreadPoolExecutor(max_workers=10)


def get_warning_open(wsystem):
    openids = []
    users = SnifferWarning.objects.filter(system__icontains=wsystem)
    for user in users:
        if len(user.wxopenid) > 5:
            openids.append(user.wxopenid)
        else:
            logger.info(user.name + '的openid有误')
    return openids


def get_warning_mobile(wsystem):
    mobileList = []
    users = SnifferWarning.objects.filter(rank='崩溃', system__icontains=wsystem)
    for user in users:
        if len(user.mobile) == 11:
            mobileList.append(user.mobile)
        else:
            logger.info(user.name + '的mobile有误')
    mobile = ','.join(mobileList)
    return mobile


def runApp(wsystem='QDapp'):
    mobile = get_warning_mobile(wsystem)
    openid = get_warning_open(wsystem)
    sniffer = SnifferCases.objects.filter(system__iexact=wsystem, state='1')
    if wsystem == 'QDapp':
        appInfo = login.loginApp()
    elif wsystem == 'HKapp':
        appInfo = login.loginHKApp()
    elif wsystem == 'BAMApp':
        appInfo = login.login_BAMApp()

    # 插入数据库预计执行用例
    result = SnifferResult.objects.filter(system__iexact=wsystem)
    result.delete()
    # 将线程组放入数组，然后消费，避免进程结束线程也结束
    futures = []
    for i in sniffer:
        future = executor.submit(runAppCase, i, mobile, openid,appInfo)
        futures.append(future)

    for future in futures:
        future.result()


def runAppCase(i, mobile, openid,appInfo):
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    token = '&userToken=' + appInfo['token']
    resultCase = SnifferResult(
        cases_id=i.id,
        casename=i.casename,
        create_by=i.create_by,
        system=i.system,
        request=i.url + '&' + i.data + token,
        method=i.method,
        create_at=runTime,
        result='0',  # 初始化状态
        return_result='going',  # 执行进行中
    )
    resultCase.save()
    result_id = resultCase.id
    logger.info(i.system + "：APP业务：" + i.casename)
    try:
        if i.method == 'POST':
            params = {'body': i.data.split('=')[1], 'userToken': appInfo.get('token')}
            # 出现appInfo前
            response = http_method.app_post(i.url, params, appInfo)
        elif i.method == 'GET':
            response = http_method.app_get(i.url, i.data + token, appInfo)
        return_result = response.text
        code = response.status_code
        # logger.info(i.system + i.casename + "返回结果：" + str(code) + "：" + return_result)

    except Exception as e:
        logger.error(i + "接口：" + i.system + i.casename + "--截取异常——" + str(e))
    if '"code":500' in return_result or code != 200:
        result = '2'
        # 如果失败，允许发送短信和pus执行，否则只执行邮件
        if i.is_warning == 'yes':
            tpl_value = {'#name#': i.system, '#card#': i.casename, '#time#': runTime, '#money#': '崩溃'}
            sendWarning.sendMsg(tpl_value, mobile)

            msg = {'system': i.system, 'rank': i.casename + '：崩溃' + ' +url: ' + i.url,
                   'info': '返回' + return_result[0:100],
                   'time': runTime,
                   'do': '详情可看邮件'}
            weixin_msg.send_sms(openid, msg)

        sendWarning.sendEmail(runTime + i.system + i.casename + ":崩溃",
                              i.method + i.url + '&' + i.data + token + 'return_result:' + return_result, i.emailto)
        logger.error(
            i.system + i.casename + "执行报错了！崩溃级别" + i.method + i.url + '&' + i.data + token + 'return_result:' + return_result)
    else:

        if i.expect in return_result:
            result = '1'  # 执行验证成功
        else:
            result = '-1'  # 执行验证失败
            # 如果失败，允许发送短信和pus执行，否则只执行邮件
            if i.is_warning == 'yes':
                msg = {'system': i.system, 'rank': i.casename + '：异常' + ' +url: ' + i.url,
                       'info': '返回' + return_result[0:100],
                       'time': runTime,
                       'do': '可看邮件解决吧'}
                weixin_msg.send_sms(openid, msg)

            sendWarning.sendEmail(runTime + i.system + i.casename + " :异常",
                                  i.method + i.url + '&' + i.data + token + 'return_result:' + return_result,
                                  i.emailto)
            logger.error("断言异常" + i.system + i.casename + return_result)
    resultEnd = SnifferResult.objects.get(id=result_id)
    resultEnd.result = result
    resultEnd.return_result = return_result
    resultEnd.save()  # 写入数据库


# 非app业务均可执行 m2 boss property shanghu finance 抽象所有登录的系统均可用这种方法。
def runBo(wsystem):
    mobile = get_warning_mobile(wsystem)
    openid = get_warning_open(wsystem)
    sniffer = SnifferCases.objects.filter(state='1', system__iexact=wsystem).order_by(
        'system')
    result = SnifferResult.objects.filter(system__iexact=wsystem)
    result.delete()
    system = wsystem
    if system == 'boss':
        login.loginBoss()
    elif system == 'shanghu':
        login.loginShanghu()
    elif system == 'm2':
        login.loginM2()
    elif system == 'property':
        login.loginProperty()
    elif system == 'finance':
        login.loginFinance()
    elif system == 'wave':
        login.loginWave()
    elif system == 'Compass':
        login.loginCompass()

    futures = []
    for i in sniffer:
        future = executor.submit(runCase, i, mobile, openid)
        futures.append(future)

    for future in futures:
        future.result()


# 定义执行过程，为内部实现线程池做准备。
def runCase(i, mobile, openid):
    try:
        runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
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
        logger.info(i.system + "：业务：" + i.casename)
    except Exception as e:
        logger.exception()

    try:
        if i.method == 'POST':
            response = http_method.do_pcpost(i.url, i.data)
        elif i.method == 'GET':
            response = http_method.do_pcget(i.url, i.data)
        return_result = response.read().decode('utf-8')
        # logger.info(i.system + i.casename + "返回结果：" + str(response.getcode()) + "：" + str(return_result))
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
            msg = {'system': i.system, 'rank': i.casename + '崩溃' + ' +url: ' + i.url,
                   'info': '返回' + return_result[0:100],
                   'time': runTime,
                   'do': '详情可看邮件'}
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
                msg = {'system': i.system, 'rank': i.casename + '异常' + ' +url: ' + i.url,
                       'info': '返回' + return_result[0:100],
                       'time': runTime,
                       'do': '看邮件解决吧!'}
                weixin_msg.send_sms(openid, msg)
            sendWarning.sendEmail(runTime + i.system + i.casename + ":异常",
                                  i.method + i.url + '&' + i.data + 'return_result:' + return_result, i.emailto)

    resultEnd = SnifferResult.objects.get(id=result_id)
    resultEnd.result = result
    resultEnd.return_result = return_result
    resultEnd.save()  # 写入数据库
