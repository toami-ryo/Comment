from django.contrib import admin
from .models import Cell, Theme

# Register your models here.


class ThemeAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title']

admin.site.register(Theme)
