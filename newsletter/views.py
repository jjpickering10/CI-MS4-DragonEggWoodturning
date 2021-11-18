from django.shortcuts import render, redirect, reverse
from .models import Subscribers
from .forms import SubscribersForm


def subscribe(request):
    """
    Subscribe to newsletter
    """

    current_subscribers = Subscribers.objects.all()
    print(current_subscribers)

    if request.method == 'POST':
        new_subscriber = request.POST.get('email')
        if current_subscribers.filter(email=new_subscriber).exists():
            print('already exists')
            return redirect(reverse('home'))
        else:
            subscriber_form = SubscribersForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                return redirect(reverse('home'))
            else:
                return redirect(reverse('home'))

    return redirect(reverse('home'))
