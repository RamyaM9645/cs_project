from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import StudentRegisterForm, AlumniRegisterForm, UserLoginForm
from .models import Student, Alumni

# Student Registration View
def stud_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create Student record linked to the User
            Student.objects.create(
                user=user,
                admission_no=form.cleaned_data['admission_no'],
                enrollment_year=form.cleaned_data['enrollment_year'],
                current_year=form.cleaned_data['current_year'],
                expected_graduation_year=form.cleaned_data['expected_graduation_year'],
            )
            messages.success(request, f'Account created for {user.username}!')
            return redirect('stud_login')
    else:
        form = StudentRegisterForm()
    return render(request, 'users/stud_register.html', {'form': form})

# Alumni Registration View
def alum_register(request):
    if request.method == 'POST':
        form = AlumniRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create Alumni record linked to the User
            Alumni.objects.create(
                user=user,
                graduation_year=form.cleaned_data['graduation_year'],
                current_company=form.cleaned_data['current_company'],
                current_position=form.cleaned_data['current_position'],
                linkedIn_profile=form.cleaned_data['linkedIn_profile']
            )
            messages.success(request, f'Account created for {user.username}!')
            return redirect('alum_login')
    else:
        form = AlumniRegisterForm()
    return render(request, 'users/alum_register.html', {'form': form})

# Student Login View
def stud_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'student'):
                login(request, user)
                return redirect('student_dashboard')  # Replace with your student dashboard
            else:
                messages.error(request, 'Invalid credentials or you are not registered as a student.')
    else:
        form = UserLoginForm()
    return render(request, 'users/stud_login.html', {'form': form})

# Alumni Login View
def alum_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'alumni'):
                login(request, user)
                return redirect('alumni_dashboard')  # Replace with your alumni dashboard
            else:
                messages.error(request, 'Invalid credentials or you are not registered as alumni.')
    else:
        form = UserLoginForm()
    return render(request, 'users/alum_login.html', {'form': form})
