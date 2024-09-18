from django.contrib import admin

from .models import *
from import_export.admin import ImportExportActionModelAdmin


admin.site.register(Block, ImportExportActionModelAdmin)
admin.site.register(Transactions, ImportExportActionModelAdmin)


# @admin.register(Transactions)
# class TransactionsAdmin(admin.ModelAdmin):
#     list_display = ['owner_address', 'to_address', 'amount']
#     list_per_page = 30
    
#     search_fields = ['owner_address', 'to_address']
    