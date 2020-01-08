

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
import apps.service.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    url("b/", include('service.urls')),
    path('a/', include('service.urls')),
    url("^a$", views.index)
]




