from django.contrib import admin
from .models import Slide, Customer, Country, Tour


class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'date']
    search_fields = ['title']


admin.site.register(Slide, SlideAdmin)
admin.site.register(Customer)
admin.site.register(Country)
admin.site.register(Tour)
