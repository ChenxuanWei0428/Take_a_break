from django import forms

class User_info(forms.Form):
    username = forms.CharField(label = "username")
    email = forms.CharField(label="email")
    password = forms.CharField(label = "password")
    confirm_password = forms.CharField(label="confirm_password")

class User_login(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label = "password")