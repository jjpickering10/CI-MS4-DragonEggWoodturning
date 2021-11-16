from django.shortcuts import render
from .models import Post

def blog(request):
    """
    Display blog page
    """
    posts = Post.objects.all()
    for post in posts:
        print(post.comment_set.all())
    template = 'blog/blog.html'

    context = {
        'posts': posts
    }

    return render(request, template, context)


def blog_post(request, blog_id):
    """
    Display a single blog post
    """
    post = Post.objects.get(id=blog_id)
    print(post)
    template = 'blog/blog_post.html'

    context = {
        'post': post
    }

    return render(request, template, context)
