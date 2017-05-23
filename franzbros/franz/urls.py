from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_mame = "franz"

urlpatterns = [
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^services', views.services, name='services'),
    url(r'', views.home, name='home'),
]
