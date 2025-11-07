from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import Portfolio, ContactMessage, Introduction
from .forms import ContactForm


def home_page(request):
    portfolios = Portfolio.objects.filter(is_active=True)
    introduction = Introduction.objects.filter(is_active=True).first()
    
    # تنظیمات SEO از مدل Introduction
    seo_title = "مهدی محبی - برنامه‌نویس حرفه‌ای وب و متخصص تبلیغات دیجیتال"
    seo_description = "برنامه‌نویس حرفه‌ای وب و متخصص تبلیغات دیجیتال با بیش از ۵ سال تجربه در حوزه برنامه‌نویسی و تبلیغات. متخصص Django، Python، طراحی وب و ربات تلگرامی"
    seo_keywords = "مهدی محبی, برنامه‌نویس وب, Django, Python, طراحی وبسایت, ربات تلگرامی, تبلیغات دیجیتال, توسعه وب"
    
    if introduction:
        seo_title = introduction.seo_title or introduction.title or seo_title
        seo_description = introduction.seo_description or seo_description
        seo_keywords = introduction.seo_keywords or seo_keywords
    
    context = {
        'works': portfolios,
        'introduction': introduction,
        'form': ContactForm(),
        'seo_title': seo_title,
        'seo_description': seo_description,
        'seo_keywords': seo_keywords,
    }
    
    return render(request, 'page.html', context)


@require_http_methods(["POST"])
@csrf_protect
def new_message(request):
    
    form = ContactForm(request.POST)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهم گرفت.')
    else:
        messages.error(request, 'خطا در ارسال پیام. لطفا دوباره تلاش کنید.')
    
    return redirect('/')

