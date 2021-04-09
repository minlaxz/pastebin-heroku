from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='indexview_uid'),
]