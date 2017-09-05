from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from . import stat
from django.contrib.auth.decorators import login_required
import _thread


@login_required
def monthStat(request):
    try:
        _thread.start_new_thread(stat.monthStat, ())
    except Exception as e:
        print("Error: 无法启动线程" + str(e))

    return HttpResponse("月度统计结果进行中，可刷新统计列")


@login_required
def weeksStat(request):
    try:
        _thread.start_new_thread(stat.monthStat, ())
        _thread.start_new_thread(stat.weeksStat, ())
    except Exception as e:
        print("Error: 无法启动线程" + str(e))

    return HttpResponse("月周统计结果进行中，可刷新统计列")


def dayStat(request):
    try:
        _thread.start_new_thread(stat.monthStat, ())
        _thread.start_new_thread(stat.weeksStat, ())
        _thread.start_new_thread(stat.dayStat, ())
    except Exception as e:
        print("Error: 无法启动线程" + str(e))

    return HttpResponse("月周日统计结果进行中，可刷新统计列表")


def adduser(request):
    stat.adduser()
    return HttpResponse("添加用户")
