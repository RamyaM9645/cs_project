from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kyc_chat',include(('kyc_chat.urls','kyc_chat'),namespace='home'))
]