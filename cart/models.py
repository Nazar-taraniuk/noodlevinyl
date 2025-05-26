from django.db import models
from django.contrib.auth.models import User
from main.models import Vinyl

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.vinyl.title} ({self.quantity})"

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('google_pay', 'Google Pay'),
        ('apple_pay', 'Apple Pay'),
        ('cod', 'Післяплата'),
    ]
    DELIVERY_CHOICES = [
        ('nova_poshta', 'Нова Пошта'),
        ('ukr_poshta', 'Укрпошта'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Користувач")

    first_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище клієнта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефону клієнта")

    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='nova_poshta', verbose_name="Спосіб доставки")
    city_ukrposhta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Місто (Укрпошта)")
    street_ukrposhta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вулиця (Укрпошта)")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Поштовий індекс")

    city_nova_poshta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Місто (Нова Пошта)")
    street_nova_poshta = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вулиця (Нова Пошта)")
    nova_poshta_branch = models.CharField(max_length=20, blank=True, null=True, verbose_name="Відділення")

    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name="Спосіб оплати")
    promo_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Промокод")

    products_json = models.JSONField(blank=True, null=True, verbose_name="Товари (JSON)")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сума")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def get_full_address(self):
        if self.delivery_method == 'ukr_poshta':
            return f"{self.city_ukrposhta}, {self.street_ukrposhta}, {self.postal_code}"
        elif self.delivery_method == 'nova_poshta':
            return f"{self.city_nova_poshta}, {self.street_nova_poshta}, Відділення: {self.nova_poshta_branch}"
        return "Адреса не вказана"

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.total_price} грн"

class OrderTracking(models.Model):
    STATUS_CHOICES = (
        ('new', 'Нове'),
        ('processing', 'В обробці'),
        ('shipped', 'Відправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Скасовано'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')


    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)
