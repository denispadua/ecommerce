from django.contrib import admin

from apps.user.models import UserModel


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

admin.site.register(UserModel, UserAdmin)