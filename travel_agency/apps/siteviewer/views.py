from django.shortcuts import render, redirect, reverse
from .models import Slide, Customer, Country, Tour


def home(request):
    slides = Slide.objects.all()
    return render(request, 'siteviewer/home.html', {'slides': slides})


def contact(request):
    return render(request, 'siteviewer/contact.html')


def about(request):
    return render(request, 'siteviewer/about.html')


def news(request):
    return render(request, 'siteviewer/news.html')


def tours(request):
    countries = Country.objects.all()
    tours = Tour.objects.all()
    return render(request, 'siteviewer/tours.html', {'countries': countries, 'tours': tours})


def customer(request):
    if request.method == 'POST':
        Customer.objects.create(first_name=request.POST.get(
            'first_name'), last_name=request.POST.get('last_name'), email=request.POST.get('email'), phone=request.POST.get('phone'))
        return redirect(reverse('contact'))
