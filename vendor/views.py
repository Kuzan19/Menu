from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import SubCategory, Category


def index(request):
    return render(request, 'vendor/index.html')


def menu(request, slug_menu):
    try:
        menu = get_object_or_404(Category, slug=slug_menu)
    except Exception:
        menu = get_object_or_404(SubCategory, slug=slug_menu)
    return render(request, 'vendor/some_menu.html', {"menu": menu})

