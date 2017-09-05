from builtins import Exception, str

from django.shortcuts import render
import _thread
import logging
# Create your views here.
from django.http import HttpResponse
from . import run
from . import sockets
from multiprocessing import Process
from django.contrib.auth.decorators import login_required

# import run
logger = logging.getLogger(__name__)


# 之前使用线程，现在使用进程进行，但无法解决系统内的并发问题，目前还是系统内顺序执行。

# @login_required
def runApp(request):
    try:
        Process(target=run.runBAMApp, args=()).start()
        Process(target=run.runApp, args=()).start()
        Process(target=run.runHKApp, args=()).start()
    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")


def quartz(request):
    return HttpResponse("设计定时")


# boss property shanghu finance
def runall(request):
    try:
        Process(target=run.runApp, args=()).start()
        Process(target=run.runApp, args=('HKapp',)).start()
        Process(target=run.runApp, args=('BAMApp',)).start()
        Process(target=sockets.reply_socket, args=()).start()
        Process(target=run.runBo, args=('m2',)).start()
        Process(target=run.runBo, args=('boss',)).start()
        Process(target=run.runBo, args=('property',)).start()
        Process(target=run.runBo, args=('shanghu',)).start()
        Process(target=run.runBo, args=('wave',)).start()
        Process(target=run.runBo, args=('Compass',)).start()
    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本进行中")


# @login_required
def runm2(request):
    try:
        Process(target=run.runBo, args=('m2',)).start()
    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")


# @login_required
def runother(request):
    try:
        Process(target=run.runBo, args=('m2',)).start()
        Process(target=run.runBo, args=('boss',)).start()
        Process(target=run.runBo, args=('property',)).start()
        Process(target=run.runBo, args=('shanghu',)).start()

        # Process(target=run.runBo, args=('wave',)).start()
        # Process(target=run.runBo, args=('boss',)).start()
        # Process(target=run.runBo, args=('property',)).start()
        # Process(target=run.runBo, args=('shanghu',)).start()
        # Process(target=run.runProperty(), args=()).start()
        # Process(target=run.runBo, args=('finance',)).start()
    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")


@login_required
def runBAMApp(request):
    try:
        Process(target=run.runBAMApp, args=()).start()
        # _thread.start_new_thread(run.runHKApp, ())

    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")


# @login_required
def runCompass(request):
    try:
        Process(target=run.runBo, args=('Compass',)).start()
        Process(target=run.runBo, args=('wave',)).start()

    except Exception as e:
        logger.error("Error: 无法启动线程" + str(e))
    return HttpResponse("执行脚本")


def index(request):
    return HttpResponse("执行脚本")


def r_socket(request):
    sockets.reply_socket()
    return HttpResponse("执行sockets脚本")


def test(request):
    mobile = run.get_warning_mobile()

    logger.info(mobile)
    openids = run.get_warning_open()
    logger.info(openids)

    return HttpResponse("执行脚本")
