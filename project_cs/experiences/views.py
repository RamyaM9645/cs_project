from django.shortcuts import render

def stories(request):
    return render(request,'experiences/stories.html')