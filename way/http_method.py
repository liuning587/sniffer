# -*- coding:utf-8 -*-
# Filename:http_method.py
import http.cookiejar, logging
import urllib.request
import requests, json

cj = http.cookiejar.CookieJar();
cjhdr = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cjhdr)
logger = logging.getLogger(__name__)
jar = requests.cookies.RequestsCookieJar()

# 以上定义的变量，在后续进程中肯定是安全的，但如果实现系统内线程执行，可能会出现问题

class Response():
    def setcode(self, code):
        Response.code = code

    def getcode(self):
        return Response.code

    def set_result(self, resmsg):
        resmsg = resmsg.encode('utf-8')
        Response.result = resmsg

    def read(self):
        return Response.result


def do_appget(url, data, appInfo):
    try:
        data = data.encode('UTF-8')
        url = url + '?%s' % data
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application / x - www - form - urlencoded')
        req.add_header('Connection', 'keep-alive')
        req.add_header('User-Agent', appInfo.get('User-Agent'))
        req.add_header('Cookie', appInfo.get('Cookie'))
        response = opener.open(req)
    except Exception as e:
        response = Response()
        response.setcode(999)
        response.set_result(str(e))
        logger.error(url + ':error:' + str(e) + response.read().decode('utf-8'))
    return response


def do_apppost(url, data, appInfo):
    try:
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8')
        req = urllib.request.Request(url=url, data=data)
        req.add_header('Cookie', appInfo.get('Cookie'))
        req.add_header('User-Agent', appInfo.get('User-Agent'))
        response = opener.open(req)
    except Exception as e:
        response = Response()
        response.setcode(999)
        response.set_result(str(e))
        logger.error(url + ':error:' + str(e))
    return response


def app_get(url, data, appInfo):
    try:
        logger.info(url + '?%s' % data)
        header = {
            'Cookie': appInfo.get('Cookie'),
            'User-Agent': appInfo.get('User-Agent')}
        response = requests.get(url, headers=header, params=data, cookies=jar)
    except Exception as e:
        response = requests.models.Response
        response.status_code = 999
        response.text = str(e)
        logger.error(url + ':error:' + str(e) + str(response.status_code))

    return response


# requsts无法在post中添加header。会参数确实，所有目前不添加
def app_post(url, data, appInfo):
    try:

        header = {
            # "Host": "api.qdingnet.com",
            # "Content-Type": "application / x - www - form - urlencoded",
            # "Connection": 'keep - alive',
            # "Accept": "* / *",
            'content-type': 'application/json',
            'Cookie': appInfo.get('Cookie'),
            'User-Agent': appInfo.get('User-Agent')
        }
        logger.info(url)
        response = requests.post(url,data=data)
    except Exception as e:
        response = requests.models.Response
        response.status_code = 999
        response.text = str(e)
        logger.error(url + ':error:' + str(e))
    return response


def do_pcget(url, data):
    response = None
    try:
        if 'shanghu.qdingnet.com' in url:
            data = urllib.parse.urlencode({"name": data})[5:].replace('%3D', '=').replace('%26', '&').replace('2C',
                                                                                                              ',').replace(
                '%3A', ':')
        else:
            data = urllib.parse.urlencode({"name": data})[5:].replace('%3D', '=').replace('%26', '&')
        response = opener.open(url + '?%s' % data)
    except Exception as e:
        response = Response()
        response.setcode(999)
        response.set_result(str(e))
        logger.error(url + ':error:' + str(e))
    return response


def do_pcpost(url, data):
    try:
        # 如果是json就进行json格式发送。
        if data.startswith('{'):
            # 将str转化成dict，便于json使用
            data_dic = eval(data)
            jdata = json.dumps(data_dic)
            req_post = jdata.encode('UTF-8')
            req = urllib.request.Request(url=url, data=req_post)
            req.add_header("Content-Type", "application/json")
            response = opener.open(req)
        else:
            data = data.encode('UTF-8')
            response = opener.open(url, data)
    except Exception as e:
        response = Response()
        response.set_result(str(e))
        response.setcode(999)
        logger.error(url + ':error:' + str(e))
    return response
