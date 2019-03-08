from django.contrib import admin

from . import models


@admin.register(models.ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'company', 'start_date', 'resume')
    ordering = ('user', '-start_date')

@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title",)

    class Meta:
        model = models.Resume
