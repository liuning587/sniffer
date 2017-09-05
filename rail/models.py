
from django.db import models

class SnifferCases(models.Model):
    id = models.BigAutoField(primary_key=True)
    casename = models.CharField(max_length=100)
    create_by = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    url = models.CharField(max_length=164)
    data = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=64)
    expect = models.TextField(blank=True, null=True)
    emailto = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=164)
    create_at = models.CharField(max_length=100)
    is_warning = models.CharField(max_length=100)
    # def __str__(self):              # __unicode__ on Python 2
    #     return self.name

    class Meta:
        managed = False
        db_table = 'sniffer_cases'
