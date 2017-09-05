from misoa.models import FormtableMain88
import os, time, datetime, logging
from django.db.models import Q

logger = logging.getLogger(__name__)


def conf_str(value):
    confs = ''
    for con in value.splitlines(keepends=True):
        con = con.strip().replace('<br>', '\r')
        confs = confs + con
    return confs


# 已经上线的
def end_online_88():
    # onlinelist = FormtableMain88.objects.using('misoa').filter(acceptance_completion_time__isnull=True).order_by('-id')
    # onlinelist = FormtableMain88.objects.using('misoa').filter(id=2)
    onlinelist = FormtableMain88.objects.using('misoa').raw('''




  SELECT a.*,h1.lastname as staffing_name,h2.lastname as employee_name,t.selectname as category_name,h3.lastname as on_line_deployment_personnel_name
from
formtable_main_88 a
left  join workflow_SelectItem t on t.selectvalue=a.category
left outer join HrmResource h1 on  h1.id=a.staffing
left outer join HrmResource h2 on h2.id=a.employee
left outer join HrmResource h3 on   h3.id=a.on_line_deployment_personnel
where
a.acceptance_completion_time !=''
and   t.fieldid = 7785
order by a.on_line_deployment_time desc;

    ''')
    mislist = list(onlinelist)
    # print(mislist)
    # for c in onlinelist:
    #     print(c.id)

    return mislist


# 今日上线完成
def today_online_88():
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d")
    # onlinelist = FormtableMain88.objects.using('misoa').filter(id=2)
    onlinelist = FormtableMain88.objects.using('misoa').raw('''



  SELECT a.*,h1.lastname as staffing_name,h2.lastname as employee_name,t.selectname as category_name,h3.lastname as on_line_deployment_personnel_name
from
formtable_main_88 a
left  join workflow_SelectItem t on t.selectvalue=a.category
left outer join HrmResource h1 on  h1.id=a.staffing
left outer join HrmResource h2 on h2.id=a.employee
left outer join HrmResource h3 on   h3.id=a.on_line_deployment_personnel
where
a.on_line_deployment_time =\'''' + timeresult + ''' \'
and   t.fieldid = 7785
order by a.id desc
                                                                                                           ''')
    mislist = list(onlinelist)
    # print (onlinelist)
    return mislist


# 周上线完成
def weeks_online_102():
    runTime = datetime.datetime.utcnow() + datetime.timedelta(weeks=-1)
    timeresult = runTime.strftime("%Y-%m-%d")
    # 2016-11-17 14:21:49
    # print (timeresult)
    onlinelist = FlowData102.objects.using('tdoa').filter(data_72__gte=timeresult).order_by("-data_72")

    return onlinelist


# 上线中
def on_online_88():
    # 查询全部上线中用例
    result_dict = {}
    onlinelist = FormtableMain88.objects.using('misoa').filter(on_line_deployment_time='').exclude(
        actual_on_line_date='')
    # 查询全部上线中用例的disconf编辑数据
    disconf_update = FormtableMain88.objects.using('misoa').raw('''
         select dt1.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt1 dt1 on main.id =dt1.mainid
          where main.actual_on_line_date !='' and main.on_line_deployment_time=''
          order by main.code
    ''')
    # disconflist = list(disconf_update)

    conf_update_str = ''
    code = ''
    for conf_update in disconf_update:

        if code != conf_update.code:
            conf_update_str = conf_update_str + '  <h4>' + '上线单：' + conf_update.code + '  ' + '</h4>'
            if conf_update.configuration_file_name != '':
                conf_update_str = '' + conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' \
                                  + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code

        else:
            if conf_update.configuration_file_name != '':
                conf_update_str = conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code

    # 查询全部上线中用例的disconf新增数据

    disconf_add = FormtableMain88.objects.using('misoa').raw('''
         select dt2.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt2 dt2 on main.id =dt2.mainid
          where main.actual_on_line_date !='' and main.on_line_deployment_time=''
          order by main.code
    ''')
    conf_add_str = ''
    code = ''
    for conf_add in disconf_add:

        if code != conf_add.code:
            conf_add_str = conf_add_str + '  <h4>' + '上线单：' + conf_add.code + '  ' + '</h4>'
            if conf_add.system != '':
                conf_add_str = '' + conf_add_str + '系统：' + conf_add.system + ' 新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code
        else:
            if conf_add.system != '':
                conf_add_str = conf_add_str + '系统：' + conf_add.system + '  新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code

    # 将三组数据放到字典中
    # logger.info("fdsf"+conf_update_str.ge().dfw())
    result_dict['onlinelist'] = onlinelist
    result_dict['disconf_update'] = conf_update_str
    result_dict['disconf_add'] = conf_add_str

    return result_dict


