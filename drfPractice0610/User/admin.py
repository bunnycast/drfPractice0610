from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'username', 'gender', 'language', 'level', 'sendmail')


admin.site.register(Users, UserAdmin)
