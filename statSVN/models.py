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
# class SvnChpwd(models.Model):
#     autoid = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=40, blank=True, null=True)
#     hexkey = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'svn_chpwd'
#
#
# class SvnauthDirAdmin(models.Model):
#     user_id = models.IntegerField()
#     repository = models.CharField(max_length=50)
#     path = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_dir_admin'
#         unique_together = (('user_id', 'repository', 'path'),)
#
#
# class SvnauthGPermission(models.Model):
#     group_id = models.CharField(max_length=11)
#     repository = models.CharField(max_length=50)
#     path = models.CharField(max_length=255)
#     permission = models.CharField(max_length=1)
#     expire = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_g_permission'
#         unique_together = (('group_id', 'repository', 'path'),)
#
#
# class SvnauthGroup(models.Model):
#     group_id = models.AutoField(primary_key=True)
#     group_name = models.CharField(unique=True, max_length=40)
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_group'
#
#
# class SvnauthGroupuser(models.Model):
#     group_id = models.AutoField()
#     user_id = models.IntegerField()
#     isowner = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_groupuser'
#         unique_together = (('group_id', 'user_id'),)
#
#
# class SvnauthPara(models.Model):
#     para_id = models.AutoField(primary_key=True)
#     para = models.CharField(unique=True, max_length=250)
#     value = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_para'
#
#
# class SvnauthPermission(models.Model):
#     user_id = models.CharField(max_length=11)
#     repository = models.CharField(max_length=50)
#     path = models.CharField(max_length=255)
#     permission = models.CharField(max_length=1)
#     expire = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'svnauth_permission'
#         unique_together = (('user_id', 'repository', 'path', 'permission'),)
#

class SvnauthUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=40)
    full_name = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=128)
    staff_no = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    supervisor = models.TextField()  # This field type is a guess.
    fresh = models.TextField(blank=True, null=True)  # This field type is a guess.
    expire = models.DateField()
    infotimes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'svnauth_user'

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
