from django.contrib import admin

from apps.product.models import ProductModel

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')

admin.site.register(ProductModel, ProductAdmin)