from django.urls import path
from . import views

app_name = 'success_stories'

urlpatterns = [
    path('', views.success_story_list, name='success_story_list'),
    path('<int:pk>/', views.success_story_detail, name='success_story_detail'),
    path('create/', views.success_story_create, name='success_story_create'),
]
