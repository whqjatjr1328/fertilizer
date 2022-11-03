from django.contrib import admin

# Register your models here.
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'published_date']
    list_display_links = ['id', 'title']
    list_per_page = 10
