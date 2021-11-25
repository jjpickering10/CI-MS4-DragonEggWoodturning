from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from products.models import Review, Category
from products.forms import DiscountForm
from newsletter.forms import NewsletterForm


@login_required
def profile(request):
    """
    Display profile of user
    """
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.order_set.all()
    reviews = Review.objects.filter(user=request.user)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update profile')

    else:
        form = UserProfileForm(instance=profile)

    if request.user.is_superuser:
        newsletter_form = NewsletterForm()
        discount_form = DiscountForm()
    else:
        newsletter_form = None
        discount_form = None

    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'orders': orders,
        'reviews': reviews,
        'form': form,
        'newsletter_form': newsletter_form,
        'categories': categories,
        'discount_form': discount_form,
    }

    return render(request, template, context)
