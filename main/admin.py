from django.contrib import admin
from django.utils.html import format_html
from .models import Portfolio, ContactMessage, Introduction


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'about']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at', 'image_preview']
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'about', 'image', 'image_preview', 'url')
        }),
        ('تنظیمات', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "بدون تصویر"
    image_preview.short_description = "پیش‌نمایش تصویر"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'title', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['fullname', 'email', 'title', 'message']
    list_editable = ['is_read']
    readonly_fields = ['fullname', 'email', 'phonenumber', 'title', 'message', 'created_at']
    
    fieldsets = (
        ('اطلاعات تماس', {
            'fields': ('fullname', 'email', 'phonenumber')
        }),
        ('پیام', {
            'fields': ('title', 'message')
        }),
        ('وضعیت', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        return False


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('محتوا', {
            'fields': ('title', 'content')
        }),
        ('تنظیمات', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


# تنظیمات پنل ادمین
admin.site.site_header = "پنل مدیریت سایت مهدی محبی"
admin.site.site_title = "پنل مدیریت"
admin.site.index_title = "خوش آمدید به پنل مدیریت"
