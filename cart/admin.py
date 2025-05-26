from .models import Order, OrderTracking
from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
admin.site.register(Order)


@admin.register(OrderTracking)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
    list_filter = ('status', 'user')
    search_fields = ('id', 'user__username')
    list_editable = ('status',)
    actions = ['send_status_update']

    def send_status_update(self, request, queryset):
        for order in queryset:
            if order.user.email:
                subject = f'Статус вашого замовлення #{order.id} оновлено'
                message = f'''
                Доброго дня, {order.user.username}!

                Статус вашого замовлення #{order.id} змінено на: {order.get_status_display()}

                Дякуємо за покупку!
                Команда Вінілового Архіву
                '''
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [order.user.email],
                    fail_silently=False,
                )
        self.message_user(request, f"Повідомлення про оновлення статусу відправлено для {queryset.count()} замовлень")

    send_status_update.short_description = "Надіслати сповіщення про зміну статусу"