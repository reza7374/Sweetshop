from django.contrib import admin
from .models import Category, Product,ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "inventory", "is_available")
    list_filter = ("category", "is_available")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "is_primary")


