# import os,time,datetime
#
# from statSVN.models import SvnauthUser
# from result.models import SvnCount
# from celery import task
# from __future__ import absolute_import, unicode_literals
# from sniffer.celery import app
# # output = os.popen('cat /proc/cpuinfo')
# # output = os.popen('svn log -r {2016-11-09}:{2016-11-10} http://svn.qdingnet.com/svn/qd/branches/rel_platform2.5')
# # print(type(output))
#
# @app.task
# def monthStat():
#     lastmonth = datetime.datetime.now() + datetime.timedelta(weeks=-4)
#     lastmonth = lastmonth.strftime("%Y-%m-%d")
#     today = datetime.datetime.now().strftime("%Y-%m-%d")
#     output = os.popen('''svn log -r {'''+lastmonth+'}:{'+today+'''} http://svn.qdingnet.com/svn/qd/trunk''')
#    # 获取所有用户
#     svnlog = output.read()
#     # svnuser = SvnauthUser.objects.using('svn').all()
#     svnuser=SvnCount.objects.all()
#     create_at = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
#     create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
#     for user in svnuser:
#         month_count = svnlog.count(user.user_name)
#         user_svn_count = SvnCount.objects.get(user_name = user.user_name)
#         user_svn_count.month_count = month_count
#         user_svn_count.create_at = create_at
#         user_svn_count.save()
#
#     # print(svninfo)
#
#
#     # 周统计结果
# @app.task
# def weeksStat():
#     lastweeks=datetime.datetime.now() + datetime.timedelta(weeks=-1)
#     lastweeks=lastweeks.strftime("%Y-%m-%d")
#     today=datetime.datetime.now().strftime("%Y-%m-%d")
#     output = os.popen('''svn log -r {'''+lastweeks+'}:{'+today+'''} http://svn.qdingnet.com/svn/qd/trunk''')
#    # 获取所有用户
#    #  svnuser = SvnauthUser.objects.using('svn').all()
#     svnuser=SvnCount.objects.all()
#
#     svnlog = output.read()
#     create_at = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
#     create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
#     for user in svnuser:
#         weeks_count = svnlog.count(user.user_name)
#         user_svn_count = SvnCount.objects.get(user_name = user.user_name)
#         user_svn_count.weeks_count = weeks_count
#         user_svn_count.create_at = create_at
#         user_svn_count.save()
#
#
# # 日统计结果
# @app.task
# def dayStat():
#     lastday=datetime.datetime.now() + datetime.timedelta(days=-1)
#     lastday=lastday.strftime("%Y-%m-%d")
#     today= datetime.datetime.now().strftime("%Y-%m-%d")
#     output = os.popen('''svn log -r {'''+lastday+'}:{'+today+'''} http://svn.qdingnet.com/svn/qd/trunk''')
#    # 获取所有用户
#    #  svnuser = SvnauthUser.objects.using('svn').all()
#     svnuser=SvnCount.objects.all()
#     svnlog = output.read()
#     create_at = datetime.datetime.utcnow()+ datetime.timedelta(hours=8)
#     create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
#     for user in svnuser:
#         days_count = svnlog.count(user.user_name)
#         user_svn_count = SvnCount.objects.get(user_name = user.user_name)
#         user_svn_count.date_count = days_count
#         user_svn_count.create_at = create_at
#         user_svn_count.save()
#     print("create_at"+str(create_at))
#
# # 轻易不要用
# def adduser():
#     user_count=SvnCount.objects.all()
#     user_count.delete()
#     # SvnCount.objects.raw("TRUNCATE TABLE svn_count")
#     svnuser = SvnauthUser.objects.using('svn').all()
#     for user in svnuser:
#         fullname=user.full_name
#         # fullname=str(fullname)
#         #
#         # fullname= fullname.encode('utf8')
#         # print(fullname)
#         #
#         # fullname= bytes(fullname)
#         # fullname=fullname.decode('latin-1')
#         # print(fullname)
#         user_svn_count = SvnCount(
#                 user_name = user.user_name,
#                 full_name = user.full_name,
#                 # weeks_count = 0,
#                 # days_count = 0,
#                 # month_count = 0,
#                 create_at = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
#             )
#         user_svn_count.save()
#
#             # .upuser_svn_countdate(weeks_count=weeks_count,create_at=create_at)
#         # user_svn_count = SvnCount.objects.get(user_name = user.user_name).
#         #     user_svn_count = SvnCount(
#         #         user_name = user.user_name,
#         #         weeks_count = svnlog.count(user.user_name),
#         #         create_at = time.time(),
#         #     )
#         #     user_svn_count.save()
#
#         # print(user.user_name)
#         # print(user.user_name+'一共提交:'+str(svnlog.count(user.user_name)))
#
#         # svninfo = output.read().count('xiexiyang')
#
#         # print(svninfo)
#
#
#
# # print(type(output))
#
#
#     # print(lastmonth.strftime("%Y-%m-%d"))
#
#
#
#
#
#     #
#     # localtime = time.localtime(time.time())
#     # print("本地时间为 :", localtime)
#     # print(time.strftime("%Y-%m-%d", time.localtime()))
#     # print(time.strftime("%Y-%m-%d", time.localtime()))
#     # print(datetime.datetime.now() + datetime.timedelta())
#     # lastmonth=datetime.datetime.now() + datetime.timedelta(weeks=-4)
#     # print(lastmonth.strftime("%Y-%m-%d"))
#     # # print(datetime.datetime.now() + datetime.timedelta(weeks=-4))
#     # # print(datetime.datetime.now().strftime("%Y-%m-%d") + datetime.timedelta(weeks=-1))
#     # # print(datetime.datetime.now().strftime("%Y-%m-%d") + datetime.timedelta(days=3))
#     #  # print(time.strftime("%Y-%m-%d", datetime()))
#
