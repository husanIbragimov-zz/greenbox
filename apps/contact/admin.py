from django.contrib import admin
from apps.contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'department', 'status', 'is_active')
    readonly_fields = ('name', 'email', 'department', 'message', 'created_at')


admin.site.register(Contact, ContactAdmin)
