from django.http import HttpResponse
from django.core import serializers
from rail.models import SnifferCases
from datetime import *
import time
import logging
from builtins import str

logger = logging.getLogger(__name__)



def add(request):
    if request.method == 'POST':
         cases = SnifferCases(
             casename=request.POST['casename'],
             create_by=request.POST['create_by'],
             system=request.POST['system'],
             url=request.POST['url'],
             data=request.POST['data'],
             method=request.POST['method'],
             expect=request.POST['expect'],
             emailto=request.POST['emailto'],
             state=request.POST['state'],
             is_warning=request.POST['is_warning'],
             create_at=time.time(),
         )
         cases.save()
         result_id = cases.id

    return result_id


def select(request):
    if request.method=='GET':
       sniffer = SnifferCases.objects.all().order_by("system")
    elif request.method=='POST':
         casename=request.POST['casename']
         system=request.POST['system']
         if system=='':
            sniffer = SnifferCases.objects.filter(casename=casename)
            logger.info("按用例查询"+casename)
         else:
            sniffer = SnifferCases.objects.filter(system=system)
            logger.info("按系统查询"+system)
    # sniffer = serializers.serialize("json", sniffer)
    return sniffer


def update(request):
    if request.method == 'POST':
          sniffer=SnifferCases.objects.get(id=request.POST['id'])
          sniffer.casename=request.POST['casename']
          sniffer.system=request.POST['system']
          sniffer.method=request.POST['method']
          sniffer.url=request.POST['url']
          sniffer.data=request.POST['data']
          sniffer.expect=request.POST['expect']
          sniffer.state=request.POST['state']
          sniffer.emailto=request.POST['emailto']
          sniffer.is_warning=request.POST['is_warning']
          sniffer.save()

    elif request.method == 'GET':
        logger.info(request.GET['id'])
        id=request.GET['id']
        sniffer = SnifferCases.objects.filter(id=id)
        sniffer = serializers.serialize("json", sniffer)

    return sniffer
