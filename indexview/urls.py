from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.indexView, name='indexview_uid'),
    # url(r'^runme', views.runme, name="script"),
]