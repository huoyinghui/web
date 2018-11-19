from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    login form
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    """
    register form
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ActiveForm(forms.Form):
    """
    active
    """
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetForm(forms.Form):
    """
    forget
    """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    """
    forget
    """
    old_password = forms.CharField(required=True, min_length=6)
    new_password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
