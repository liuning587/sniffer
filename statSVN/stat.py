import os, time, datetime
from statSVN.models import SvnauthUser
from result.models import SvnCount


# output = os.popen('cat /proc/cpuinfo')
# output = os.popen('svn log -r {2016-11-09}:{2016-11-10} http://svn.qdingnet.com/svn/qd/branches/rel_platform2.5')
# print(type(output))


def monthStat():
    lastmonth = datetime.datetime.now() + datetime.timedelta(weeks=-4)
    lastmonth = lastmonth.strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    lastmonth = '2017-08-01'
    today = '2017-09-01'
    # print(type(today))

    output = os.popen('''svn log -r {''' + lastmonth + '}:{' + today + '''} http://svn.qdingnet.com/svn/qd/trunk''')
    # 获取所有用户
    svnlog = output.read()
    # print(svnlog)
    # svnuser = SvnauthUser.object s.using('svn').all()
    svnuser = SvnCount.objects.all()
    create_at = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
    for user in svnuser:
        month_count = svnlog.count(user.user_name)
        user_svn_count = SvnCount.objects.get(user_name=user.user_name)
        user_svn_count.month_count = month_count
        user_svn_count.create_at = create_at
        user_svn_count.save()

        print(user_svn_count)
    print('over')


        # 周统计结果


def weeksStat():
    lastweeks = datetime.datetime.now() + datetime.timedelta(weeks=-1)
    lastweeks = lastweeks.strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    output = os.popen('''svn log -r {''' + lastweeks + '}:{' + today + '''} http://svn.qdingnet.com/svn/qd/trunk''')
    # 获取所有用户
    #  svnuser = SvnauthUser.objects.using('svn').all()
    svnuser = SvnCount.objects.all()

    svnlog = output.read()
    create_at = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
    for user in svnuser:
        weeks_count = svnlog.count(user.user_name)
        user_svn_count = SvnCount.objects.get(user_name=user.user_name)
        user_svn_count.weeks_count = weeks_count
        user_svn_count.create_at = create_at
        user_svn_count.save()
        # print(user.user_name)


# 日统计结果
def dayStat():
    lastday = datetime.datetime.now() + datetime.timedelta(days=1)
    lastday = lastday.strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    output = os.popen('''svn log -r {''' + today + '}:{' + lastday + '''} http://svn.qdingnet.com/svn/qd/trunk''')
    # 获取所有用户
    #  svnuser = SvnauthUser.objects.using('svn').all()
    svnuser = SvnCount.objects.all()
    svnlog = output.read()
    create_at = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    create_at = create_at.strftime("%Y-%m-%d %H:%M:%S")
    for user in svnuser:
        days_count = svnlog.count(user.user_name)
        user_svn_count = SvnCount.objects.get(user_name=user.user_name)
        user_svn_count.date_count = days_count
        user_svn_count.create_at = create_at
        user_svn_count.save()
    print("create_at" + str(create_at))


# 轻易不要用
def adduser():
    user_count = SvnCount.objects.all()
    user_count.delete()
    svnuser = SvnauthUser.objects.using('svn').all()
    for user in svnuser:
        user_svn_count = SvnCount(
            user_name=user.user_name,
            full_name=user.full_name,
            # weeks_count='0',
            # days_count='0',
            # month_count='0',
            create_at=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
        )
        user_svn_count.save()
