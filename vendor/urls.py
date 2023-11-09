from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base_page'),
    path('menu/<slug:slug_menu>', views.menu, name='menu_page'),
]
