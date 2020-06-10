from django.contrib import admin
from .models import Cards


class CardAdmin(admin.ModelAdmin):
    list_display = ('cardname', 'cardnos', 'validity')


admin.site.register(Cards, CardAdmin)