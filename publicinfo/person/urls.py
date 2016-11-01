from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/(?P<city>[\w-]+)/(?P<state>[\w-]+)/(?P<slug>[\w-]+)/$', views.PageDetailView.as_view(), name='person_detail_page'),
]
