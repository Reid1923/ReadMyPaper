# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import DocumentList

urlpatterns = patterns('ReadMyPaper.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^document_list/$', DocumentList.as_view()),
)
