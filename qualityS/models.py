# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class QualityService(models.Model):
    id = models.BigAutoField(primary_key=True)
    info = models.CharField(max_length=100)
    ques_from = models.CharField(max_length=100)
    ques_system = models.CharField(max_length=100)
    ques_dsc = models.TextField()
    ques_to = models.CharField(max_length=100, blank=True, null=True)
    ques_result = models.TextField()
    ques_status = models.CharField(max_length=64, blank=True, null=True)
    is_bug = models.CharField(max_length=64, blank=True, null=True)
    create_at = models.CharField(max_length=64)
    update_at = models.CharField(max_length=64)
    category = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'quality_service'

