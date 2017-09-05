from django.shortcuts import render, render_to_response
import datetime
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import online_102


# import

def online(request):


    # onlineL=online_102.online()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    onlineL = online_102.online_102()
    return render_to_response('online.html', {'onlineL': onlineL, 'name': '未上线统计', 'present': quTime})


def end_online(request):
    # onlineL=online_102.end_online()
    onlineL = online_102.end_online_102()

    return render_to_response('online.html', {'onlineL': onlineL, 'name': '已经上线统计'})


def today_online(request):
    # onlineL=online_102.today_online()
    onlineL = online_102.today_online_102()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    return render_to_response('online.html', {'onlineL': onlineL, 'name': '今日上线统计','present': quTime})


def weeks_online(request):
    # onlineL=online_102.weeks_online()
    onlineL = online_102.weeks_online_102()
    return render_to_response('online.html', {'onlineL': onlineL, 'name': '近一周上线统计'})


def month_online(request):
    # onlineL=online_102.weeks_online()
    onlineL = online_102.month_online_102()
    return render_to_response('online.html', {'onlineL': onlineL, 'name': '本月上线统计'})
