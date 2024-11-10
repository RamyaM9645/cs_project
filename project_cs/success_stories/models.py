# stories/models.py

from django.db import models

class SuccessStory(models.Model):
    story_id = models.AutoField(primary_key=True)
    alumni_id = models.IntegerField(null=True, blank=True)  # Temporarily allow NULL values
    company_id = models.IntegerField(null=True, blank=True)  # Temporarily allow NULL values
    story_title = models.CharField(max_length=255)
    story_content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.story_title
