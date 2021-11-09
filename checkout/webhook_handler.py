from django.http import HttpResponse


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
        print(intent)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
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
