from django.contrib import admin
from .models import Therapist

class TherapistAdmin(admin.ModelAdmin):
    list_display = ('user', 'therapist_name', 'is_approved', 'amhs_id', 'created_at')
    list_display_links = ('user', 'therapist_name')

# Register your models here.
admin.site.register(Therapist, TherapistAdmin)