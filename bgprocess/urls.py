from django.conf.urls import include, url
from django.contrib import admin

from web import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view()),
    url(r'^django-rq/', include('django_rq.urls')),
]
