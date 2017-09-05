from django.shortcuts import render, render_to_response
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rail.models import SnifferCases
from . import sniffercases
from . import snifferwarning
import time


@csrf_exempt
@login_required
def add(request):
    mes = sniffercases.add(request)
    return HttpResponse("新增脚本成功用例id：   " + str(mes))


def update(request):
    return HttpResponse("修改脚本")


@csrf_exempt
def select(request):
    snifferCa = sniffercases.select(request)
    return render_to_response('cases_select.html', {'snifferCa': snifferCa})


def index(request):
    # return HttpResponse("欢迎光临snibffer用例管理系统")
    return render_to_response('index.html')


@login_required
def addCases(request):
    return render_to_response('add.html')


@login_required
def selectCases(request):
    # return HttpResponse("欢迎光临snibffer用例管理系统")
    return render_to_response('select.html')


@login_required
@csrf_exempt
def update(request):
    msg = sniffercases.update(request)
    return HttpResponse(msg)


@login_required
def selectid(request):
    msg = sniffercases.update(request)
    return HttpResponse(msg)
    # return render_to_response('cases_select2.html',{'msg': msg})


# 报警管理
@csrf_exempt
@login_required
def add_warning_user(request):
    msg = snifferwarning.add(request)
    msg = '添加用户id：'+str(msg)
    return HttpResponse(msg)



@csrf_exempt
@login_required
def select_warning_user(request):
    user = snifferwarning.select(request)
    return render_to_response('sniffer_warning.html', {'user': user})


@login_required
@csrf_exempt
def update_user(request):
    user = snifferwarning.update(request)
    return HttpResponse(user)
    # return render_to_response('sniffer_warning.html', {'user': user})


