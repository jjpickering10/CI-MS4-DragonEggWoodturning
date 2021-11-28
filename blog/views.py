from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, BlogForm

from django.contrib import messages

def blog(request):
    """
    Display blog page
    """
    posts = Post.objects.all()
    for post in posts:
        print(post.comment_set.all())

    query = None

    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('blog'))

            queries = Q(title__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)

    template = 'blog/blog.html'

    context = {
        'posts': posts,
        'search_term': query,
    }

    return render(request, template, context)


def blog_post(request, blog_id):
    """
    Display a single blog post
    """
    post = Post.objects.get(id=blog_id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    print(post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, f'New comment added to {post.title}')
            return redirect(reverse('blog_post', args=[blog_id]))
        else:
            messages.error(request, 'Error posting comment')
            return redirect(reverse('blog_post', args=[blog_id]))

    comment_form = CommentForm()
    template = 'blog/blog_post.html'

    context = {
        'post': post,
        'comment_form': comment_form,
        'liked': liked
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """
    Add blog page
    """

    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            new_blog = blog_form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            messages.success(request, 'New blog added')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Error posting blog')
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
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('home'))

    post = Post.objects.get(id=blog_id)

    if request.method == 'POST':
        edited_post = BlogForm(request.POST, instance=post)
        if edited_post.is_valid():
            edited_post.save()
            messages.success(request, f'Blog post {post.title} edited')
            return redirect(reverse('blog_post', args=[post.id]))
        else:
            messages.error(request, f'Error editing post {post.title}')
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
def delete_blog(request, blog_id):
    """
    Delete a blog post
    """
    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('home'))
        
    post = Post.objects.get(id=blog_id)
    post.delete()
    messages.success(request, f'Blog post {post.title} deleted')

    return redirect(reverse('blog'))


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
            messages.success(request, f'Comment on post {comment.post.title} edited')
            return redirect(reverse('blog_post', args=[comment.post.id]))
        else:
            messages.error(request, f'Error editing comment on post {comment.post.title}')
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
    messages.success(request, f'Comment on post {comment.post.title} deleted')

    return redirect(reverse('blog_post', args=[comment.post.id]))


@login_required
def like_post(request, blog_id):
    """
    View for liking and unliking a post
    """
    if not request.user.is_authenticated:
        messages.info(request, 'Only registered users can like a post')
        return redirect(reverse('blog_post', args=[blog_id]))
    
    post = Post.objects.get(id=blog_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.like_count -=1
        post.save()
        messages.success(request, f'You unliked {post.title}')
    else:
        post.likes.add(request.user)
        post.like_count +=1
        post.save()
        messages.success(request, f'You liked {post.title}')
    
    return redirect(reverse('blog_post', args=[blog_id]))