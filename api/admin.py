from django.contrib import admin

from .models import *


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['owner_address', 'to_address', 'amount']
    list_per_page = 30
    
    search_fields = ['owner_address', 'to_address']
    