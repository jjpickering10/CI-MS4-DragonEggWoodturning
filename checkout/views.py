from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    """
    A view to checkout
    """

    bag = request.session.get('bag', {})

    if not bag:
        return redirect(reverse('all_products'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_testdsff',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
