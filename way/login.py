from django.apps import AppConfig
import time, logging, urllib.request, json, datetime
from . import http_method
from . import sendWarning

logger = logging.getLogger(__name__)


# app用户13552487304 登录获取tokenm ff8080814dfce413014e005a47550634
# 由于授权策略变更，固定x.sig和X
def loginApp():
    appInfo = {}
    appInfo['User-Agent'] = 'qd-app-1.0.0-ios'
    appInfo['Cookie'] = 'X.sig = GVsG9s1CvdmJrxQ7yhD6RrXNfjY; X=eyJtSWQiOiJmZjgwODA4MTVhZDE5ZTAzMDE1YWU3NDZkNzRlMGE2NiIsImFJZCI6IkZmODA4MDgxNWFkMTllMDMwMTVhZTc0NmQ3NGUwYTY1In0='
    Userdata = '''body={"accountId":"ff8080814dfce413014e005a47550633","appDevice":{"qdPlatform":"IOS","qdDevice":"iphone6","qdVersion":"3.0.0"},"appUser":null}'''
    Userdata = Userdata.encode('UTF-8')
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = urllib.request.urlopen('https://api.qdingnet.com/qding-api/api/json/user/authorize', Userdata)
        result = json.loads(response.read().decode('utf-8'))
        token = result.get('data').get('userToken')
        appInfo['token'] = token

    except Exception as e:
        logger.error('APP登录失败' + str(e))
        tpl_value = {'#name#': 'APP登录失败', '#card#': 'APP登录失败', '#time#': runTime, '#money#': '崩溃'}
        sendWarning.sendMsg(tpl_value, '15001365242')
        param = {"msg": "sniffer:app登录异常;" + name + 'runTime：' + runTime}
        sendWarning.sendWeixinMsg(param)
    return appInfo


# 管家app用户13911979999   登录获取token ff8080815ad19e03015ae746d74e0a66
# 由于授权策略变更，固定x.sig和X

def loginHKApp():
    appInfo = {}

    Userdata = '''body={"accountId":"ff8080815ad19e03015ae746d74e0a65","appDevice":{"qdPlatform":"IOS","qdDevice":"iphone6","qdVersion":"3.0.0"},"appUser":null}'''
    Userdata = Userdata.encode('UTF-8')
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    appInfo['Cookie'] = 'X=eyJtSWQiOiJmZjgwODA4MTVhZDE5ZTAzMDE1YWU3NDZkNzRlMGE2NiIsImFJZCI6ImZmODA4MDgxNWFkMTllMDMwMTVhZTc0NmQ3NGUwYTY1In0=; X.sig=blCvyS5v-Fa37KMpT0o_j_wdUms'

    try:
        response = urllib.request.urlopen('https://api.qdingnet.com/qding-api/api/json/user/authorize', Userdata)
        result = json.loads(response.read().decode('utf-8'))
        token = result.get('data').get('userToken')
        appInfo['token'] = token
        appInfo['User-Agent'] = 'mobile/qd-app-3.0.0-ios'


    except Exception as e:
        logger.error('HKAPP登录失败' + str(e))
        tpl_value = {'#name#': 'HKAPP登录失败', '#card#': 'HKAPP登录失败', '#time#': runTime, '#money#': '崩溃'}
        sendWarning.sendMsg(tpl_value, '15001365242')
        param = {"msg": "sniffer:HKapp登录异常;" + name + 'runTime：' + runTime}
        sendWarning.sendWeixinMsg(param)
    return appInfo


# 登录商户app #商户App登录获取token 15001365242  avTTSq 40aa06fb1ea746d2956a01624c15b262
# 由于授权策略变更，固定x.sig和X

def login_BAMApp():
    appInfo = {}
    Userdata = '''body={ "providerId":"1000324"}'''
    Userdata = Userdata.encode('UTF-8')
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
    appInfo['Cookie'] = 'X=eyJwcm92aWRlcklkIjoiMTAwMDMyNCJ9; X.sig=8Wzy1A1OY4ccn6cHgTw4dFXDDuY'
    appInfo['User-Agent'] = 'qd-app-1.0.0-ios'

    try:
        response = urllib.request.urlopen('https://api.qdingnet.com/qding-merchant-api/api/json/user/authorize',
                                          Userdata)
        result = json.loads(response.read().decode('utf-8'))
        token = result.get('data').get('userToken')
        appInfo['token'] = token
    except Exception as e:
        logger.error('merchantAPP登录失败' + str(e))
        tpl_value = {'#name#': 'merchant APP登录失败', '#card#': 'merchant APP登录失败', '#time#': runTime, '#money#': '崩溃'}
        sendWarning.sendMsg(tpl_value, '15001365242')
        param = {"msg": "sniffer:merchant app登录异常;" + name + 'runTime：' + runTime}
        sendWarning.sendWeixinMsg(param)
    return appInfo