# 今日上线统计
def today_on_online_88():
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d")
    # onlinelist = FormtableMain88.objects.using('misoa').filter(id=2)
    onlinelist = FormtableMain88.objects.using('misoa').raw('''



      SELECT a.*,h1.lastname as staffing_name,h2.lastname as employee_name,t.selectname as category_name,h3.lastname as on_line_deployment_personnel_name
    from
    formtable_main_88 a
    left  join workflow_SelectItem t on t.selectvalue=a.category
    left outer join HrmResource h1 on  h1.id=a.staffing
    left outer join HrmResource h2 on h2.id=a.employee
    left outer join HrmResource h3 on   h3.id=a.on_line_deployment_personnel
    where
    a.on_line_deployment_time =\'''' + timeresult + ''' \'
    and   t.fieldid = 7785
    order by a.id desc
                                                                                                               ''')
    onlinelist = list(onlinelist)
    # 查询全部上线中用例
    result_dict = {}

    disconf_update = FormtableMain88.objects.using('misoa').raw('''
         select dt1.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt1 dt1 on main.id =dt1.mainid
          where main.on_line_deployment_time =\'''' + timeresult + ''' \'
          order by main.code
    ''')
    # disconflist = list(disconf_update)

    conf_update_str = ''
    code = ''
    for conf_update in disconf_update:

        if code != conf_update.code:

            conf_update_str = conf_update_str + '  <h4>' + '上线单：' + conf_update.code + '  ' + '</h4>'
            if conf_update.configuration_file_name != '':

                conf_update_str = '' + conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' \
                                  + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code


        else:
            if conf_update.configuration_file_name != '':
                conf_update_str = conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code

    # 查询全部上线中用例的disconf新增数据

    disconf_add = FormtableMain88.objects.using('misoa').raw('''
         select dt2.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt2 dt2 on main.id =dt2.mainid
          where main.on_line_deployment_time =\'''' + timeresult + ''' \'
          order by main.code
    ''')
    conf_add_str = ''
    code = ''
    for conf_add in disconf_add:

        if code != conf_add.code:
            conf_add_str = conf_add_str + '  <h4>' + '上线单：' + conf_add.code + '  ' + '</h4>'
            if conf_add.system != '':
                conf_add_str = '' + conf_add_str + '系统：' + conf_add.system + ' 新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code
        else:
            if conf_add.system != '':
                conf_add_str = conf_add_str + '系统：' + conf_add.system + '  新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code

    # 将三组数据放到字典中
    result_dict['onlinelist'] = onlinelist
    result_dict['disconf_update'] = conf_update_str
    result_dict['disconf_add'] = conf_add_str

    return result_dict


# 废弃
def online_88():
    # onlinelist = FormtableMain88.objects.using('misoa').filter(acceptance_completion_time__isnull=True).order_by('-id')
    # onlinelist = FormtableMain88.objects.using('misoa').filter(id=2)
    #
    #     onlinelist = FormtableMain88.objects.using('misoa').raw('''SELECT * from formtable_main_88 where acceptance_completion_time =''
    # order by id desc''')


    onlinelist = FormtableMain88.objects.using('misoa').raw('''

  SELECT a.*,h1.lastname as staffing_name,h2.lastname as employee_name,t.selectname as category_name,h3.lastname as on_line_deployment_personnel_name
from
formtable_main_88 a
left  join workflow_SelectItem t on t.selectvalue=a.category
left outer join HrmResource h1 on  h1.id=a.staffing
left outer join HrmResource h2 on h2.id=a.employee
left outer join HrmResource h3 on   h3.id=a.on_line_deployment_personnel
where
a.on_line_deployment_time=''
and   t.fieldid = 7785
order by a.id desc


''')

    mislist = list(onlinelist)

    return mislist


