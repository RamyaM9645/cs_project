from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import AlumniDetails, StudentUser


def landing_page(request):
    return render(request, 'authenti/landing.html')

# Alumni Registration View
def alumni_register(request):
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
            messages.error(request, "Passwords do not match.")
            return render(request, 'authenti/register.html')

        try:
            # Create the user with hashed password
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password1)
            )
            # Create alumni details entry
            AlumniDetails.objects.create(
                user=user,
                graduation_year=int(graduation_year),
                current_company=current_company,
                current_position=current_position,
                linkedIn_profile=linkedIn_profile.strip()
            )
            return redirect('/alumni/login/')  # Redirect to alumni login

        except IntegrityError:
            messages.error(request, "A user with this username or email already exists.")
            return render(request, 'authenti/register.html')
        except ValueError:
            messages.error(request, "Please enter valid data.")
            return render(request, 'authenti/register.html')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'authenti/register.html')

    return render(request, 'authenti/register.html')

# Student Registration View
def student_register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        admission_no = request.POST.get('admission_no')
        enrollment_year = request.POST.get('enrollment_year')
        current_year = request.POST.get('current_year')
        expected_graduation_year = request.POST.get('expected_graduation_year')
        role_type = request.POST.get('student_year') 

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authenti/student_register.html')

        try:
            # Create the user with hashed password
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password1)
            )
            # Create student details entry
            StudentUser.objects.create(
                user=user,
                admission_no=admission_no,
                enrollment_year=int(enrollment_year),
                current_year=int(current_year),
                expected_graduation_year=int(expected_graduation_year),
                role_type=role_type
            )
            return redirect('/student/login/')  # Redirect to student login

        except IntegrityError:
            messages.error(request, "A user with this username or email already exists.")
            return render(request, 'authenti/student_register.html')
        except ValueError:
            messages.error(request, "Please enter valid data.")
            return render(request, 'authenti/student_register.html')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'authenti/student_register.html')

    return render(request, 'authenti/student_register.html')

# Student Login View

# def student_login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to student home page after login
#         else:
#             messages.error(request, "Invalid username or password.")
    
#     return render(request, 'authenti/student_login.html')

def student_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                student_user = StudentUser.objects.get(user=user)
                print(f"Session before setting role: {student_user.role_type}")  # Debug print
                request.session['role_type'] = student_user.role_type
                request.session.save()
                print(f"Session after setting role: {request.session.items()}") 
            except StudentUser.DoesNotExist:
                messages.error(request, "This account does not have a Student profile.")
                return redirect('student_login')
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'authenti/student_login.html')



# Alumni Login View
def alumni_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['role_type'] = "Alumni"
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to alumni home page after login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'authenti/alumni_login.html')
