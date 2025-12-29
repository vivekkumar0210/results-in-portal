from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    # --- Custom Function: Jo bhara ho wo title dikhaye ---
    def display_name(self, obj):
        # Pehle check karega Job Title, fir Result, fir Admit Card
        return obj.job_title or obj.result_title or obj.admit_title or "Untitled Entry"
    
    # Column ka naam set karein
    display_name.short_description = 'Entry Title (Job/Result/Admit)'

    # list_display mein 'job_title' ki jagah 'display_name' likhein
    list_display = ('display_name', 'show_in_latest_job', 'show_in_result', 'show_in_admit_card', 'created_at')
    
    # Sidebar filters
    list_filter = ('show_in_latest_job', 'show_in_result', 'show_in_admit_card')
    
    # Search bar (teeno titles mein search karega)
    search_fields = ('job_title', 'result_title', 'admit_title')

    # Fieldsets (Wahi jo pehle the)
    fieldsets = (
        ('Control & Visibility', {
            'fields': (
                'show_in_latest_job', 'job_title',
                'show_in_result', 'result_title',
                'show_in_admit_card', 'admit_title',
            )
        }),
        ('Basic Information', {
            'fields': ('vacancy_name', 'start_date', 'fee_gen', 'age_limit', 'total_posts')
        }),
        ('Main Content', {
            'fields': ('category_details', 'important_links')
        }),
        ('Additional Sections', {
            'fields': ('has_physical_standards', 'physical_details', 'has_selection_mode', 'selection_mode', 'additional_info'),
            'classes': ('collapse',),
        }),
    )