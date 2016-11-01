from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info/([0-9]{4})/$', views.page, name='page'),
]
