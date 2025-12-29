from django.db import models
from ckeditor.fields import RichTextField

class Job(models.Model):
    # --- Checkboxes & Control ---
    show_in_latest_job = models.BooleanField(default=False, verbose_name="LATEST JOB")
    job_title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Job Section Title")

    show_in_result = models.BooleanField(default=False, verbose_name="LATEST RESULT")
    result_title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Result Section Title")

    show_in_admit_card = models.BooleanField(default=False, verbose_name="ADMIT CARD")
    admit_title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Admit Section Title")

    has_physical_standards = models.BooleanField(default=False, verbose_name="Physical Standards hai?")
    has_selection_mode = models.BooleanField(default=False, verbose_name="Mode of Selection hai?")

    # --- Information Fields (Numbering Hata di gayi hai) ---
    vacancy_name = RichTextField(verbose_name="Vacancy Name", default="Various Posts")
    start_date = RichTextField(verbose_name="Important Dates")
    fee_gen = RichTextField(verbose_name="Application Fee")
    age_limit = RichTextField(verbose_name="Age Limit Details")
    total_posts = RichTextField(verbose_name="Total Posts")
    
    # Detail Sections (Eligibility ko Category Details mein merge kiya gaya hai)
    category_details = RichTextField(verbose_name="Vacancy Details and Eligibility")
    physical_details = RichTextField(verbose_name="Physical Standards", blank=True, null=True)
    selection_mode = RichTextField(verbose_name="Mode Of Selection", blank=True, null=True)
    important_links = RichTextField(verbose_name="Important Links")
    additional_info = RichTextField(verbose_name="Optional Section", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Jo bhi title bhara ho, wahi Admin panel mein dikhega
        if self.job_title:
            return self.job_title
        if self.result_title:
            return self.result_title
        if self.admit_title:
            return self.admit_title
        return "New Entry (No Title)"