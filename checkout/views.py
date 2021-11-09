from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from bag.contexts import bag_contents
import stripe


def checkout(request):
    """
    A view to checkout
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'post_code': request.POST.get('post_code'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()

            for item_id, item_quantity in bag.items():
                order_line_item = OrderLineItem(
                    order=order,
                    product=Product.objects.get(id=item_id),
                    quantity=item_quantity
                )
                order_line_item.save()
        
            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        bag = request.session.get('bag', {})
        
        if not bag:
            return redirect(reverse('all_products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    A view to checkout success page
    """

    order = get_object_or_404(Order, order_number=order_number)
    print(order.full_name)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }

    return render(request, template, context)