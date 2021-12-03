import random
from django.shortcuts import render
from products.models import Category, Review

from .forms import ContactForm


def index(request):
    """
    A view to return the index page
    """

    categories = Category.objects.all()
    reviews = list(Review.objects.all())

    random.shuffle(reviews)

    context = {
        'categories': categories,
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)


def about(request):
    """
    A view to return the about page
    """

    return render(request, 'home/about.html')


def contact(request):
    """
    A view to return the contact page
    """

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'home/contact.html', context)
