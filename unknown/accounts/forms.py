from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    location = forms.CharField(required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'location' )

