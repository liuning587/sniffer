# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class SnifferCases(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     casename = models.CharField(max_length=100)
#     create_by = models.CharField(max_length=100)
#     system = models.CharField(max_length=100)
#     url = models.CharField(max_length=164)
#     data = models.TextField(blank=True, null=True)
#     method = models.CharField(max_length=64)
#     expect = models.TextField(blank=True, null=True)
#     emailto = models.CharField(max_length=64, blank=True, null=True)
#     create_at = models.BigIntegerField()
#     state = models.CharField(max_length=164, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sniffer_cases'
#
#
# class SnifferResult(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cases_id = models.BigIntegerField()
#     casename = models.CharField(max_length=100)
#     create_by = models.CharField(max_length=100)
#     system = models.CharField(max_length=100)
#     request = models.TextField()
#     method = models.CharField(max_length=64)
#     return_result = models.TextField(blank=True, null=True)
#     result = models.CharField(max_length=64, blank=True, null=True)
#     create_at = models.BigIntegerField()
#     run_count = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sniffer_result'
#
#
# class SvnCount(models.Model):
#     id = models.BigAutoField()
#     user_name = models.CharField(max_length=100)
#     month_count = models.CharField(max_length=100)
#     weeks_count = models.CharField(max_length=100)
#     date_count = models.CharField(max_length=164)
#     info = models.CharField(max_length=64, blank=True, null=True)
#     create_at = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'svn_count'
#         unique_together = (('id', 'user_name'),)
#
#
# class SvnCountLog(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user_name = models.CharField(max_length=100)
#     month_count = models.CharField(max_length=100)
#     weeks_count = models.CharField(max_length=100, blank=True, null=True)
#     date_count = models.CharField(max_length=164, blank=True, null=True)
#     month = models.CharField(max_length=100)
#     info = models.CharField(max_length=64, blank=True, null=True)
#     create_at = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'svn_count_log'
