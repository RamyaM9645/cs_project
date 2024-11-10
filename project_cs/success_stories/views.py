from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import SuccessStory
from .forms import SuccessStoryForm  # Form to create or edit stories (defined below)

# View to list all success stories
# def success_story_list(request):
#     stories = SuccessStory.objects.filter(visibility=True).order_by('-created_at')
#     return render(request, 'success_stories/success_story_list.html', {'stories': stories})

# def success_story_list(request):
#     # Assume `user_year` is a field on the user model or obtained through user profile
#     is_first_year = request.user.role_type == 'First Year' if request.user.is_authenticated else False
#     stories = SuccessStory.objects.all()
#     return render(request, 'success_stories/success_story_list.html', {'stories': stories, 'is_first_year': is_first_year})

def success_story_list(request):
    # Check if the user has a related StudentUser record and if they are a first-year student
    is_first_year = (
        hasattr(request.user, 'studentuser') and 
        request.user.studentuser.current_year == 1
    ) if request.user.is_authenticated else False
    
    stories = SuccessStory.objects.all()
    return render(request, 'success_stories/success_story_list.html', {'stories': stories, 'is_first_year': is_first_year})



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
