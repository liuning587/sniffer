# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
# 
# 
# class FormtableMain16(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     attachment = models.TextField()
#     comment = models.TextField()
#     request_reason = models.TextField()
#     send_rule = models.TextField()
#     publish_date = models.CharField(max_length=200)
#     publish_time = models.CharField(max_length=200)
#     development_personnel = models.IntegerField()
#     comment1 = models.TextField()
#     code = models.CharField(max_length=200)
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_16'
# 
# 
# class FormtableMain17(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     attachment = models.TextField()
#     comment = models.TextField()
#     request_reason = models.TextField()
#     sql_comment = models.TextField()
#     fin_related = models.CharField(max_length=200)
#     code = models.CharField(max_length=200)
#     select_rd_personnel = models.IntegerField()
#     technical_leader_remarks = models.TextField()
#     sql_implementation_notes = models.TextField()
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_17'
# 
# 
# class FormtableMain19(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     attachment = models.TextField()
#     comment = models.TextField()
#     request_reason = models.TextField()
#     online_date = models.CharField(max_length=200)
#     business = models.IntegerField()
#     start_date = models.CharField(max_length=200)
#     end_date = models.CharField(max_length=200)
#     product_personnel = models.IntegerField(db_column='Product_personnel')  # Field name made lowercase.
#     development_personnel = models.IntegerField()
#     go_online_personnel = models.IntegerField()
#     comment1 = models.TextField()
#     comment2 = models.TextField()
#     comment3 = models.TextField()
#     activity = models.CharField(max_length=200)
#     code = models.CharField(max_length=200)
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_19'
# 
# 
# class FormtableMain21(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     abstract = models.TextField()
#     attachment = models.TextField()
#     comment = models.TextField()
#     fin_related = models.CharField(max_length=200)
#     excel_use = models.TextField()
#     code = models.CharField(max_length=200)
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_21'
# 
# 
# class FormtableMain69(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     title = models.CharField(max_length=200)
#     department = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     ver_number = models.CharField(max_length=200)
#     function_introduction = models.TextField()
#     attachment = models.TextField()
#     comment1 = models.TextField()
#     code = models.CharField(max_length=200)
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_69'
# 
# 
# class FormtableMain8(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     attachment = models.TextField()
#     comment = models.TextField()
#     budget = models.CharField(max_length=200)
#     activity_name = models.CharField(db_column='Activity_name')  # Field name made lowercase.
#     nominal_amount = models.TextField()
#     valid_period = models.TextField()
#     rule1 = models.TextField()
#     path = models.TextField()
#     activity_all = models.IntegerField()
#     estimated_use_quantity = models.IntegerField()
#     use_rule = models.TextField()
#     code = models.CharField(max_length=200)
#     shop = models.CharField(max_length=200)
#     type_of_opera = models.CharField(max_length=200)
#     apply_for_coupons = models.IntegerField()
#     apply_for_integral = models.IntegerField()
#     integral_application_details = models.TextField()
#     o_poly = models.CharField(max_length=200)
#     tool = models.CharField(max_length=200)
#     tourism = models.CharField(max_length=200)
#     member = models.CharField(max_length=200)
#     marketing = models.CharField(max_length=200)
#     coupon_type = models.IntegerField()
#     budget_limit = models.IntegerField()
#     coupon_start_date = models.CharField(max_length=200)
#     coupon_end_date = models.CharField(max_length=200)
#     apply_for_property_charges = models.IntegerField()
#     need_to_apply_for_a_coupon = models.IntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_8'
# 

