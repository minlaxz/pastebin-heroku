from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.aboutView, name='aboutview_uid'),
    # url(r'^runme', views.runme, name="script"),
]