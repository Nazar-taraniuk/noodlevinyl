from django.db import models
from django.contrib.auth.models import User
import random

def random_price():
    return random.choice(range(10000, 30001, 1000))  # лише круглі ціни

class VinylOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='order_images/')
    price = models.PositiveIntegerField(default=random_price)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist} (by {self.user.username})"
