from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Product, Image, WoodType
from .forms import ReviewForm, DiscountForm


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
    sort = None
    direction = None

    if request.GET:
        if 'wood' in request.GET:
            wood_search = request.GET['wood']
            products = Product.objects.filter(wood_type__id=wood_search)
            wood_results = WoodType.objects.filter(id=wood_search)

        if 'category' in request.GET:
            categories = request.GET['category']
            products = Product.objects.filter(category=categories)
            categories = Category.objects.filter(id=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'images': images,
        'search_term': query,
        'current_categories': categories,
        'wood_types': wood_types,
        'wood_results': wood_results,
        'all_categories': all_categories,
        'all_products': all_products,
        'current_sorting': current_sorting
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """
    A view to show an individual product
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.review_set.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.product = product
            new_review.save()
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    if request.user.is_superuser:
        discount_form = DiscountForm()
    else:
        discount_form = None

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'discount_form': discount_form,
    }

    return render(request, 'products/product_detail.html', context)


def add_discount(request, product_id):
    """
    A view to add discount
    """

    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        discount_form = DiscountForm(request.POST, instance=product)
        if discount_form.is_valid():
            discount_form.save()
            return redirect(reverse('product_detail', args=[product_id]))


def all_categories(request):
    """
    A view to show all categories
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/all_categories.html', context)
