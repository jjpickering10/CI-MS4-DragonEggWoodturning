from django.shortcuts import render


def blog(request):
    """
    Display blog page
    """

    template = 'blog/blog.html'

    context = {

    }

    return render(request, template, context)
