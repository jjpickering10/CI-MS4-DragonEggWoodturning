from django import forms
from .models import Comment, Post


class BlogForm(forms.ModelForm):
    """
    Form for blog
    """
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('image_url', 'author', 'likes', 'like_count')


class CommentForm(forms.ModelForm):
    """
    Form for comment
    """
    class Meta:
        model = Comment
        fields = ['body']
