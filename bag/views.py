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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(id=item_id)
    bag = request.session.get('bag', {})
    print(bag)

    print(type(item_id))
    for id in list(bag.keys()):
        print(type(id))
    
    if str(item_id) in list(bag.keys()):
        bag[str(item_id)] += quantity
        messages.success(request, f'{quantity} more {product.name} added to your bag')
        print('in bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{quantity} {product.name} added to your bag')
        print('NOT in bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove items in the bag
    """
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
    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if str(item_id) in list(bag.keys()):
        bag[str(item_id)] = quantity
        messages.success(request, f'Edited {product.name} to {quantity} items')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
