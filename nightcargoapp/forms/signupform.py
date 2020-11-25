from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class SignUpForm(UserCreationForm):
    tck_no = forms.CharField(max_length=11, help_text='T.C Kimlik Numaranızı Giriniz', validators=[MinLengthValidator(11)])
    first_name = forms.CharField(max_length=100, help_text='Adınızı Giriniz')
    last_name = forms.CharField(max_length=100, help_text='Soyadınızı Giriniz')
    email = forms.EmailField(max_length=150, help_text='Email Adresinizi Giriniz')

    class Meta:
        model = User
        fields = ('username', 'tck_no', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)
