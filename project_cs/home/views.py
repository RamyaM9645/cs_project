from django.shortcuts import render
from django.http import request
from authenti import views
def index(request):
    return render(request,'home/index.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    """Logs the user out and redirects to the homepage or login page."""
    logout(request)  # Log out the user
    return redirect('landing_page')  # Redirect to home page or any other page after logout
