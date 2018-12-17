# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from shareinf.models import Good
from rest_framework import viewsets
from shareinf.serializers import goodSerializer

# Create your views here.
class goodViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Good.objects.all().order_by('-CreateTime')
  serializer_class = goodSerializer
