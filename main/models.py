from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50, blank=True, default='Unknown')
    description = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name

class Vinyl(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='vinyls')
    genre = models.CharField(max_length=100, default='Various')
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='vinyl_images/', height_field = None , width_field = None, blank=True, null=True)
    hover_image = models.ImageField(upload_to='vinyls_hover/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.artist.name})"
