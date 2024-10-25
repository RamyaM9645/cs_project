from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('kyc_chat',include(('kyc_chat.urls','kyc_chat'),namespace='home1')),
    path('news',include(('news.urls','news'),namespace='home2')),
    path('stories',include('experiences.urls',namespace='home3'))
]