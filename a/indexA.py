from django.http import HttpResponse
from django.core import serializers
import collections
from a.models import IndexA
from datetime import *
import time
import logging
from builtins import str

logger = logging.getLogger(__name__)


def add(request):
    try:
        if request.method == 'POST':
            index = IndexA(
                url=request.POST['url'],
                url_name=request.POST['url_name'],
                is_blank=request.POST['is_blank'],
                group_name=request.POST['group_name'],
                btn=request.POST['btn'],
            )
            index.save()
            index_id = index.id
    except Exception as e:
        logger.error(str(e))
        index_id = 'N/A'

    return index_id


def select(request):
    if request.method == 'GET':
        index = IndexA.objects.all().order_by("group_name")
        # result_index = {}
        result_index = collections.OrderedDict()
        for c in index:
            result_index[c.group_name] = result_index.get(c.group_name, [])
            result_index[c.group_name].append(c)
            # logger.info(c.group_name)

    return result_index


def select_all(request):
    if request.method == 'GET':
        index = IndexA.objects.all().order_by("id")

    return index


def update(request):
    if request.method == 'POST':
        index = IndexA.objects.get(id=request.POST['id'])
        index.url = request.POST['url']
        index.url_name = request.POST['url_name']
        index.is_blank = request.POST['is_blank']
        index.group_name = request.POST['group_name']
        index.btn = request.POST['btn']
        index.save()

    elif request.method == 'GET':
        logger.info(request.GET['id'])
        id = request.GET['id']
        index = IndexA.objects.filter(id=id)
        index = serializers.serialize("json", index)

    return index
