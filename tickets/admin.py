from django.contrib import admin
from .models import RepairTicket


@admin.register(RepairTicket)
class RepairTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'device_type', 'device_model', 'status', 'date_received', 'estimated_cost')
    list_filter = ('status', 'device_type')
    search_fields = ('customer_name', 'device_model', 'customer_phone')
