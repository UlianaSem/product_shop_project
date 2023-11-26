from django.contrib import admin

from shop.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug_name', 'picture']
    search_fields = ['name', 'pk']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug_name', 'picture']
    search_fields = ['name', 'pk']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug_name', 'picture', "price", "subcategory"]
    list_filter = ['subcategory']
    search_fields = ['name', 'pk']
