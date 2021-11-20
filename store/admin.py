from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category', 'modified_date', 'is_availaible')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)


