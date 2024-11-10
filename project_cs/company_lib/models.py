from django.db import models
from django.conf import settings  # Import settings to use the custom User model

class CompanyDetails(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, unique=True)
    headquarters = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
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
    review_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name='reviews')   # Link to CompanyDetails
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the User model
    review_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.review_title} - {self.company.company_name}"