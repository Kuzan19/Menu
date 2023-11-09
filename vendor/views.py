from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import SubCategory, Category


def index(request):
    return render(request, 'vendor/index.html')


def subcategory(request, slug_subcategory):
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)
    return render(request, 'vendor/some_menu.html', {'subcategory': subcategory})


def category(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    return render(request, 'vendor/some_menu.html', {'category': category})
