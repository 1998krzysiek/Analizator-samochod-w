from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('contact/', views.contact, name='contact'),
    url('ekspert/', views.ekspert, name='ekspert'),
]
