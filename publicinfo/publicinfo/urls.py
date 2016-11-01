"""publicinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from person.models import Page
from person.views import PageListView

info_dict = {
    'queryset': Page.objects.all(),
    'slug': 'slug',
    'state': 'state',
    'city': 'city'
}

urlpatterns = [
    #url(r'^', PageListView.as_view(), name='person_list_page'),
    url(r'^person/', include('person.urls')),
    url(r'^dj_admin-2081238/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'page': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
