# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
    titleField = forms.CharField(max_length = 100, label="title")
    dueDateField = forms.IntegerField()
    classNumField = forms.IntegerField()
    promptField = forms.CharField(max_length = 300)