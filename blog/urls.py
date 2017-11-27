from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    url(r'^edit/action$',views.edit_action,name='edit_action'),
    url(r'^update/(?P<article_id>[0-9]+)$',views.update,name='update_page'),
    url(r'^update/action/(?P<article_id>[0-9]+)$',views.update_action,name='update_action'),
]

