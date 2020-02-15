

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
import apps.service.views as views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url("api/", include('apps.service.urls')),
    path('a/', include('apps.service.urls')),
    re_path("^ad$", views.index)
]




