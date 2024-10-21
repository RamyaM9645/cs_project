from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User,Student, Alumni


# Student Registration Form
class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    admission_no = forms.CharField(max_length=20)
    enrollment_year = forms.IntegerField()
    current_year = forms.IntegerField()
    expected_graduation_year = forms.IntegerField()

# Alumni Registration Form
class AlumniRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    graduation_year = forms.IntegerField()
    current_company = forms.CharField(max_length=255)
    current_position = forms.CharField(max_length=255)
    linkedIn_profile = forms.URLField(required=False)

# Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
