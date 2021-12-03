import random
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from products.models import Category, Review

from .forms import ContactForm


def index(request):
    """
    A view to return the index page
    """

    categories = Category.objects.all()
    reviews = list(Review.objects.all())

    random.shuffle(reviews)

    context = {
        'categories': categories,
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)


def about(request):
    """
    A view to return the about page
    """

    return render(request, 'home/about.html')


def contact(request):
    """
    A view to return the contact page
    """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email = contact_form.cleaned_data['email']
            subject = render_to_string(
                'home/contact_emails/contact_subject.txt', {
                    'subject': contact_form.cleaned_data['subject']
                    }
                )
            body = render_to_string(
                'home/contact_emails/contact_body.txt', {
                    'message': contact_form.cleaned_data['message'],
                    'name': contact_form.cleaned_data['name'],
                    }
                )

            send_mail(
                subject,
                body,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False)

            auto_reply_subject = render_to_string(
                'home/contact_emails/auto_reply_contact_subject.txt', {
                    'auto_reply_subject': contact_form.cleaned_data['subject']
                    }
                )
            auto_reply_body = render_to_string(
                'home/contact_emails/auto_reply_contact_body.txt', {
                    'contact_message': contact_form.cleaned_data['message'],
                    'contact_name': contact_form.cleaned_data['name'],
                    }
                )

            send_mail(
                auto_reply_subject,
                auto_reply_body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False)
            messages.success(request, 'Message \
                sent!')
            return redirect(reverse('home'))

        else:
            messages.error(
                request,
                'Sorry, there was an error. \
                Please make sure the form is filled out correctly!')
            return redirect(reverse('contact'))

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'home/contact.html', context)
