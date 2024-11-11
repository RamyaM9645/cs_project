from django.db import models
from django.utils import timezone
# CompanyDetails

class SuccessStory(models.Model):
    story_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,null=True, blank=True)
    user_role = models.CharField(max_length=255,null=True, blank=True)
    story_title = models.CharField(max_length=255)
    story_content = models.TextField()
    image = models.ImageField(upload_to='stories/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.story_title