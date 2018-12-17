# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Good(models.Model):
  goodName = models.CharField('goodName', max_length=32)
  goodType = models.CharField('goodType', max_length=32)
  goodDesc = models.CharField('goodDesc', max_length=128) # Improve to rich text object
  goodAmount = models.IntegerField('goodAmount', blank=False, default=1)
  goodStatus = models.IntegerField('goodStatus', blank=False, default=1) # 1: sharing, 2: shared
  goodRemark = models.CharField('goodRemark', max_length=128)
  goodOwner = models.ManyToManyField(User, related_name="owner")
  goodWanter = models.ManyToManyField(User, related_name="wanter")
  Tags = models.CharField('Tags', max_length=128)
  CreateTime = models.DateTimeField('CreateTime', null=False, auto_now_add=True)
  LastModifyTime = models.DateTimeField('LastModifyTime', null=True, auto_now=True)

  class Meta:
    db_table = 'h_good'
    ordering = ['-id']
