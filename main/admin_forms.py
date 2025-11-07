from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class AdminLoginForm(AuthenticationForm):
    """فرم لاگین ادمین با کپچا"""
    captcha = CaptchaField(
        label='عبارت امنیتی',
        error_messages={'invalid': 'عبارت امنیتی اشتباه است. لطفا دوباره تلاش کنید.'}
    )

