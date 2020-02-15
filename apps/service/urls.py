from django.conf.urls import url
from apps.service import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'upload$', views.upload),
    url(r'^celery$', views.celeryTest)
]
