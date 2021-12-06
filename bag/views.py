from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view to view the shopping bag
    """
    template = 'bag/bag.html'

    context = {}

    return render(request, template, context)


def add_to_bag(request, item_id):
    """
    Add quantity of items to the bag
    """
    if not Product.objects.filter(id=item_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('home'))

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(id=item_id)
    bag = request.session.get('bag', {})

    if str(item_id) in list(bag.keys()):
        if bag[str(item_id)] + quantity > 10:
            messages.warning(request, 'Sorry, maximum 10 items of each')
            return redirect(redirect_url)
        else:
            bag[str(item_id)] += quantity
            messages.success(
                request, f'{quantity} more {product.name} added to your bag')

    else:
        bag[item_id] = quantity
        messages.success(
            request, f'{quantity} {product.name} added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove items in the bag
    """
    if not Product.objects.filter(id=item_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('home'))

    product = Product.objects.get(id=item_id)
    bag = request.session.get('bag', {})

    if str(item_id) in list(bag.keys()):
        bag.pop(str(item_id))
        messages.success(request, f'All {product.name} removed from your bag')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def edit_bag(request, item_id):
    """
    Edit items in the bag
    """
    if not Product.objects.filter(id=item_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('home'))

    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if str(item_id) in list(bag.keys()):
        bag[str(item_id)] = quantity
        messages.success(request, f'Edited {product.name} to {quantity} items')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
