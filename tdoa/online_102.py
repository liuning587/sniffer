
from tdoa.models import FlowRun,FlowData102
import os,time,datetime,logging
from django.db import connections
from django.db.models import Q


logger = logging.getLogger(__name__)
# 查询正在执行的上线单
def online():
    onlinelist = FlowRun.objects.using('tdoa').filter(flow_id='102',end_time__isnull=True).order_by("-begin_time")

    return onlinelist

def end_online():
    onlinelist = FlowRun.objects.using('tdoa').filter(flow_id='102',end_time__isnull=False).order_by("-end_time")

    return onlinelist

def today_online():
    runTime = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowRun.objects.using('tdoa').filter(flow_id='102',end_time__gte= timeresult ).order_by("-begin_time")

    return onlinelist

def weeks_online():
    runTime = datetime.datetime.utcnow()+ datetime.timedelta(weeks=-1)
    timeresult = runTime.strftime("%Y-%m-%d")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowRun.objects.using('tdoa').filter(flow_id='102',end_time__gte= timeresult ).order_by("-end_time")

    return onlinelist

# 已经上线的
def end_online_102():
    onlinelist = FlowData102.objects.using('tdoa').exclude(data_72='').order_by("-data_72")
    return onlinelist


# 今日上线完成
def today_online_102():
    runTime = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowData102.objects.using('tdoa').filter(data_72__gte= timeresult ).order_by("-data_72")

    return onlinelist


# 周上线完成
def weeks_online_102():
    runTime = datetime.datetime.utcnow()+ datetime.timedelta(weeks=-1)
    timeresult = runTime.strftime("%Y-%m-%d")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowData102.objects.using('tdoa').filter(data_72__gte= timeresult ).order_by("-data_72")

    return onlinelist


# 本月上线完成
def month_online_102():
    runTime = datetime.datetime.utcnow()
    timeresult = runTime.strftime("%Y-%m")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowData102.objects.using('tdoa').filter(data_72__gte= timeresult ).order_by("-data_72")

    return onlinelist


def online_102():
    end_error = FlowRun.objects.using('tdoa').filter(end_time__isnull=True,flow_id= 102,del_flag = 0).values('run_id')
    endoalist=[]
    for end_oa in end_error:
        endoalist.append(end_oa['run_id'])
    onlinelist = FlowData102.objects.using('tdoa').filter(data_72='',run_id__in=endoalist).exclude(data_3='').order_by("-begin_time")
    return onlinelist