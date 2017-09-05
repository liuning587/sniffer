from django.test import TestCase
import os,time,datetime
# Create your tests here.
from django.test import TestCase

# Create your tests here.
import os
# output = os.popen('cat /proc/cpuinfo')
# output = os.popen('svn log -r {2016-11-09}:{2016-11-10} http://svn.qdingnet.com/svn/qd/branches/rel_platform2.5')
# # print(type(output))
#
# svninfo = output.read().count('zhaotong')
# print(svninfo)

lastday=datetime.datetime.now() + datetime.timedelta(days=1)
lastday=lastday.strftime("%Y-%m-%d")
print (lastday)
today= datetime.datetime.now().strftime("%Y-%m-%d")
print (today)

# 10.37.253.32:3306
# grant select On svn.* to zhaochunyu@'10.%.%.%' identified by  '=3u*)n3Z' ;
# #
# svninfolist=svninfo.split("------------------------------------------------------------------------")
# # print(svninfolist)
# # print(svninfolist.count("zhaotong"))
# svninfolist.remove('')
# for listuser in svninfolist:
#
#     svnname=listuser.split('|')
#     svnname.pop()
#     print(svnname)
#     # svnname.remove(r'\n')
#     print(svnname[1])
#     # print(listuser.split("|")[1])
#


# print(output.read())
# print(output.next())
# for index in range(5):
#     # line = next(output)
#     print ("第 %d 行 - %s" % (index, line))

# svn log -r {2016-11-09}:{2016-11-10} http://svn.qdingnet.com/svn/qd/branches/rel_platform2.5
# os.system('cat /proc/cpuinfo')