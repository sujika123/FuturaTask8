from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, studentlogin, notificationadd, StdntComplaint


class DateInput(forms.DateInput):
    input_type="date"

class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2= forms.CharField(widget=forms.PasswordInput, label='confirm password')
    class Meta:
        model=Login
        fields=('username','password1','password2',)

class studentloginform(forms.ModelForm):
    class Meta:
        model=studentlogin
        fields=('name','email','rollnum','collegename','phone')


class notificationform(forms.ModelForm):

    class Meta:
        model=notificationadd
        fields=('name','description')


class StdntComplaintForm(forms.ModelForm):

    class Meta:
        model = StdntComplaint
        fields = ('subject', 'complaint')