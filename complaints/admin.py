from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'complaint_id',
        'name',
        'subject',
        'status',
        'created_at',
    )

    list_filter = ('status',)

    search_fields = (
        'complaint_id',
        'name',
        'email',
        'subject',
    )

    ordering = ('-created_at',)