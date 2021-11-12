from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile


@login_required
def profile(request):
    """
    Display profile of user
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'

    context = {
        'profile': profile
    }

    return render(request, template, context)
