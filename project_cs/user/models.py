from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Custom User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Add related_name to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to any unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change this to any unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.email

# Student Model (Linked to User)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=20)
    enrollment_year = models.IntegerField()
    current_year = models.IntegerField()
    expected_graduation_year = models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - Student'

# Alumni Model (Linked to User)
class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()
    current_company = models.CharField(max_length=255)
    current_position = models.CharField(max_length=255)
    linkedIn_profile = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - Alumni'

class SuccessStory(models.Model):
    story_id = models.AutoField(primary_key=True)  # Primary Key for the story
    alumni = models.IntegerField(null=True, blank=True) # models.ForeignKey(Alumni, on_delete=models.CASCADE)  # Foreign Key to Alumni
    company = models.IntegerField(null=True, blank=True) # models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)  # Foreign Key to Company
    story_title = models.CharField(max_length=255)  # Title of the success story
    story_content = models.TextField()  # Content of the success story
    image_url = models.URLField(blank=True, null=True)  # Optional image URL
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update on modification

    def __str__(self):
        return self.story_title