class FormtableMain88(models.Model):
    requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
    department = models.IntegerField()
    code = models.CharField(max_length=200)
    employee = models.IntegerField()
    request_date = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    attachment = models.TextField()
    entry_name = models.CharField(max_length=200)
    project_profile = models.TextField()
    rd_personnel = models.IntegerField()
    development_date = models.CharField(max_length=200)
    date_of_survey = models.CharField(max_length=200)
    on_line_date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    sql_file_path = models.CharField(max_length=200)
    profile_change_details = models.TextField()
    staffing = models.IntegerField()
    research_note = models.TextField()
    category = models.IntegerField()
    qa_database = models.CharField(max_length=200)
    configure_accessories = models.TextField()
    configuration_notes = models.TextField()
    test_start_time = models.CharField(max_length=200)
    estimated_time_on_line = models.CharField(max_length=200)
    test_conclusion = models.TextField()
    on_line_confirmation = models.IntegerField()
    actual_on_line_time = models.CharField(max_length=200)
    on_line_deployment_personnel = models.IntegerField()
    confirm_on_line_remarks = models.TextField()
    data_base = models.CharField(max_length=200)
    on_line_deployment_time = models.CharField(max_length=200)
    emergency_line = models.CharField(max_length=200)
    online_system = models.TextField()
    data_base1 = models.CharField(max_length=200)
    configuration_file = models.CharField(max_length=200)
    add_menu = models.CharField(max_length=200)
    fill_in_the_qa = models.TextField()
    test_result1 = models.IntegerField()
    confirmation_of_operation = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    test_start_date = models.CharField(max_length=200)
    acceptance_completion_time = models.CharField(max_length=200) #验收完成时间
    test_assignment_remarks = models.TextField()
    special_approver = models.IntegerField()
    operation_confirmation = models.CharField(max_length=200)
    select_project_leader = models.IntegerField()
    select_quality_person = models.IntegerField()
    operational_opinion = models.IntegerField()
    operation_confirmation_remarks = models.TextField()
    on_line_deployment_date = models.CharField(max_length=200)
    actual_on_line_date = models.CharField(max_length=200)
    operation_confirmation1 = models.IntegerField()
    emergency_line1 = models.IntegerField()
    menu_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'formtable_main_88'


