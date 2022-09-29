from django.contrib import admin
from apps.account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'username', 'is_active')
    readonly_fields = ('date_login', 'date_created',)
    search_fields = ('id', 'first_name', 'last_name', 'username')
    list_filter = ('date_created', 'is_active')
    date_hierarchy = 'date_created'


admin.site.register(Account, AccountAdmin)
