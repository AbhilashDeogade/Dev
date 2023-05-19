from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from captcha.fields import CaptchaField


# class SignupForm(UserCreationForm):
#     image = forms.ImageField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'image']


class SignupForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    #mobile = forms.IntegerField()
    #is_loan_representativ = forms.BooleanField()
    class Meta:
        model = User
        fields = ['username', 'email']



class PasswordReset(PasswordResetForm):
    class Meta:
        model = User
        fields = '__all__'

class UserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class EditAdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= '__all__'
        labels = {'email': 'Email'}

    
class CaptchaForm(forms.Form):
    captcha = CaptchaField()