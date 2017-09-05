# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class SnifferWarning(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, unique=True)
    wxopenid = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    system = models.CharField(max_length=255)


    class Meta:
        managed = False
        db_table = 'sniffer_warning'


class SnifferResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    cases_id = models.BigIntegerField()
    casename = models.CharField(max_length=100)
    create_by = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    request = models.TextField()
    method = models.CharField(max_length=64)
    return_result = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=64, blank=True, null=True)
    create_at = models.BigIntegerField()
    run_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sniffer_result'
