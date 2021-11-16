from django.shortcuts import render
from .models import Post

def blog(request):
    """
    Display blog page
    """
    posts = Post.objects.all()
    template = 'blog/blog.html'

    context = {
        'posts': posts
    }

    return render(request, template, context)
