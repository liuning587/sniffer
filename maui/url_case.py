import time, datetime
import logging
from django.core import serializers
import xlwt
import pymysql
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from maui.models import MauiUrlCase


# logger = logging.getLogger(__name__)

def add_cases(request):
    qu_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    qu_time = qu_time.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        url_cases = MauiUrlCase(
            url_id=request.POST['id'],
            case_desc=request.POST['case_desc'],
            data=request.POST['data'],
            expect=request.POST['expect'],
            create_by=request.POST['create_by'],
            state=request.POST['case_state'],
            create_time=qu_time,
        )
        url_cases.save()
        url_cases_id = url_cases.id

    return url_cases_id


def select(request):
    if request.method == 'GET':
        id = request.GET['id']
        url_case = MauiUrlCase.objects.filter(id=id)
        # 查询全部
        url_case = serializers.serialize("json", url_case)
        # print (url_case)
    return url_case


def update(request):
    qu_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    qu_time = qu_time.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        url_cases = MauiUrlCase.objects.get(id=request.POST['id'])
        url_cases.case_desc = request.POST['case_desc']
        url_cases.data = request.POST['data']
        url_cases.expect = request.POST['expect']
        url_cases.create_by = request.POST['create_by']
        url_cases.state = request.POST['case_state']
        url_cases.create_time = qu_time
        url_cases.save()
    elif request.method == 'GET':
        # logger.info("查询问题："+request.GET['id'])
        id = request.GET['url_id']
        # url_cases = MauiUrlCase.objects.filter(url_id=id)
        url_cases = MauiUrlCase.objects.raw('''
        select t1.* ,t2.* from `maui_url_case` t1
left join `maui_url` t2
on t1.url_id=t2.id
where t1.url_id=
        ''' + id)
    return url_cases


