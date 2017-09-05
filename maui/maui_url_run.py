# Filename: run.py
import datetime
import logging
from builtins import dict, type, Exception, str, list
from maui.models import MauiUrlCase
from maui.models import MauiUrl
from django.core import serializers
from . import run
import _thread

from . import login
from way import http_method

logger = logging.getLogger(__name__)


def run_url():
    url_id = 1
    # 这里有一个循环
    maui_url = MauiUrl.objects.filter(id=urlID, state='1')[0]
    system = maui_url.system
    if system in 'app':
        try:
            _thread.start_new_thread(run.run_app, (url_id))
            # _thread.start_new_thread(run.runOther, ())

        except Exception as e:
            logger.error("Error: 无法启动线程" + str(e))
            # print (list(request.POST['id']))
    else:
        try:
            _thread.start_new_thread(run.run_app, (url_id))
            # _thread.start_new_thread(run.runOther, ())

        except Exception as e:
            logger.error("Error: 无法启动线程" + str(e))
