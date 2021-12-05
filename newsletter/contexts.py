from newsletter.forms import SubscribersForm


def subscribers(request):
    """
    Returns subscriber form throughout site
    """
    subscribers_form = SubscribersForm()

    context = {
        'subscribers_form': subscribers_form
    }

    return context
