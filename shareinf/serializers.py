# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from shareinf.models import Good
from django.contrib.auth.models import User

class goodSerializer(serializers.ModelSerializer):
  #SubmitterID = serializers.IntegerField(source='User.id')
  #SubmitterName = serializers.CharField(source='User.last_name')

  class Meta:
    model = Good
    #fields = ('id', 'IssueTitle', 'IssueDesc', 'SubmitterID', 'SubmitterName', 'Vote', 'View', 'Answer', 'Tags', 'CreateTime', 'LastModifyTime')
    fields = ('id', 'goodName', 'goodType', 'goodDesc', 'goodAmount', 'goodStatus', 'goodRemark', 'goodOwner', 'goodWanter', 'Tags', 'CreateTime', 'LastModifyTime')
