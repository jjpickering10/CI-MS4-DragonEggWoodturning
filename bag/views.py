from django.shortcuts import render, redirect, reverse
from django.contrib import messages


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
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, 'Added')
    else:
        bag[item_id] = quantity
        messages.success(request, 'Added')

    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove items in the bag
    """
    bag = request.session.get('bag', {})
    
    if str(item_id) in list(bag.keys()):
        bag.pop(str(item_id))

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
