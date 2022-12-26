"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('whitelabel/', TemplateView.as_view(template_name='whitelabel.html'), name='whitelabel'),
    path('forex/', TemplateView.as_view(template_name='forex_crm.html'), name='forex'),
    path('crm/', TemplateView.as_view(template_name='crm.html'), name='crm'),
    path('office/', TemplateView.as_view(template_name='office.html'), name='office'),
    path('wbft/', TemplateView.as_view(template_name='wbft.html'), name='wbft'),
    path('test_one/', TemplateView.as_view(template_name='test_one.html'), name='test_one'),
    path('test_two/', TemplateView.as_view(template_name='test_two.html'), name='test_two'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('news/', TemplateView.as_view(template_name='news.html'), name='news'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('legal/', TemplateView.as_view(template_name='legal_services.html'), name='legal'),
    path('liquidity/', TemplateView.as_view(template_name='liquidity.html'), name='liquidity'),
]
