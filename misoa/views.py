from django.shortcuts import render, render_to_response
import datetime
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import FormtableMain88


# Create your views here.
def online(request):
    # onlineL=online_102.online()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    onlineL = FormtableMain88.online_88()
    # print (onlineL)
    return render_to_response('./misoa/misOnline.html', {'onlineL': onlineL, 'name': '未上线统计', 'present': quTime})


def end_online(request):
    # onlineL=online_102.online()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    result_dict = FormtableMain88.onlined_88()
    onlineL = result_dict['onlinelist']
    conf_update=result_dict['disconf_update']
    disconf_add=result_dict['disconf_add']
    # print (onlineL)
    return render_to_response('./misoa/misOnlineed.html', {'onlineL': onlineL, 'name': '已经上线统计', 'present': quTime,'conf_update':conf_update,'disconf_add':disconf_add})


def today_online(request):
    # onlineL=online_102.online()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    result_dict = FormtableMain88.today_on_online_88()
    onlineL = result_dict['onlinelist']
    conf_update=result_dict['disconf_update']
    disconf_add=result_dict['disconf_add']
    # print (onlineL)
    return render_to_response('./misoa/misOnlineed.html', {'onlineL': onlineL, 'name': '今日上线', 'present': quTime,'conf_update':conf_update,'disconf_add':disconf_add })

# 上线中统计
def on_online(request):
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d %H:%M:%S")
    result_dict = FormtableMain88.on_online_88()
    onlineL = result_dict['onlinelist']
    conf_update=result_dict['disconf_update']
    disconf_add=result_dict['disconf_add']
    # print (onlineL)
    return render_to_response('./misoa/Online.html', {'onlineL': onlineL, 'name': '上线中', 'present': quTime,'conf_update':conf_update,'disconf_add':disconf_add })


def today_online_mail(request):
    # onlineL=online_102.online()
    quTime = datetime.datetime.now()
    quTime = quTime.strftime("%Y-%m-%d")
    result_dict = FormtableMain88.today_on_online_88()
    onlineL = result_dict['onlinelist']
    conf_update=result_dict['disconf_update']
    disconf_add=result_dict['disconf_add']
    # print (onlineL)
    return render_to_response('./misoa/misOnlineed_mail.html', {'onlineL': onlineL, 'name': '今日上线', 'present': quTime,'conf_update':conf_update,'disconf_add':disconf_add })
