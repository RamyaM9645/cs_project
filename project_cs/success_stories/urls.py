from django.urls import path
from . import views

app_name = 'success_stories'

urlpatterns = [
    path('', views.success_story_list),  # List all success stories
    path('add/', views.add_success_story),  # Page to add a new story
    path('<int:story_id>/', views.success_story_detail),  # View individual story by ID
]