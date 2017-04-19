import re
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Registration


class RegistrationForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20,
                                       widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    class Meta:
        model = Registration
        exclude = ['user']

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']
        if password != confirm_password:
            raise forms.ValidationError("Password doesn't match")
        return password

    def clean_email_id(self):
        email_id = self.cleaned_data.get('email_id')
        match = re.search(r'[\w.-]+@[\w.-]+.\w+', email_id)
        if not match:
            raise forms.ValidationError("Enter Correct Email Address")
        email = User.objects.filter(username=email_id)
        if email_id and email.count() > 0:
            raise forms.ValidationError("Email Already Exist")
        return email_id
