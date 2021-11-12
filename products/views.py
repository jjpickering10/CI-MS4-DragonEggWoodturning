from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Category, Product, Image


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()
    images = Image.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            print(categories)
            products = products.filter(category__id__in=categories)
            categories = Category.objects.filter(id__in=categories)
            for product in products:
                print(product.name)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'images': images,
        'search_term': query,
        'current_categories': categories,
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
