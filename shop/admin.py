from django.contrib import admin
# Register your models here.
from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','price', 
                    'available', 'created','updated']
    list_filter = ['available', 'created','updated']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ('name',)}