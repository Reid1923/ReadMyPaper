# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    titleField = models.CharField(max_length=100, default="")

    dueDateField = models.IntegerField(default=10)
    
    classNumField = models.IntegerField(default=0)
    promptField = models.CharField(max_length=300, default="")