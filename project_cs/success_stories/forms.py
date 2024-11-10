from django import forms
from .models import SuccessStory

class SuccessStoryForm(forms.ModelForm):
    class Meta:
        model = SuccessStory
        fields = ['story_title', 'story_content', 'image_url', 'visibility']
