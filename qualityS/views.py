from django.shortcuts import render
from . import questions
# Create your views here.
from django.shortcuts import render, render_to_response
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.http import StreamingHttpResponse
import xlwt
import pymysql


logger = logging.getLogger(__name__)

@csrf_exempt
@login_required
def add(request):
    mes = questions.add(request)
    return render_to_response('addq.html', {'mes': mes})


@login_required
def addQuestion(request):
    mes = ' (N/A) '
    return render_to_response('addq.html', {'mes': mes})


@csrf_exempt
def selectQuestion(request):
    question = questions.select(request)
    logger.info("查询问题记录")
    return render_to_response('questions.html', {'question': question})


def selectid(request):
    msg = questions.update(request)
    return HttpResponse(msg)


def updateQuestion(request):
    mes = ' (N/A) '
    return render_to_response('addq.html', {'mes': mes})


@csrf_exempt
@login_required
def update(request):
    msg = questions.update(request)
    return HttpResponse(msg)

