from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import SuccessStory
from .forms import SuccessStoryForm  # Form to create or edit stories (defined below)

# View to list all success stories
def success_story_list(request):
    stories = SuccessStory.objects.filter(visibility=True).order_by('-created_at')
    return render(request, 'success_stories/success_story_list.html', {'stories': stories})

# View to display details of a single story
def success_story_detail(request, pk):
    story = SuccessStory.objects.get(pk=pk)
    return render(request, 'success_stories/success_story_detail.html', {'story': story})

# View to create a new success story
def success_story_create(request):
    if request.method == 'POST':
        form = SuccessStoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_stories:success_story_list')
    else:
        form = SuccessStoryForm()
    return render(request, 'success_stories/success_story_form.html', {'form': form})
