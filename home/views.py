from django.shortcuts import render
from products.models import Category, Review

import random

def index(request):
    """
    A view to return the index page
    """

    categories = Category.objects.all()
    reviews = list(Review.objects.all())

    random.shuffle(reviews)
    reviews = reviews

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
