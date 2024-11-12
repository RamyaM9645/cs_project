from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('authenti/', include('authenti.urls')),  # Include authen URLs
    path('kyc_chat',include(('kyc_chat.urls','kyc_chat'),namespace='home1')),
    path('news',include(('news.urls','news'),namespace='home2')),
    path('success_stories/', include('success_stories.urls')), 
    path('company_lib/', include('company_lib.urls')), 
]