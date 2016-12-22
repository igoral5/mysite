from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts':posts})
