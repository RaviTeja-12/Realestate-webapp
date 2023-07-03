from django import forms
from .models import Users


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Users
        fields = '__all__'

class LoginForm(forms.Form):
    Email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)