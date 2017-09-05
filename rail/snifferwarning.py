from django.http import HttpResponse
from django.core import serializers
from way.models import SnifferWarning
from datetime import *
import time
import logging
from builtins import str

logger = logging.getLogger(__name__)


def add(request):
    try:
        if request.method == 'POST':
            user = SnifferWarning(
                name=request.POST['name'],
                mobile=request.POST['mobile'],
                wxopenid=request.POST['wxopenid'],
                rank=request.POST['rank'],
                system=request.POST['system'],
            )
            user.save()
            user_id = user.id
    except Exception as e:
        logger.error(str(e))
        user_id = 'N/A'

    return user_id


def select(request):
    if request.method == 'GET':
        user = SnifferWarning.objects.all().order_by("id")
    elif request.method == 'POST':
        mobile = request.POST['mobile']
        user = SnifferWarning.objects.filter(mobile=mobile)
        logger.info("按手机查询：" + mobile)
    return user


def update(request):
    if request.method == 'POST':
        user = SnifferWarning.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        user.wxopenid = request.POST['wxopenid']
        user.rank = request.POST['rank']
        user.system = request.POST['system']
        user.save()

    elif request.method == 'GET':
        logger.info(request.GET['id'])
        id = request.GET['id']
        user = SnifferWarning.objects.filter(id=id)
        user = serializers.serialize("json", user)

    return user
