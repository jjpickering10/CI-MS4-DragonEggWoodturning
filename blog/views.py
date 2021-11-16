from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import CommentForm

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

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect(reverse('blog_post', args=[blog_id]))
        else:
            return redirect(reverse('blog_post', args=[blog_id]))

    comment_form = CommentForm()
    template = 'blog/blog_post.html'

    context = {
        'post': post,
        'comment_form': comment_form
    }

    return render(request, template, context)