# class FormtableMain99(models.Model):
#     requestid = models.IntegerField(db_column='requestId')  # Field name made lowercase.
#     department = models.IntegerField()
#     link_order = models.IntegerField()
#     code = models.CharField(max_length=200)
#     countersign = models.TextField()
#     document = models.IntegerField()
#     employee = models.IntegerField()
#     request_date = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     attachment = models.TextField()
#     comment = models.TextField()
#     abstract = models.TextField()
#     open_user = models.CharField(max_length=200)
#     subordinate_department = models.IntegerField()
#     svn_route = models.TextField()
#     jurisdiction = models.IntegerField()
#     email_address = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'formtable_main_99'
#
#
# class WorkflowBase(models.Model):
#     id = models.IntegerField()
#     workflowname = models.CharField(max_length=200)
#     workflowdesc = models.CharField(max_length=200)
#     workflowtype = models.IntegerField()
#     securelevel = models.CharField(max_length=200)
#     formid = models.IntegerField()
#     userid = models.IntegerField()
#     isbill = models.CharField(max_length=200)
#     iscust = models.IntegerField()
#     helpdocid = models.IntegerField()
#     isvalid = models.CharField(max_length=200)
#     needmark = models.CharField(max_length=200)
#     messagetype = models.IntegerField(db_column='messageType')  # Field name made lowercase.
#     multisubmit = models.IntegerField(db_column='multiSubmit')  # Field name made lowercase.
#     defaultname = models.IntegerField(db_column='defaultName')  # Field name made lowercase.
#     docpath = models.CharField(db_column='docPath')  # Field name made lowercase.
#     subcompanyid = models.IntegerField()
#     mailmessagetype = models.IntegerField(db_column='mailMessageType')  # Field name made lowercase.
#     docrightbyoperator = models.IntegerField(db_column='docRightByOperator')  # Field name made lowercase.
#     doccategory = models.CharField(db_column='docCategory')  # Field name made lowercase.
#     istemplate = models.CharField(max_length=200)
#     templateid = models.IntegerField()
#     catelogtype = models.IntegerField(db_column='catelogType')  # Field name made lowercase.
#     selectedcatelog = models.IntegerField(db_column='selectedCateLog')  # Field name made lowercase.
#     docrightbyhrmresource = models.IntegerField(db_column='docRightByHrmResource')  # Field name made lowercase.
#     needaffirmance = models.CharField(db_column='needAffirmance')  # Field name made lowercase.
#     isremarks = models.CharField(max_length=200)
#     isannexupload = models.CharField(db_column='isannexUpload')  # Field name made lowercase.
#     annexdoccategory = models.CharField(max_length=200)
#     isshowonreportinput = models.CharField(db_column='isShowOnReportInput')  # Field name made lowercase.
#     titlefieldid = models.IntegerField(db_column='titleFieldId')  # Field name made lowercase.
#     keywordfieldid = models.IntegerField(db_column='keywordFieldId')  # Field name made lowercase.
#     isshowchart = models.CharField(max_length=200)
#     orderbytype = models.CharField(max_length=200)
#     istridiffworkflow = models.CharField(db_column='isTriDiffWorkflow')  # Field name made lowercase.
#     ismodifylog = models.CharField(db_column='isModifyLog')  # Field name made lowercase.
#     ifversion = models.CharField(db_column='ifVersion')  # Field name made lowercase.
#     wfdocpath = models.CharField(max_length=200)
#     wfdocowner = models.CharField(max_length=200)
#     isedit = models.CharField(db_column='isEdit')  # Field name made lowercase.
#     editor = models.IntegerField()
#     editdate = models.CharField(max_length=200)
#     edittime = models.CharField(max_length=200)
#     showdelbuttonbyreject = models.CharField(db_column='ShowDelButtonByReject')  # Field name made lowercase.
#     showuploadtab = models.CharField(db_column='showUploadTab')  # Field name made lowercase.
#     issigndoc = models.CharField(db_column='isSignDoc')  # Field name made lowercase.
#     showdoctab = models.CharField(db_column='showDocTab')  # Field name made lowercase.
#     issignworkflow = models.CharField(db_column='isSignWorkflow')  # Field name made lowercase.
#     showworkflowtab = models.CharField(db_column='showWorkflowTab')  # Field name made lowercase.
#     candelacc = models.CharField(max_length=200)
#     isforwardrights = models.CharField(max_length=200)
#     isimportwf = models.CharField(max_length=200)
#     isrejectremind = models.CharField(max_length=200)
#     ischangrejectnode = models.CharField(max_length=200)
#     wfdocownertype = models.IntegerField()
#     wfdocownerfieldid = models.IntegerField()
#     newdocpath = models.CharField(max_length=200)
#     keepsign = models.IntegerField()
#     seccategoryid = models.IntegerField(db_column='secCategoryId')  # Field name made lowercase.
#     custompage = models.CharField(max_length=200)
#     issignview = models.IntegerField()
#     isselectrejectnode = models.CharField(db_column='IsSelectrejectNode')  # Field name made lowercase.
#     forbidattdownload = models.IntegerField(db_column='forbidAttDownload')  # Field name made lowercase.
#     isimportdetail = models.CharField(db_column='isImportDetail')  # Field name made lowercase.
#     specialapproval = models.CharField(db_column='specialApproval')  # Field name made lowercase.
#     frequency = models.IntegerField(db_column='Frequency')  # Field name made lowercase.
#     cycle = models.CharField(db_column='Cycle')  # Field name made lowercase.
#     nosynfields = models.CharField(max_length=200)
#     isneeddelacc = models.CharField(max_length=200)
#     sapsource = models.CharField(db_column='SAPSource')  # Field name made lowercase.
#     isfnacontrol = models.CharField(max_length=200)
#     fnanodeid = models.CharField(max_length=200)
#     fnadepartmentid = models.CharField(max_length=200)
#     smsalertstype = models.CharField(db_column='smsAlertsType')  # Field name made lowercase.
#     forwardreceivedef = models.CharField(db_column='forwardReceiveDef')  # Field name made lowercase.
#     issavecheckform = models.CharField(db_column='isSaveCheckForm')  # Field name made lowercase.
#     archivenomsgalert = models.CharField(db_column='archiveNoMsgAlert')  # Field name made lowercase.
#     archivenomailalert = models.CharField(db_column='archiveNoMailAlert')  # Field name made lowercase.
#     isfnabudgetwf = models.CharField(max_length=200)
#     chatstype = models.IntegerField(db_column='chatsType')  # Field name made lowercase.
#     chatsalerttype = models.IntegerField(db_column='chatsAlertType')  # Field name made lowercase.
#     notremindifarchived = models.IntegerField(db_column='notRemindifArchived')  # Field name made lowercase.
#     isworkflowdoc = models.IntegerField(db_column='isWorkflowDoc')  # Field name made lowercase.
#     officaltype = models.IntegerField(db_column='officalType')  # Field name made lowercase.
#     version = models.IntegerField()
#     activeversionid = models.IntegerField(db_column='activeVersionID')  # Field name made lowercase.
#     versiondescription = models.CharField(db_column='versionDescription')  # Field name made lowercase.
#     versioncreater = models.IntegerField(db_column='VersionCreater')  # Field name made lowercase.
#     dsporder = models.IntegerField()
#     fieldnotimport = models.TextField(db_column='fieldNotImport')  # Field name made lowercase.
#     isfree = models.CharField(max_length=200)
#     ecology_pinyin_search = models.CharField(max_length=200)
#     custompage4emoble = models.CharField(db_column='custompage4Emoble')  # Field name made lowercase.
#     isupdatetitle = models.IntegerField()
#     isshared = models.CharField(max_length=200)
#     isoverrb = models.CharField(max_length=200)
#     isoveriv = models.CharField(max_length=200)
#     sendtomessagetype = models.CharField(max_length=200)
#     tracefieldid = models.IntegerField(db_column='traceFieldId')  # Field name made lowercase.
#     tracesavesecid = models.IntegerField(db_column='traceSaveSecId')  # Field name made lowercase.
#     tracecategorytype = models.CharField(db_column='traceCategoryType')  # Field name made lowercase.
#     tracecategoryfieldid = models.IntegerField(db_column='traceCategoryFieldId')  # Field name made lowercase.
#     tracedocownertype = models.IntegerField(db_column='traceDocOwnerType')  # Field name made lowercase.
#     tracedocownerfieldid = models.IntegerField(db_column='traceDocOwnerFieldId')  # Field name made lowercase.
#     tracedocowner = models.IntegerField(db_column='traceDocOwner')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'workflow_base'
#
#
# class WorkflowNodebase(models.Model):
#     id = models.IntegerField()
#     nodename = models.CharField(max_length=200)
#     isstart = models.CharField(max_length=200)
#     isreject = models.CharField(max_length=200)
#     isreopen = models.CharField(max_length=200)
#     isend = models.CharField(max_length=200)
#     drawxpos = models.IntegerField()
#     drawypos = models.IntegerField()
#     totalgroups = models.IntegerField()
#     nodeattribute = models.CharField(max_length=200)
#     passnum = models.IntegerField()
#     isfreenode = models.CharField(db_column='IsFreeNode')  # Field name made lowercase.
#     floworder = models.IntegerField()
#     signtype = models.CharField(db_column='Signtype')  # Field name made lowercase.
#     operators_1 = models.CharField(max_length=200)
#     requestid = models.IntegerField()
#     startnodeid = models.IntegerField()
#     operators = models.TextField()
#     ecology_pinyin_search = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'workflow_nodebase'
#
#
# class WorkflowRequestbase(models.Model):
#     requestid = models.IntegerField()
#     workflowid = models.IntegerField()
#     lastnodeid = models.IntegerField()
#     lastnodetype = models.CharField(max_length=200)
#     currentnodeid = models.IntegerField()
#     currentnodetype = models.CharField(max_length=200)
#     status = models.CharField(max_length=200)
#     passedgroups = models.IntegerField()
#     totalgroups = models.IntegerField()
#     requestname = models.CharField(max_length=200)
#     creater = models.IntegerField()
#     createdate = models.CharField(max_length=200)
#     createtime = models.CharField(max_length=200)
#     lastoperator = models.IntegerField()
#     lastoperatedate = models.CharField(max_length=200)
#     lastoperatetime = models.CharField(max_length=200)
#     deleted = models.SmallIntegerField()
#     creatertype = models.IntegerField()
#     lastoperatortype = models.IntegerField()
#     nodepasstime = models.FloatField()
#     nodelefttime = models.FloatField()
#     docids = models.TextField()
#     crmids = models.TextField()
#     hrmids = models.TextField()
#     prjids = models.TextField()
#     cptids = models.TextField()
#     requestlevel = models.IntegerField()
#     requestmark = models.CharField(max_length=200)
#     messagetype = models.IntegerField(db_column='messageType')  # Field name made lowercase.
#     mainrequestid = models.IntegerField(db_column='mainRequestId')  # Field name made lowercase.
#     currentstatus = models.IntegerField()
#     laststatus = models.CharField(max_length=200)
#     ismultiprint = models.IntegerField()
#     chatstype = models.IntegerField(db_column='chatsType')  # Field name made lowercase.
#     ecology_pinyin_search = models.CharField(max_length=200)
#     requestnamenew = models.CharField(max_length=200)
#     formsignaturemd5 = models.CharField(max_length=200)
#     dataaggregated = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'workflow_requestbase'
