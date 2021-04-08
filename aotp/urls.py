from django.urls import path
from .views import HomePageView 

from django.conf.urls import url
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    url(r'^external', views.external)
]