from django.contrib import admin
from .models import User,Student,Alumni,SuccessStory,CompanyDetails,CompanyReview

admin.site.register(User)
admin.site.register(Alumni)
admin.site.register(Student)
admin.site.register(SuccessStory)
admin.site.register(CompanyDetails)
admin.site.register(CompanyReview)


