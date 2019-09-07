from django.conf.urls import url
import myproject.views as views

urlpatterns = [
    url("^a$",views.index)
]