from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

        
#extension of auth form to include checkbox validation -Claudia
class MyUserCreationForm(UserCreationForm):
	remember_me = forms.BooleanField(widget=forms.CheckboxInput(),
                                     required=True,
                                     label='I agree to the Read My Paper terms of user.')