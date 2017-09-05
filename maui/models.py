# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MauiResult(models.Model):
    url_id = models.IntegerField()
    case_id = models.IntegerField()
    id = models.BigAutoField(unique=True, primary_key=True)
    url_desc = models.CharField(max_length=600, blank=True, null=True)
    case_desc = models.CharField(max_length=500, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    return_req = models.TextField(blank=True,
                                  null=True)
    request = models.TextField(blank=True,
                               null=True)  # Field renamed because it was a Python reserved word.
    run_time = models.DateTimeField(blank=True, null=True)
    system = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maui_result'


class MauiUrl(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    url_desc = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=600, blank=True, null=True)
    system = models.CharField(max_length=100, blank=True, null=True)
    environ = models.CharField(max_length=100, blank=True, null=True)
    create_by = models.CharField(max_length=100, blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    login_name = models.CharField(max_length=100, blank=True, null=True)
    login_pwd = models.CharField(max_length=100, blank=True, null=True)
    is_warning = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maui_url'


class MauiUrlCase(models.Model):
    # blog = models.ForeignKey(MauiUrl)
    url_id = models.IntegerField()
    id = models.BigAutoField(unique=True, primary_key=True)
    case_desc = models.CharField(max_length=100, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    expect = models.CharField(max_length=100, blank=True, null=True)
    create_by = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maui_url_case'
