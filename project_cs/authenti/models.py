# from django.contrib.auth.models import User
# from django.db import models

# class AlumniDetails(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     graduation_year = models.IntegerField()
#     current_company = models.CharField(max_length=100)
#     current_position = models.CharField(max_length=100)
#     linkedIn_profile = models.URLField()
#     def __str__(self):
#         return f"{self.user.username}'s Profile"
    
    
# class StudentUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     admission_no = models.CharField(max_length=20)
#     enrollment_year = models.IntegerField()
#     current_year = models.IntegerField()
#     expected_graduation_year = models.IntegerField()
from django.contrib.auth.models import User
from django.db import models

class AlumniDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()
    current_company = models.CharField(max_length=100)
    current_position = models.CharField(max_length=100)
    linkedIn_profile = models.URLField()

    def __str__(self):
        return f"{self.user.username}'s Profile"

class StudentUser(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=20)
    enrollment_year = models.IntegerField()
    current_year = models.IntegerField()
    expected_graduation_year = models.IntegerField()
    role_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s Student Profile"
