from django.shortcuts import render
from .models import Category, Product


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)

def all_categories(request):
    """
    A view to show all categories
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/all_categories.html', context)
