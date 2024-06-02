from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page),
    path('register', views.register),
    path('change', views.change),
]
