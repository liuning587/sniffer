from django.shortcuts import render, render_to_response
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import indexA
# Create your views here.

# 报警管理
@csrf_exempt
@login_required
def add(request):
    msg = indexA.add(request)
    msg = '添加id：'+str(msg)
    return HttpResponse(msg)



@csrf_exempt
@login_required
def select_all(request):
    indexa = indexA.select_all(request)
    return render_to_response('./a/index_a.html', {'indexa': indexa})


@login_required
@csrf_exempt
def update(request):
    indexa = indexA.update(request)
    return HttpResponse(indexa)
    # return render_to_response('sniffer_warning.html', {'user': user})


def index(request):
    indexa = indexA.select(request)
    return render_to_response('./a/a.html', {'indexa': indexa})

