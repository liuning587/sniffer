import urllib.request
import requests


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


def do_appget(url, data):
    try:
        data = data.encode('UTF-8')
        print(url + '?%s' % data.decode('utf-8'))
        response = urllib.request.urlopen(url + '?%s' % data.decode('utf-8'))
    except Exception as e:
        response = Response()
        response.setcode(999)
        response.set_result(str(e))
        print(url + ':error:' + str(e))
    print (response.read().decode('utf-8'))




def do_get(url, data):
    try:
        data = data.encode('UTF-8')
        print(url + '?%s' % data.decode('utf-8'))
        response = requests.get(url ,params=data)
    except Exception as e:
        # response = Response()
        # response.setcode(999)
        # response.set_result(str(e))
        print(url + ':error:' + str(e))
    print (response.text)



url = 'https://api.qdingnet.com/qding-merchant-api/api/json/order/searchOrder'
data = 'body= { "pageNo" : 1, "condition" : "{\"notPayStatus\":1,\"orderStatusList\":[11,12,14,15,16]}", "productNo" : "NC", "appUser" : { }, "pageSize" : 10, "appDevice" : { "qdAppName" : "qding", "qdPlatform" : "iOS", "OSVersion" : "10.3.1", "qdDevice" : "iPhone 7 Plus", "qdVersion" : "1.0.0" } }' \
       '&userToken=v1_UU5LQm56KzdLYnJFZnRWeVluenV3b2t3RzU1T0c5eklsMXhmbHdaYndaZ0dTY05FTzNYaGozUUZYVU05SERMOGpOejN3c3VPZEo1RGY4eUEwWUxSRnNqaG5WandoU2Q2SlJBdlNUUEZJdU14SlE4MHhwRFo4K3h6UnJWWEtjaHk4eTQ2eGpVK3NuNHc0cllJNUx4NjVETi9HZ3lEWHJ0MEpucUdBemVFcnVSMEkweGNUMWxZMDB2WkhMZGNMMXBaWGpxQm5CLzZpb3B4ZzROOEdpMWl0YUVFaW5KclpLbng3NDByYXpvWWRrckVmTzErc0JHREdOYkhkTGVhSFV1MitLTGdTcXpVSi80PR7YPEGfOfUmKW2r4zQWsoKCffbQdIB4lQSjuEdWyZMyoNzk1cQSPyNofa724_v9wMX1i8D-J4jOyG5q9Lfdj8aDR4f4_iHW6zHmOvNejXymDAKPZF6WNBrZ5ANxQy0aTh2pdmeS_O2a8dsS2lBRxJLvsgxg20phRUg-P9INhJbD'
do_appget(url, data)
print("&&&&&&&&&&&&&&&&&&")
do_get(url, data)


url = 'https://api.qdingnet.com/qding-merchant-api/api/json/finance/getSettleAmount'
data = 'body={ "appUser" : { }, "appDevice" : { "qdAppName" : "qding", "qdPlatform" : "iOS", "OSVersion" : "10.3.1", "qdDevice" : "iPhone 7 Plus", "qdVersion" : "1.0.0" }}' \
       '&userToken=v1_UU5LQm56KzdLYnJFZnRWeVluenV3b2t3RzU1T0c5eklsMXhmbHdaYndaZ0dTY05FTzNYaGozUUZYVU05SERMOGpOejN3c3VPZEo1RGY4eUEwWUxSRnNqaG5WandoU2Q2SlJBdlNUUEZJdU14SlE4MHhwRFo4K3h6UnJWWEtjaHk4eTQ2eGpVK3NuNHc0cllJNUx4NjVETi9HZ3lEWHJ0MEpucUdBemVFcnVSMEkweGNUMWxZMDB2WkhMZGNMMXBaWGpxQm5CLzZpb3B4ZzROOEdpMWl0YUVFaW5KclpLbng3NDByYXpvWWRrckVmTzErc0JHREdOYkhkTGVhSFV1MitLTGdTcXpVSi80PR7YPEGfOfUmKW2r4zQWsoKCffbQdIB4lQSjuEdWyZMyoNzk1cQSPyNofa724_v9wMX1i8D-J4jOyG5q9Lfdj8aDR4f4_iHW6zHmOvNejXymDAKPZF6WNBrZ5ANxQy0aTh2pdmeS_O2a8dsS2lBRxJLvsgxg20phRUg-P9INhJbD'
do_appget(url, data)
print("&&&&&&&&&&&&&&&&&&")

do_get(url, data)




