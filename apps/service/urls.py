from django.conf.urls import url
from apps.service import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^myexp$',views.myExp),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d+)/$',views.herolist),
    url(r'^area/$',views.area),
    url(r'^area/(\d+)/$',views.area2),

]