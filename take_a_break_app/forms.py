from django import forms

class Userinfo(forms.Form):
    username = forms.CharField(label = "username")
    email = forms.CharField(label="email")
    password = forms.CharField(label = "password")
    confirmed_password = forms.CharField(label = "confirmed_password")