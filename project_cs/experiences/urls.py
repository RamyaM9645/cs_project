from django.urls import path

from .views import stories

urlpatterns = [
    path("",stories,name="stories")
]