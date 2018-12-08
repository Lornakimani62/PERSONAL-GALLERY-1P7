from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^image/$', views.image, name='image'),
    url(r'^search/$', views.search, name='search')
]