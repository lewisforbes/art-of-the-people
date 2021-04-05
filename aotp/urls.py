from django.urls import path
from .views import HomePageView, AboutPageView

from django.conf.urls import url
from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    url(r'^external', views.external)
]