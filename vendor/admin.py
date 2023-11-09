from django.contrib import admin
from .models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fields = ['name', ]
    list_display = ['name', 'slug', ]
    readonly_fields = ('slug', )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):

    fields = ['name', 'parent', 'category']
    ordering = ['name']
    list_display = ['name', 'slug', 'parent', 'category' ]
    readonly_fields = ('slug', )

