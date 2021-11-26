from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages

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
            if request.user.is_authenticated:
                new_review.user = request.user
            new_review.product = product
            new_review.save()
            messages.success(request, f'Review for {product.name} added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Error posting review for {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    if request.user.is_superuser:
        if product.discounted:
            discount_form = DiscountForm(instance=product)
        else:
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
            messages.success(request, f'Discount for {product.name} added')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, f'Error giving discount for {product.name}')
            return redirect(reverse('product_detail', args=[product_id]))


def category_discount(request, category_id):
    """
    A view to add discounts to all products in one category
    """

    products = Product.objects.filter(category=category_id)
    category = Category.objects.get(id=category_id)
    # print(products)

    discount = request.POST.get('discount_choices')
    print('discount', discount)

    for product in products:
        discount_form = DiscountForm(request.POST, instance=product)
        if discount_form.is_valid():
            discount_form.save()

    if discount:
        category.on_sale = True
        category.on_sale_amount = int(discount)
        messages.success(request, f'{discount} for all {category.name} products added')
    else:
        category.on_sale = False
        category.on_sale_amount = None
        messages.success(request, f'No discount for {category.name} products')
    category.save()
    return redirect(reverse('profile'))


def all_categories(request):
    """
    A view to show all categories
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/all_categories.html', context)
