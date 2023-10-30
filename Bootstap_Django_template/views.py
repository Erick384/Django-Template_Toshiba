from django.shortcuts import render


def layout(request):
    return render(request, 'layout.html')


def index(request):
    return render(request, 'index.html')


def error(request):
    return render(request, '404.html')


def product(request):
    return render(request, 'product.html')


def service(request):
    return render(request, 'service.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def team(request):
    return render(request, 'team.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
