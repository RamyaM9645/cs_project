from django.shortcuts import render, redirect, get_object_or_404
from .models import SuccessStory
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# View to list all success stories
@login_required
# def success_story_list(request):
#     # Check if the user has a related StudentUser record and if they are a first-year student
#     is_first_year = (
#         hasattr(request.user, 'studentuser') and 
#         request.user.studentuser.role_type == "First Year"
#     ) if request.user.is_authenticated else False
    
#     # Fetch all success stories
#     stories = SuccessStory.objects.all()
#     return render(request, 'success_stories/success_story_list.html', {'stories': stories, 'is_first_year': is_first_year})

# from django.shortcuts import render
# from .models import SuccessStory

def success_story_list(request):
    # Get the search query from the request
    search_query = request.GET.get('q', '')

    # Check if the user has a related StudentUser record and if they are a first-year student
    is_first_year = (
        hasattr(request.user, 'studentuser') and 
        request.user.studentuser.role_type == "First Year"
    ) if request.user.is_authenticated else False

    # Filter stories based on the search query if provided
    if search_query:
        stories = SuccessStory.objects.filter(story_title__icontains=search_query)
    else:
        stories = SuccessStory.objects.all()

    context = {
        'stories': stories,
        'is_first_year': is_first_year,
        'search_query': search_query,  # Pass the query to the template to keep it in the input field
    }
    return render(request, 'success_stories/success_story_list.html', context)


def success_story_detail(request, story_id):
    story = get_object_or_404(SuccessStory, pk=story_id)  # Use story_id here
    return render(request, 'success_stories/success_story_detail.html', {'story': story})

# View for logging out
def logout_view(request):
    """Logs the user out and redirects to the homepage or login page."""
    logout(request)  # Log out the user
    return redirect('home')  # Redirect to home page or any other page after logout

# View for adding a new success story
def add_success_story(request):
    if request.method == 'POST':
        # Collect data from the form
        story_title = request.POST.get('story_title')
        story_content = request.POST.get('story_content')
        image = request.FILES.get('image')
        username = request.user.username
        print(f"session role : {request.session['role_type']}")
        user_role = request.session['role_type']
         # Handle image upload
        
        # Create the new success story
        story = SuccessStory.objects.create(
            story_title=story_title,
            story_content=story_content,
            image=image,
            username=username,
            user_role=user_role
        )
        story.save()
        # Redirect after saving the new story
        return redirect('/home/success_stories/')  # Ensure this matches your URL path
    
    return render(request, 'success_stories/success_story_form.html')  # Show the form if not a POST request
