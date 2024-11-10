from django.db import models

from django.db import models

class CompanyDetails(models.Model):
    company_id = models.AutoField(primary_key=True)  # Primary Key for the company
    company_name = models.CharField(max_length=255, unique=True)  # Unique company name
    headquarters = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)  # Add Country field here
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
    company = models.IntegerField(null=True, blank=True) # models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name='company_reviews')  # Foreign Key to CompanyDetails
    user = models.IntegerField(null=True, blank=True) # models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign Key to User
    review_title = models.CharField(max_length=255)  # Title of the review
    review_content = models.TextField()  # Content of the review
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Rating (e.g., 4.5)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on modification

    def __str__(self):
        return f"{self.review_title} - {self.company.company_name}"