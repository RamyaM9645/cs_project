# corporate_dict/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.corporate_dict_page, name='corporate_dict_page'),  # Main dictionary page
]