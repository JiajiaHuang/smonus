"""SMONU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, static
from django.contrib import admin
from django.urls import path, include

from SMONU import settings
from backstage.views import index, collections, collections_list, product, contact, error
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    url(r'^management-admin/', include('user.management.urls')),
    path('', index, name='index'),

]

news_patterns = ([
    path('', index, name='index'),
], 'news')

urlpatterns += i18n_patterns(
    url(_(r'^'), include('backstage.urls')),
    path(_(r'^i18n/'), include('django.conf.urls.i18n')),

)
