from builtins import list

import os,time,datetime

from result.models import SvnCount
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
import logging

logger = logging.getLogger(__name__)

def svnCountreslut():


    user_svn_count = SvnCount.objects.exclude(user_name__icontains='lh_').order_by("month_count")\
        .values('user_name','month_count','weeks_count','date_count','create_at')
    logger.info("获取到图表信息")
    user_svn_count = json.dumps(list(user_svn_count), cls=DjangoJSONEncoder)

    return user_svn_count

def svnCount():
    logger.info("进行svn统计")

    user_svn_count = SvnCount.objects.exclude(user_name__icontains='lh_').order_by("-month_count")\
        .values('user_name','month_count','weeks_count','date_count','create_at')
    logger.info("获取到图表信息")
    # user_svn_count = json.dumps(list(user_svn_count), cls=DjangoJSONEncoder)

    return user_svn_count