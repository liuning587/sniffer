from django.shortcuts import render
from . import url
from . import url_case
from . import run
from . import maui_url_run


# Create your views here.
from django.shortcuts import render, render_to_response
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@login_required
def add_url_cases(request):
    mauiurl = url.select(request)
    return render_to_response('./maui/add_url_cases.html', {'url': mauiurl})


def add_url(request):
    return render_to_response('./maui/add_url.html')


def result(request):
    return render_to_response('./maui/result.html')


@csrf_exempt
def select_id(request):
    mauiurl = url.select(request)
    return HttpResponse(mauiurl)


@csrf_exempt
def update(request):
    mauiurl = url.update(request)
    return HttpResponse(mauiurl)


@csrf_exempt
def select_cases(request):
    mauiUrlCases = url_case.update(request)
    return render_to_response('./maui/update_case.html', {'urlCases': mauiUrlCases})

@csrf_exempt
def select_cases_id(request):
    mauiUrlCases = url_case.select(request)

    return HttpResponse(mauiUrlCases)

@csrf_exempt
def update_cases(request):
    mauiUrlCases = url_case.update(request)
    return HttpResponse(mauiUrlCases)

@csrf_exempt
@login_required
def run(request):
    maui_url_run.run_url()

    # try:
    #     _thread.start_new_thread(run.runApp, ())
    #     _thread.start_new_thread(run.runHKApp, ())
    #     _thread.start_new_thread(run.runOther, ())
    #
    # except Exception as e:
    #     logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")




@csrf_exempt
@login_required
def url_add(request):
    mes = url.add(request)
    return render_to_response('./maui/add_url.html', {'mes': mes})


@csrf_exempt
@login_required
def add_cases(request):
    mes = url_case.add_cases(request)
    return HttpResponse(mes)
