from django import forms


class LoginForm(forms.Form): 
    username = forms.CharField(max_length=150)
    password = forms.charField(max_length=150, widget=forms.PasswordInput)