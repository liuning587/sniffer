# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class IndexA(models.Model):
    url = models.CharField(max_length=555, blank=True, null=True)
    url_name = models.CharField(max_length=300, blank=True, null=True)
    is_blank = models.CharField(max_length=200, blank=True, null=True)
    group_name = models.CharField(max_length=500, blank=True, null=True)
    btn = models.CharField(max_length=500, blank=True, null=True)
    other = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_a'
