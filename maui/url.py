from maui.models import MauiUrl
from maui.models import MauiUrlCase

import time, datetime
import logging
from django.core import serializers
import xlwt
import pymysql
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.db import connection

from django.db.models import Q


# logger = logging.getLogger(__name__)

def add(request):
    quTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    quTime = quTime.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        url = MauiUrl(
            create_by=request.POST['create_by'],
            url_desc=request.POST['url_desc'],
            url=request.POST['url'],
            system=request.POST['system'],
            environ=request.POST['environ'],
            login_name=request.POST['login_name'],
            login_pwd=request.POST['login_pwd'],
            create_time=quTime,
            method=request.POST['method'],
            is_warning=request.POST['is_warning'],
            state=request.POST['state'],
        )
        url.save()
        result_id = url.id

    return result_id


def select(request):
    qu_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    qu_time = qu_time.strftime("%Y-")
    # print (request.GET['id'])
    id = request.GET['id']
    if id == 'all':
        url = MauiUrl.objects.all().order_by('-id')  # 查询全部
        # url = MauiUrlCase.objects.filter(MauiUrl__id=1)  # 查询全部
        # url = serializers.serialize("json", url)
        # print(url)

    else:

        url = MauiUrl.objects.filter(id=id)
        url = serializers.serialize("json", url)

    return url


def update(request):
    quTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    quTime = quTime.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        maui = MauiUrl.objects.get(id=request.POST['id'])
        maui.url_desc = request.POST['url_desc']
        maui.url = request.POST['url']
        maui.system = request.POST['system']
        maui.environ = request.POST['environ']
        maui.login_name = request.POST['login_name']
        maui.login_pwd = request.POST['login_pwd']
        maui.method = request.POST['method']
        maui.state = request.POST['state']
        maui.is_warning = request.POST['is_warning']
        maui.create_by = request.POST['create_by']
        maui.create_time = quTime
        maui.save()
    elif request.method == 'GET':
        # logger.info("查询问题："+request.GET['id'])
        id = request.GET['id']
        questions = QualityService.objects.filter(id=id)
        questions = serializers.serialize("json", questions)
        # print(questions)
    return maui


#    __Desc__ = 从数据库中导出数据到excel数据表中


def download(response):
    cursor = connection.cursor()
    count = cursor.execute('select * from quality_service')
    # 重置游标的位置
    cursor.scroll(0, mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()

    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    workbook = xlwt.Workbook()
    sheet_quality = workbook.add_sheet('quality_service', cell_overwrite_ok=True)

    sheet_quality.write(0, 0, 'id')
    sheet_quality.write(0, 1, '图片上传')
    sheet_quality.write(0, 2, '问题来源')
    sheet_quality.write(0, 3, '系统')
    sheet_quality.write(0, 4, '问题描述')
    sheet_quality.write(0, 5, '解决人')
    sheet_quality.write(0, 6, '反馈结果')
    sheet_quality.write(0, 7, '问题状态')
    sheet_quality.write(0, 8, '是否bug')
    sheet_quality.write(0, 9, '创建时间')
    sheet_quality.write(0, 10, '更新时间')
    sheet_quality.write(0, 11, '原因')

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(results) + 1):
        for col in range(0, len(fields)):
            sheet_quality.write(row, col, u'%s' % results[row - 1][col])

    workbook.save('quality.xls')

    import os
    import io
    path = "./"
    filename_tmp = 'quality.xls'  # quality.xls为将要被下载的文件名
    filename = os.path.join(path, filename_tmp)
    wrapper = FileWrapper(open(filename, "rb"))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="quality.xls"'  # somefilename.csv为下载后的文件名
    return response
