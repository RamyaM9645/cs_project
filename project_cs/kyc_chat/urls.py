from django.urls import path

from .views import index 

urlpatterns = [
    path("", index,name="kyc_chat"),
]