from django.urls import path
from .views import stories

app_name = 'experiences'

urlpatterns = [
    path("",stories,name="stories")
]