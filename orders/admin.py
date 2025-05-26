from django.contrib import admin
from .models import VinylOrder

@admin.register(VinylOrder)
class VinylOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'user', 'price', 'year', 'created_at')
    list_filter = ('genre', 'year')
    search_fields = ('title', 'artist', 'user__username')
