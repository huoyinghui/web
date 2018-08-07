from django import forms


class LoginForm(forms.Form):
    """
    login form
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
