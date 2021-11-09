import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks
    """
    # Webhook setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Webhook data and signature verification
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
    # Invalid payload
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
    # Invalid signature
        return HttpResponse(status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up webhook

    handler = StripeWH_Handler(request)

    # Map events to handler functions

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get type from stripe

    event_type = event['type']

    # Get handler from event map otherwise use generic handler

    event_handler = event_map.get(event_type, handler.handle_event)

    # Call handler

    response = event_handler(event)
    return response
