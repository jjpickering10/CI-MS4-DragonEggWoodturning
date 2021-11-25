from django.shortcuts import render, redirect, reverse
from .models import Subscribers
from .forms import SubscribersForm, NewsletterForm

from django.contrib import messages



def subscribe(request):
    """
    Subscribe to newsletter
    """

    current_subscribers = Subscribers.objects.all()
    print(current_subscribers)

    if request.method == 'POST':
        new_subscriber = request.POST.get('email')
        if current_subscribers.filter(email=new_subscriber).exists():
            messages.info(request, 'Email already subscribed')
            return redirect(reverse('home'))
        else:
            subscriber_form = SubscribersForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, 'Thank you for subscribing')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Invalid email given')
                return redirect(reverse('home'))

    return redirect(reverse('home'))


def unsubscribe(request, unsubscribe_id):
    """
    Unsubscribe to newsletter
    """
    subscribers = Subscribers.objects.all()
    current_subscriber = None
    if subscribers.filter(unsubscribe=unsubscribe_id).exists():
        current_subscriber = Subscribers.objects.get(unsubscribe=unsubscribe_id)
        current_subscriber.delete()
        messages.success(request, 'Unsubscribed')
    else:
        messages.info(request, 'Already unsubscribed')
        return redirect(reverse('home'))

    template = 'newsletter/unsubscribe.html'

    context = {
        'current_subscriber': current_subscriber,
    }

    return render(request, template, context)


def send_newsletter(request):
    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Newsletter sent to subscribers')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Error posting newsletter')
            return redirect(reverse('profile'))
