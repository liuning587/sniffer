from django.db import models

# Create your models here.


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
    create_at = models.CharField(max_length=100)
    run_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sniffer_result'



class SnifferResultLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    cases_id = models.BigIntegerField()
    casename = models.CharField(max_length=100)
    create_by = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    request = models.TextField()
    method = models.CharField(max_length=64)
    return_result = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=64, blank=True, null=True)
    create_at = models.CharField(max_length=100)
    run_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sniffer_result_log'



class SvnCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    full_name= models.CharField(max_length=100)
    month_count = models.BigIntegerField()
    weeks_count = models.BigIntegerField()
    date_count = models.BigIntegerField()
    info = models.CharField(max_length=64, blank=True, null=True)
    create_at = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'svn_count'
        unique_together = (('id', 'user_name'),)


class SvnCountLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    month_count = models.BigIntegerField()
    weeks_count = models.BigIntegerField()
    date_count = models.BigIntegerField()
    month = models.CharField(max_length=100)
    info = models.CharField(max_length=64, blank=True, null=True)
    create_at = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'svn_count_log'
