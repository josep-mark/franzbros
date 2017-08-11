"""franzbros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from franz import views as franz_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico$',
        RedirectView.as_view(url=staticfiles_storage.url('search/favicon.ico'),
                             permanent=False), name="favicon"),
    url(r'^about$', franz_views.about, name='about'),
    url(r'^services', franz_views.services, name='services'),
    url(r'^contact$', franz_views.contact, name='contact'),
    url(r'', franz_views.home, name='home')
]
