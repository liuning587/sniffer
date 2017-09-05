from django.apps import AppConfig
import time, logging, urllib.request, json, datetime
from way import http_method

logger = logging.getLogger(__name__)


# app用户13552487304 登录获取token 正式环境
def login_app_qd():
    Userdata = '''body={"accountId":"ff8080814dfce413014e005a47550633","appDevice":{"qdPlatform":"IOS","qdDevice":"iphone6","qdVersion":"1.3.0"},"appUser":null}'''
    Userdata = Userdata.encode('UTF-8')
    response = urllib.request.urlopen('https://api.qdingnet.com/qding-api/api/json/user/authorize', Userdata)
    result = json.loads(response.read().decode('utf-8'))
    token = result.get('data').get('userToken')
    return token

# app用户13552487304 登录获取token qa环境
def login_app_qa():
    Userdata = '''body={"accountId":"ff8080814dfce413014e005a47550633","appDevice":{"qdPlatform":"IOS","qdDevice":"iphone6","qdVersion":"1.3.0"},"appUser":null}'''
    Userdata = Userdata.encode('UTF-8')
    response = urllib.request.urlopen('https://qaapi.qdingnet.com/qding-api/api/json/user/authorize', Userdata)
    result = json.loads(response.read().decode('utf-8'))
    token = result.get('data').get('userToken')
    return token

# app用户13552487304 登录获取token dev环境
def login_app_dev():
    Userdata = '''body={"accountId":"ff8080814dfce413014e005a47550633","appDevice":{"qdPlatform":"IOS","qdDevice":"iphone6","qdVersion":"1.3.0"},"appUser":null}'''
    Userdata = Userdata.encode('UTF-8')
    response = urllib.request.urlopen('https://api.qdingnet.com/qding-api/api/json/user/authorize', Userdata)
    result = json.loads(response.read().decode('utf-8'))
    token = result.get('data').get('userToken')
    return token

def loginShanghu():
    url = 'https://qd.qdingnet.com/managerbg/home/loginByMobile'
    data = 'callback=angular.callbacks._1&mobile=15001365242&orgTypeFlag=sh&password=5242&remember=false'
    http_method.do_pcget(url, data)
    url = 'https://shanghu.qdingnet.com/merchantbg/admin/login/currentUser'
    data = 'remember=true'
    name = 'shanghu'
    login(name, url, data)


def loginBoss():
    # 登录前先推出
    url = 'https://qd.qdingnet.com/managerbg/home/logout'
    response = http_method.do_pcget(url, '')
    logger.info('bosscases退出成功')
    url = 'https://finance.qdingnet.com/#/logout'
    response = http_method.do_pcget(url, '')

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


def loginFinance():
    # 登录前先退出

    url = 'https://finance.qdingnet.com/#/logout'
    http_method.do_pcget(url, '')
    logger.info('finance退出成功')

    url = 'https://finance.qdingnet.com/managerbg/home/login'
    data = 'account=finance&captcha=EndTo2&password=qdf2016&remember=false&orgTypeFlag=cw'
    http_method.do_pcpost(url, data)
    url = 'https://finance.qdingnet.com/managerbg/puser/get'
    data = 'orgTypeFlag=cw'
    name = 'finance'
    login(name, url, data)


def loginProperty():
    url = 'https://qd.qdingnet.com/managerbg/home/loginByMobile'
    data = 'callback=jQuery111007020590975880623_1468319377873&mobile=18311078056&password=123qwe&orgTypeFlag=wy&_=1468319377875'
    http_method.do_pcget(url, data)
    url = 'https://property.qdingnet.com/login'
    data = 'uuId=ff808181539dffee01539e005c9300e0'
    name = 'property'
    login(name, url, data)


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
