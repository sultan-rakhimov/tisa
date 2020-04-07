from django.shortcuts import render
from django.http import HttpResponse
from siteviewer.models import Slide


def home(request):
    slides = Slide.objects.all()
    context = {
        'slides': slides
    }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def tours(request):
    return render(request, 'tours.html')
