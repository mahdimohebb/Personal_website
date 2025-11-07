from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('newmsg/', views.new_message, name='newmsg'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
]

