from django.shortcuts import render
from products.models import Category

def index(request):
    """
    A view to return the index page
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
