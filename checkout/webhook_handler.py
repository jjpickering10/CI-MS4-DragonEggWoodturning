import json
import time
from django.http import HttpResponse

from products.models import Product
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """
    Handle webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic webhook event
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded webhook event
        """

        intent = event.data.object
        payment_id = intent.id
        bag = intent.metadata.bag

        billing = intent.charges.data[0].billing_details
        shipping = intent.shipping
        grand_total = round(intent.data.charges[0].amount/100, 2)

        for field, value in shipping.address.items():
            if value == '':
                shipping.address[field] = None

        order_exists = False
        attempts = 1
        while attempts <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping.name,
                    email__iexact=billing.email,
                    phone_number__iexact=shipping.phone,
                    country__iexact=shipping.address.country,
                    postcode__iexact=shipping.address.postal_code,
                    town_or_city__iexact=shipping.address.city,
                    street_address1__iexact=shipping.address.line1,
                    street_address2__iexact=shipping.address.line2,
                    county__iexact=shipping.state,
                    grand_total=grand_total,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempts += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Success! Order already exists',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping.name,
                    email=billing.email,
                    phone_number=shipping.phone,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    town_or_city=shipping.address.city,
                    street_address1=shipping.address.line1,
                    street_address2=shipping.address.line2,
                    county=shipping.state,
                    grand_total=grand_total,
                )
                for item_id, item_quantity in json.loads(bag).items():
                    order_line_item = OrderLineItem(
                        order=order,
                        product=Product.objects.get(id=item_id),
                        quantity=item_quantity
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Error! {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success! created order',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle payment intent succeeded webhook event
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
