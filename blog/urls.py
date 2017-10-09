from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='article_page'),
    url(r'^article/edit/(?P<article_id>\d+)$', views.edit, name='edit_page'),
    url(r'^article/action$', views.action, name='edit_action'),
]