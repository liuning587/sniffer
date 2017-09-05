from django.shortcuts import render, render_to_response
import datetime
import _thread
from . import svncount
from . import sniffer_result
from . import online_mail

from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse


def result(request):
    return HttpResponse("执行结果")


def index(request):
    return HttpResponse("欢迎光临snibffer结果查询系统")


def statistics(request):
    return HttpResponse("统计系统")


def sniffercount(request):
    snifferRe = sniffer_result.resultC()
    runTime = snifferRe.get('time')
    del snifferRe['time']
    return render_to_response('result.html', {'snifferRe': snifferRe, 'timeresult': runTime})


def svn_count(request):
    svnresult = svncount.svnCount()
    return render_to_response('svn_count.html', {'svncount': svnresult})


def svn_chart(request):
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d %H:%M:%S")
    svnresult = svncount.svnCountreslut()
    return render_to_response('svn_chart.html', {'svncount': svnresult, 'timeresult': timeresult})


# 工作日自动化发送上线公告
def img_email(request):
    try:
        _thread.start_new_thread(online_mail.htmlToImg, ())
    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("发送中，请稍后查看邮件。")

    # return HttpResponse(result)
