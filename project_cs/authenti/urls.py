from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_view, name='login'),
    path('',views.landing_page),
    path('alumni/register/', views.alumni_register, name='alumni_register'),
    path('student/register/', views.student_register, name='student_register'),
    # path('login/', views.login_view, name='login'),/
    path('student/login/', views.student_login_view ),
    path('alumni/login/', views.alumni_login_view)

    
]
