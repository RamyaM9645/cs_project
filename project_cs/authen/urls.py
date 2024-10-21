from django.urls import path
from . import views

urlpatterns = [
    path('stud_register/', views.stud_register, name='stud_register'),
    path('alum_register/', views.alum_register, name='alum_register'),
    path('stud_login/', views.stud_login, name='stud_login'),
    path('alum_login/', views.alum_login, name='alum_login'),
]