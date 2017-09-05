from qualityS.models import QualityService
import time, datetime
import logging
from django.core import serializers
import xlwt
import pymysql
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.db import connection



# logger = logging.getLogger(__name__)

def add(request):
    quTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    quTime = quTime.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        question = QualityService(
            ques_from=request.POST['ques_from'],
            ques_system=request.POST['ques_system'],
            ques_dsc=request.POST['ques_dsc'],
            ques_to=request.POST['ques_to'],
            ques_result=request.POST['ques_result'],
            ques_status=request.POST['ques_status'],
            is_bug=request.POST['is_bug'],
            create_at=quTime,
            category=request.POST['category'],
            info=request.POST['info'],
        )
        question.save()
        result_id = question.id

    return result_id


def select(request):
    qu_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    qu_time = qu_time.strftime("%Y-")
    if request.method == 'GET':
        questions = QualityService.objects.all().order_by('-id')  # 查询全部
    elif request.method == 'POST':
        if request.POST['month'] == '99':  # 查询全部未解决
            questions = QualityService.objects.filter(ques_status='未解决').order_by('-id')
        elif request.POST['month'] == '2016-12':  # 查询往期
            questions = QualityService.objects.filter(create_at__startswith='2016-12', ).order_by('-id')
        elif request.POST['month']:  # 按月份查询
            month = request.POST['month']
            qu_time = qu_time + month
            questions = QualityService.objects.filter(create_at__startswith=qu_time).order_by('-id')

    # casename = request.POST['casename']
    #     system = request.POST['system']
    #     if system == '':
    #         sniffer = SnifferCases.objects.filter(casename=casename)
    #         logger.info("按用例查询" + casename)
    #     else:
    #         sniffer = SnifferCases.objects.filter(system=system)
    #         logger.info("按系统查询" + system)
    # # sniffer = serializers.serialize("json", sniffer)
    return questions


def update(request):
    quTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    quTime = quTime.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        questions = QualityService.objects.get(id=request.POST['id'])
        questions.category = request.POST['category']
        questions.is_bug = request.POST['is_bug']
        questions.ques_system = request.POST['ques_system']
        questions.ques_dsc = request.POST['ques_dsc']
        questions.ques_result = request.POST['ques_result']
        questions.ques_to = request.POST['ques_to']
        questions.ques_status = request.POST['ques_status']
        questions.update_at = quTime
        questions.save()

    elif request.method == 'GET':
        # logger.info("查询问题："+request.GET['id'])
        id = request.GET['id']
        questions = QualityService.objects.filter(id=id)
        questions = serializers.serialize("json", questions)
        # print(questions)
    return questions


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
