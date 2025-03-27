from django.contrib import admin
from .models import Category, Product, Contacts

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)
    search_field = ('name_category', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'category',)
    list_filter = ('category',)
    search_field = ('name_product', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'address')