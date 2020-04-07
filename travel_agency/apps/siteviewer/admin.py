from django.contrib import admin
from siteviewer.models import Slide


class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_display = ['title', 'summary']
    search_fields = ['title']


admin.site.register(Slide, SlideAdmin)
