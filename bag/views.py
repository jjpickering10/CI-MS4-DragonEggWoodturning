from django.shortcuts import render


def view_bag(request):
    """
    A view to view the shopping bag
    """
    template = 'bag/bag.html'

    context = {}

    return render(request, template, context)