from django.contrib import admin
from siteviewer.models import Slide, Customer


class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'date']
    search_fields = ['title']


admin.site.register(Slide, SlideAdmin)
admin.site.register(Customer)
