from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base_page'),
    path('menu/<slug:slug_subcategory>', views.subcategory, name='subcategory_page'),
    path('menu/<slug:slug_category>', views.category, name='category_page'),
]
