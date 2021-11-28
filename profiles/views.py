from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from products.models import Review, Category, Product
from products.forms import DiscountForm, ProductForm, ImageForm
from newsletter.forms import NewsletterForm
from blog.forms import BlogForm
from blog.models import Post


@login_required
def profile(request):
    """
    Display profile of user
    """
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.order_set.all()
    reviews = Review.objects.filter(user=request.user)
    categories = Category.objects.all()
    products = Product.objects.all()
    blogs = Post.objects.all()

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
        product_form = ProductForm()
        image_form = ImageForm()
        blog_form = BlogForm()
    else:
        newsletter_form = None
        discount_form = None
        product_form = None
        image_form = None
        blog_form = None

    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'orders': orders,
        'reviews': reviews,
        'blogs': blogs,
        'form': form,
        'newsletter_form': newsletter_form,
        'categories': categories,
        'products': products,
        'discount_form': discount_form,
        'product_form': product_form,
        'image_form': image_form,
        'blog_form': blog_form,
    }

    return render(request, template, context)
