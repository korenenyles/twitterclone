from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import TwitterUser

class SignUpForm(UserCreationForm):

    class Meta:
        model = TwitterUser
        fields = ('username', 'password1', 'password2')
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)