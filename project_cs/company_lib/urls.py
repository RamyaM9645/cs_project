# company_lib/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
]