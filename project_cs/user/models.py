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

class CompanyDetails(models.Model):
    company_id = models.AutoField(primary_key=True)  # Primary Key for the company
    company_name = models.CharField(max_length=255, unique=True)  # Unique company name
    headquarters = models.CharField(max_length=255, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    core_products_services = models.TextField(blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)
    recruitment_process = models.TextField(blank=True, null=True)
    common_roles = models.TextField(blank=True, null=True)
    global_presence = models.BooleanField(default=False)
    college_visited = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='company_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    
class CompanyReview(models.Model):
    review_id = models.AutoField(primary_key=True)  # Primary Key for each review
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name='company_reviews')  # Foreign Key to CompanyDetails
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign Key to User
    review_title = models.CharField(max_length=255)  # Title of the review
    profile_picture = models.ImageField(upload_to='review_profiles/', blank=True, null=True)  # Optional profile picture
    review_content = models.TextField()  # Content of the review
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Rating (e.g., 4.5)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on modification

    def __str__(self):
        return f"{self.review_title} - {self.company.company_name}"