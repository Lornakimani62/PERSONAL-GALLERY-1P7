from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^image/(\d+)', views.image, name='display'),
    url(r'^search/$', views.search, name='search'),
      url(r'^location/(\d+)', views.location_filter, name='location_filter'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)