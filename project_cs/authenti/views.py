from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import AlumniDetails
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        graduation_year = request.POST.get('graduation_year')
        current_company = request.POST.get('current_company')
        current_position = request.POST.get('current_position')
        linkedIn_profile = request.POST.get('linkedIn_profile')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'authenti/register.html')

        # Create the user and handle possible errors
        try:
            user = User.objects.create(
                username=username,
                email=email,
                # password=make_password(password1)  # Hash the password
                password=make_password(password1)  # Hash the password
            )
            print("User created:", user)

            # Create the alumni details entry
            AlumniDetails.objects.create(
                user=user,
                graduation_year=int(graduation_year),  # Ensure it's an integer
                current_company=current_company,
                current_position=current_position,
                linkedIn_profile=linkedIn_profile.strip()
            )
            print("Alumni details saved.")

            return redirect('login')  # Redirect to login page after registration
        
        except IntegrityError as e:
            print("IntegrityError:", e)
            print("Could not create user. A user with this username or email may already exist.")
            return render(request, 'authenti/register.html')
        except ValueError as e:
            print("ValueError:", e)
            print("Invalid data format.")
            return render(request, 'authenti/register.html')
        except Exception as e:
            print("An error occurred:", e)
            return render(request, 'authenti/register.html')

    return render(request, 'authenti/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            print("Invalid username or password.")
    
    return render(request, 'authenti/login.html')