# 已经上线完成
def onlined_88():
    runTime = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    timeresult = runTime.strftime("%Y-%m-%d")
    # onlinelist = FormtableMain88.objects.using('misoa').filter(id=2)
    onlinelist = FormtableMain88.objects.using('misoa').raw('''



      SELECT a.*,h1.lastname as staffing_name,h2.lastname as employee_name,t.selectname as category_name,h3.lastname as on_line_deployment_personnel_name
    from
    formtable_main_88 a
    left  join workflow_SelectItem t on t.selectvalue=a.category
    left outer join HrmResource h1 on  h1.id=a.staffing
    left outer join HrmResource h2 on h2.id=a.employee
    left outer join HrmResource h3 on   h3.id=a.on_line_deployment_personnel
    where
    a.on_line_deployment_time <=\'''' + timeresult + ''' \'
    and   t.fieldid = 7785
    and a.on_line_deployment_time !=''
    order by a.on_line_deployment_time desc
                                                                                                               ''')
    onlinelist = list(onlinelist)
    # 查询全部上线中用例
    result_dict = {}

    disconf_update = FormtableMain88.objects.using('misoa').raw('''
         select dt1.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt1 dt1 on main.id =dt1.mainid
          where main.on_line_deployment_time <=\'''' + timeresult + ''' \'
          order by main.code
    ''')
    # disconflist = list(disconf_update)

    conf_update_str = ''
    code = ''
    for conf_update in disconf_update:

        if code != conf_update.code:
            conf_update_str = conf_update_str + '  <h4>' + '上线单：' + conf_update.code + '  ' + '</h4>'
            if conf_update.configuration_file_name != '':
                conf_update_str = '' + conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' \
                                  + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code

        else:
            if conf_update.configuration_file_name != '':
                conf_update_str = conf_update_str + '系统：' + conf_update.update_config + '<br> 配置文件： ' + conf_update.configuration_file_name

                if conf_update.updated_value != '':
                    conf_update_str = conf_update_str + '<br> 修改：<br> <pre><code>' + conf_str(
                        conf_update.updated_value) + '</code></pre>'
                if conf_update.create_config1 != '':
                    conf_update_str = conf_update_str + '<br> 新增配置项：<br>  <pre><code>' + conf_str(
                        conf_update.create_config1) + '</code></pre><br>'
            code = conf_update.code

    # 查询全部上线中用例的disconf新增数据

    disconf_add = FormtableMain88.objects.using('misoa').raw('''
         select dt2.* ,main.code from [dbo].[formtable_main_88] main
          INNER JOIN formtable_main_88_dt2 dt2 on main.id =dt2.mainid
          where main.on_line_deployment_time <=\'''' + timeresult + ''' \'
          order by main.code
    ''')
    conf_add_str = ''
    code = ''
    for conf_add in disconf_add:

        if code != conf_add.code:
            conf_add_str = conf_add_str + '  <h4>' + '上线单：' + conf_add.code + '  ' + '</h4>'
            if conf_add.system != '':
                conf_add_str = '' + conf_add_str + '系统：' + conf_add.system + ' 新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code
        else:
            if conf_add.system != '':
                conf_add_str = conf_add_str + '系统：' + conf_add.system + '  新配置文件： ' \
                               + conf_add.new_configuration_file_name + '参考：' + conf_add.reference_environment + '<br>'

            code = conf_add.code

    # 将三组数据放到字典中
    result_dict['onlinelist'] = onlinelist
    result_dict['disconf_update'] = conf_update_str
    result_dict['disconf_add'] = conf_add_str

    return result_dict
