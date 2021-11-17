from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, BlogForm

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


@login_required
def add_blog(request):
    """
    Add blog page
    """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            new_blog = blog_form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect(reverse('blog'))
    else:
        blog_form = BlogForm()

    template = 'blog/add_blog.html'

    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """
    Edit a blog
    """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    post = Post.objects.get(id=blog_id)

    if request.method == 'POST':
        edited_post = BlogForm(request.POST, instance=post)
        if edited_post.is_valid():
            edited_post.save()
            return redirect(reverse('blog_post', args=[post.id]))
    else:
        blog_form = BlogForm(instance=post)

    template = 'blog/edit_blog.html'

    context = {
        'post': post,
        'blog_form': blog_form
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """
    Edit a comment
    """
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        edited_comment = CommentForm(request.POST, instance=comment)
        if edited_comment.is_valid():
            edited_comment.save()
            return redirect(reverse('blog_post', args=[comment.post.id]))
    else:
        comment_form = CommentForm(instance=comment)

    template = 'blog/edit_comment.html'

    context = {
        'comment': comment,
        'comment_form': comment_form
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment
    """
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect(reverse('blog_post', args=[comment.post.id]))
