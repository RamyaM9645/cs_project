from django.contrib import admin
from .models import User,Student,Alumni,CompanyDetails,CompanyReview

admin.site.register(User)
admin.site.register(Alumni)
admin.site.register(Student)
admin.site.register(CompanyDetails)
admin.site.register(CompanyReview)


