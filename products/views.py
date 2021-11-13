from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Category, Product, Image, WoodType


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()
    images = Image.objects.all()
    wood_types = WoodType.objects.all()
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    query = None
    categories = None
    current_categories = None
    wood_search = None
    wood_results = None

    if request.GET:
        if 'wood' in request.GET:
            wood_search = request.GET['wood']
            print(wood_search)
            # products = products.filter(wood_type__id__in=wood_search)
            products = Product.objects.filter(wood_type__id=wood_search)
            wood_results = WoodType.objects.filter(id=wood_search)

        if 'category' in request.GET:
            categories = request.GET['category']
            # products = products.filter(category__id__in=categories)
            products = Product.objects.filter(category=categories)
            categories = Category.objects.filter(id=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            print(query)

    context = {
        'products': products,
        'images': images,
        'search_term': query,
        'current_categories': categories,
        'wood_types': wood_types,
        'wood_results': wood_results,
        'all_categories': all_categories,
        'all_products': all_products
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
