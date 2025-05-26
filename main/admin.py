from django.contrib import admin
from main.models import Artist, Vinyl

admin.site.register(Artist)

@admin.register(Vinyl)
class VinylAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)