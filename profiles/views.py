from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from products.models import Review
from newsletter.forms import NewsletterForm


@login_required
def profile(request):
    """
    Display profile of user
    """
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.order_set.all()
    reviews = Review.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)

    if request.user.is_superuser:
        print('superuser')
        newsletter_form = NewsletterForm()
    else:
        print('not-super-user')
        newsletter_form = None

    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'orders': orders,
        'reviews': reviews,
        'form': form,
        'newsletter_form': newsletter_form
    }

    return render(request, template, context)
