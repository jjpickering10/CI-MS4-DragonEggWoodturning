from newsletter.forms import SubscribersForm


def subscribers(request):

    subscribers_form = SubscribersForm()

    context = {
        'subscribers_form': subscribers_form
    }

    return context
