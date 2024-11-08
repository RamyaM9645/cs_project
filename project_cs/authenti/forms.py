from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AlumniDetails

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    graduation_year = forms.IntegerField()
    current_company = forms.CharField(max_length=100)
    current_position = forms.CharField(max_length=100)
    linkedIn_profile = forms.URLField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            AlumniDetails.objects.create(
                user=user,
                graduation_year=self.cleaned_data['graduation_year'],
                current_company=self.cleaned_data['current_company'],
                current_position=self.cleaned_data['current_position'],
                linkedIn_profile=self.cleaned_data['linkedIn_profile']
            )
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