# 商户后台登录
def loginShanghu():
    url = 'https://qd.qdingnet.com/managerbg/home/loginByMobile'
    data = 'callback=angular.callbacks._1&mobile=15001365242&orgTypeFlag=sh&password=5242&remember=false'
    http_method.do_pcget(url, data)
    url = 'https://shanghu.qdingnet.com/merchantbg/admin/login/currentUser'
    data = 'remember=true'
    name = 'shanghu'
    login(name, url, data)

# boss后台登录
def loginBoss():
    # 登录前先推出
    url = 'https://qd.qdingnet.com/managerbg/home/logout'
    response = http_method.do_pcget(url, '')
    logger.info('bosscases退出成功')
    # url = 'https://finance.qdingnet.com/#/logout'
    # response = http_method.do_pcget(url, '')
    time.sleep(1)

    url = 'https://qd.qdingnet.com/managerbg/home/login'
    data = 'account=autotest&password=@349223382a!@&remember=false&orgTypeFlag=bs&captcha=EndTo2'
    response = http_method.do_pcpost(url, data)
    if response.getcode() == 200:
        logger.info("bosscases登录成功")
    else:
        logger.error("bosscases登录失败")
    # 存储缓存
    url = 'https://qd.qdingnet.com/managerbg/puser/get'
    data = 'remember=true'
    http_method.do_pcpost(url, data)

#m2内部登录，也可以直接用token，待授权统一后，将接入app中
def loginM2():
    url = 'https://m2.iqdnet.com/location/choose/1789'
    data = ''
    http_method.do_pcget(url, data)
    url = 'https://m2.iqdnet.com/account/login'
    data = 'mobile=13552487304&password=487304'
    http_method.do_pcpost(url, data)
    url = 'https://m2.iqdnet.com/profile'
    data = ''
    name = 'm2'
    login(name, url, data)


# 财务系统登录，已经没有用了
def loginFinance():
    # 登录前先退出

    url = 'https://finance.qdingnet.com/#/logout'
    http_method.do_pcget(url, '')
    logger.info('finance退出成功')
    time.sleep(1)

    url = 'https://finance.qdingnet.com/managerbg/home/login'
    data = 'account=finance&captcha=EndTo2&password=qdf2016&remember=false&orgTypeFlag=cw'
    http_method.do_pcpost(url, data)
    url = 'https://finance.qdingnet.com/managerbg/puser/get'
    data = 'orgTypeFlag=cw'
    name = 'finance'
    login(name, url, data)

# 物业系统登录
def loginProperty():
    url = 'https://qd.qdingnet.com/managerbg/home/loginByMobile'
    data = 'callback=jQuery111007020590975880623_1468319377873&mobile=18311078056&password=123qwe&orgTypeFlag=wy&_=1468319377875'
    http_method.do_pcget(url, data)
    url = 'https://property.qdingnet.com/login'
    data = 'uuId=ff808181539dffee01539e005c9300e0'
    name = 'property'
    login(name, url, data)

# 罗盘系统登录
def loginCompass():
    url = 'https://c.qdingnet.com/login/verify.login'
    data = 'username=18801479233&password=admin'
    http_method.do_pcpost(url, data)
    url = 'https://c.qdingnet.com/index/index.do'
    data = ''
    name = 'Compass'
    login(name, url, data)


def loginWave():
    url = 'http://wave.qdingnet.com/qdp-wave-web/login/login.do'
    data = 'account=qding&password=qding123qwe'
    http_method.do_pcget(url, data)
    name = 'wave'
    url = 'http://wave.qdingnet.com/qdp-wave-web/workOrderProcess/queryPendingCount.do'
    data = ''
    login(name, url, data)


# 抽象登录方法
def login(name, url, data):
    try:
        response = http_method.do_pcget(url, data)
        responses = response.read().decode('utf-8')
        time.sleep(2)
        if response.getcode() == 200:
            logger.info(name + "登录200")
        else:
            logger.error(name + "登录失败" + responses)
            runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
            runTime = runTime.strftime("%Y-%m-%d %H:%M:%S")
            param = {"msg": "sniffer:登录异常;" + name + 'runTime：' + runTime}
            sendWarning.sendWeixinMsg(param)
            sendWarning.sendEmail(runTime + ":失败", name + '登录失败return_result:' + responses, 'zhaochunyu@qding.me')
    except Exception as e:
        logger.error(name + "登录失败" + str(e))
