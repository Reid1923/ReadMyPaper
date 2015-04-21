# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models
from django import forms
from ReadMyPaper.myapp.models import Document
from ReadMyPaper.myapp.forms import DocumentForm

#imports for viewing list of papers
from django.views.generic import ListView
from models import Document
from .forms import DocumentForm

#class for list view of documents
newdoc = Document
class DocumentList(ListView):
	model = Document

#functions for uploading papers

#----------------------------------
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
        	newDoc = form.save()
    else:
    	form = DocumentForm()
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )