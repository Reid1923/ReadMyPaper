from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf
from django import forms
from ReadMyPaper.feedbackEmail.forms import EmailForm
from django.core.mail import EmailMessage

# Create your views here.
def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        return render(request ,'email.html', {'email_form': form})
    
    form = EmailForm(request.POST, request.FILES)   
    if form.is_valid():
        subject = "Your feedback from Read My Paper is ready"
        
        message = "Hello there, \n Your feedback from Read My Paper is ready and downloadable in the attachment. Please do not forget to be courteous and make edits for others! \n -The Read My Paper team"
        
        email = form.cleaned_data['email']
        attach = request.FILES['attach']
        ext = ['.doc' , '.docx' , '.txt' , '.pdf' , '.rtf']
        if attach.name.endswith(tuple(ext)):
            mail = EmailMessage(subject, message, 'noreplyreadmypaper@gmail.com', [email])
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            
            return render(request ,'email.html', {'message': 'Sent email to %s'%email})   
        
        return render(request , 'email.html' , {'message': 'Please attach a file that ends with one of the following: .doc , .docx , .txt , .pdf , .rtf'})
 #           return render(request ,'email.html' , {'message': 'Did not send email to %s'%email})