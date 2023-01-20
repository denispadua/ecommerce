from django.contrib import admin

from apps.category.models import CategoryModel

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(CategoryModel, CategoryAdmin)