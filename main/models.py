from django.db import models
from django.utils import timezone


class Portfolio(models.Model):
    """مدل نمونه کارها"""
    title = models.CharField(max_length=200, verbose_name="عنوان")
    about = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='portfolio/', verbose_name="تصویر")
    url = models.URLField(max_length=500, blank=True, null=True, verbose_name="لینک مشاهده (اختیاری)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کارها"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """مدل پیام‌های ارسالی از فرم تماس"""
    fullname = models.CharField(max_length=200, verbose_name="نام کامل")
    email = models.EmailField(verbose_name="ایمیل")
    phonenumber = models.CharField(max_length=20, verbose_name="شماره تلفن")
    title = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.fullname} - {self.title}"


class Introduction(models.Model):
    """مدل متن معرفی"""
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    seo_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="عنوان SEO", help_text="اگر خالی باشد از عنوان استفاده می‌شود")
    seo_description = models.TextField(blank=True, null=True, verbose_name="توضیحات SEO", help_text="توضیحات برای موتورهای جستجو")
    seo_keywords = models.CharField(max_length=500, blank=True, null=True, verbose_name="کلمات کلیدی SEO", help_text="کلمات کلیدی با کاما جدا شوند")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "متن معرفی"
        verbose_name_plural = "متن‌های معرفی"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
