from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AlumniDetails,StudentUser

admin.site.register(AlumniDetails)
admin.site.register(StudentUser)
