from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'account_number', 'inn', 'status')
    list_display_links = ('name', 'surname', 'account_number', 'inn', )
    list_filter = ('status', )
    search_fields = ('name', 'surname', 'inn', 'account_number', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'is_staff')
    list_display_links = ('username', )
    list_filter = ('is_superuser', 'is_staff')
    search_fields = ('username', )
    autocomplete_fields = ('clients', )


admin.site.register(Client, ClientAdmin)
admin.site.register(Person, PersonAdmin)
