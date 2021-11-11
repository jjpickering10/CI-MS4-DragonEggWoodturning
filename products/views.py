from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()

    for product in products:
        print(type(product.sku))

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """
    A view to show an individual product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def all_categories(request):
    """
    A view to show all categories
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/all_categories.html', context)
