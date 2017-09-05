from django.test import TestCase


# Create your tests here.


def conf_update_str(string):
    confs = ''
    for con in string.splitlines(keepends=True):
        con = con.replace('<br>', '').strip()
        confs = confs + con
    return confs


string = '''#需要修复供应商 工单创建日期
<br>supplier.startTime=2017-7-1
<br>supplier.endTime=2017-9-1
<br>supplier.cron=0 2 14 31 8 ? *'''

print(conf_update_str(string))
