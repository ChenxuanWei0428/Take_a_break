from django import forms

class User_info(forms.Form):
    username = forms.CharField(label = "username")
    email = forms.CharField(label="email")
    password = forms.CharField(label = "password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label = "Please enter again your password", widget=forms.PasswordInput)