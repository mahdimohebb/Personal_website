from django import forms
from captcha.fields import CaptchaField
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """فرم تماس با کپچا"""
    captcha = CaptchaField(
        label='عبارت امنیتی',
        error_messages={'invalid': 'عبارت امنیتی اشتباه است. لطفا دوباره تلاش کنید.'}
    )

    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'phonenumber', 'title', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }
        labels = {
            'fullname': 'نام کامل',
            'email': 'ایمیل',
            'phonenumber': 'شماره تلفن',
            'title': 'موضوع',
            'message': 'پیام',
        }

