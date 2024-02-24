from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    email = forms.EmailField(help_text='Required', required=True, widget=forms.EmailInput(attrs={'class': 'form-control shadow'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control shadow'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control shadow'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control shadow'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control shadow'} ))   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control shadow'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-center shadow'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-center shadow'}))
    
    


