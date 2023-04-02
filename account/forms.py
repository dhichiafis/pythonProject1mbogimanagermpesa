from django.contrib.auth.models import User
from django import forms
class SignupForm(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('password incorrect')

        return cd['password2']

