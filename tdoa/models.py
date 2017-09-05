# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models


class FlowRun(models.Model):
    run_id = models.IntegerField(db_column='RUN_ID',primary_key=True)  # Field name made lowercase.
    run_name = models.CharField(db_column='RUN_NAME', max_length=200)  # Field name made lowercase.
    flow_id = models.IntegerField(db_column='FLOW_ID')  # Field name made lowercase.
    begin_user = models.CharField(db_column='BEGIN_USER', max_length=40)  # Field name made lowercase.
    begin_dept = models.IntegerField(db_column='BEGIN_DEPT')  # Field name made lowercase.
    begin_time = models.DateTimeField(db_column='BEGIN_TIME')  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    attachment_id = models.TextField(db_column='ATTACHMENT_ID')  # Field name made lowercase.
    attachment_name = models.TextField(db_column='ATTACHMENT_NAME')  # Field name made lowercase.
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=1)  # Field name made lowercase.
    focus_user = models.TextField(db_column='FOCUS_USER')  # Field name made lowercase.
    parent_run = models.IntegerField(db_column='PARENT_RUN')  # Field name made lowercase.
    from_user = models.CharField(db_column='FROM_USER', max_length=20)  # Field name made lowercase.
    aip_files = models.TextField(db_column='AIP_FILES')  # Field name made lowercase.
    pre_set = models.TextField(db_column='PRE_SET')  # Field name made lowercase.
    view_user = models.TextField(db_column='VIEW_USER')  # Field name made lowercase.
    archive = models.IntegerField(db_column='ARCHIVE')  # Field name made lowercase.
    force_over = models.TextField(db_column='FORCE_OVER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flow_run'




class FlowData102(models.Model):
    # flowrun = models.ForeignKey(FlowRun)
    id = models.AutoField(primary_key=True)
    run_id = models.IntegerField(unique=True)
    run_name = models.CharField(max_length=200) #流程单名称
    begin_user = models.CharField(max_length=20) #发起人
    begin_time = models.DateTimeField(blank=True, null=True) #发起时间
    flow_auto_num = models.IntegerField()
    data_1 = models.TextField()
    data_2 = models.TextField() #发起人名字
    data_3 = models.TextField() #流程单详情
    data_4 = models.TextField()
    data_5 = models.TextField()
    data_6 = models.TextField()
    data_7 = models.TextField() #预计上线时间
    data_8 = models.TextField()
    data_17 = models.TextField()
    data_9 = models.TextField() #研发分配开始时间，进入开发
    data_20 = models.TextField() #研发
    data_11 = models.TextField()
    data_12 = models.TextField()
    data_13 = models.TextField()
    data_14 = models.TextField()
    data_15 = models.TextField()
    data_16 = models.TextField()
    data_18 = models.TextField()
    data_19 = models.TextField()
    data_21 = models.TextField()
    data_22 = models.TextField()  #测试分配时间，进入测试
    data_23 = models.TextField()
    data_24 = models.TextField()
    data_26 = models.TextField()
    data_25 = models.TextField()
    data_27 = models.TextField()
    data_28 = models.TextField()
    data_29 = models.TextField()
    data_31 = models.TextField()
    data_32 = models.TextField()
    data_33 = models.TextField()
    data_34 = models.TextField()
    data_35 = models.TextField()
    data_36 = models.TextField()
    data_37 = models.TextField()
    data_38 = models.TextField()
    data_39 = models.TextField()
    data_40 = models.TextField()
    data_41 = models.TextField()
    data_43 = models.TextField()
    data_42 = models.TextField()
    data_44 = models.TextField()
    data_45 = models.TextField() #质量验收人
    data_46 = models.TextField()
    data_49 = models.TextField()
    data_48 = models.TextField()
    data_47 = models.TextField()
    data_50 = models.TextField() #项目负责人
    data_53 = models.TextField()
    data_51 = models.TextField()
    data_52 = models.TextField()
    data_54 = models.TextField()
    data_55 = models.TextField()
    data_56 = models.TextField()
    data_57 = models.TextField()
    data_58 = models.TextField()
    data_59 = models.TextField()
    data_60 = models.TextField()
    data_61 = models.TextField()
    data_63 = models.TextField()
    data_62 = models.TextField()
    data_66 = models.TextField()
    data_67 = models.TextField()
    data_68 = models.TextField()
    data_70 = models.TextField()
    data_72 = models.TextField() #验收时间
    data_74 = models.TextField() #预计开发时间
    data_75 = models.TextField() #预计提测时间
    data_76 = models.TextField() #线单类别



    class Meta:
        managed = False
        db_table = 'flow_data_102'
