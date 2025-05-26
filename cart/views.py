from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import Vinyl
from .models import CartItem, Order
from .forms import OrderForm
from django.contrib import messages
import json

@login_required
def add_to_cart(request, vinyl_id):
    vinyl = get_object_or_404(Vinyl, id=vinyl_id)
    item, created = CartItem.objects.get_or_create(user=request.user, vinyl=vinyl)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, "Додано до кошика!")
    return redirect('cart')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.vinyl.price * item.quantity for item in items)

    recommended_vinyls = Vinyl.objects.order_by('?')[:3]

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total,
        'recommended_vinyls': recommended_vinyls,
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.warning(request, "Платівку видалено з кошика.")
    return redirect('cart')



@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.vinyl.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        delivery_method = request.POST.get('delivery_method')
        payment_method = request.POST.get('payment_method')
        promo_code = request.POST.get('promo_code')

        order_data = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'delivery_method': delivery_method,
            'payment_method': payment_method,
            'promo_code': promo_code,
            'user': request.user,
            'total_price': total_price,
            'products_json': json.dumps([
                {
                    'vinyl': item.vinyl.title,
                    'quantity': item.quantity,
                    'price': float(item.vinyl.price),
                } for item in cart_items
            ])
        }

        # Доставка
        if delivery_method == 'ukr_poshta':
            order_data.update({
                'city_ukrposhta': request.POST.get('city_ukrposhta'),
                'street_ukrposhta': request.POST.get('street_ukrposhta'),
                'postal_code': request.POST.get('postal_code'),
            })
        elif delivery_method == 'nova_poshta':
            order_data.update({
                'city_nova_poshta': request.POST.get('city_nova_poshta'),
                'street_nova_poshta': request.POST.get('street_nova_poshta'),
                'nova_poshta_branch': request.POST.get('nova_poshta_branch'),
            })

        Order.objects.create(**order_data)
        cart_items.delete()

        messages.success(request, "Замовлення успішно оформлено!")
        return redirect('cart/checkout_success')

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cart/orders.html', {'orders': orders})

@login_required
def order_tracking(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_tracking.html', {'orders': orders})

def checkout_success(request):
    return render(request, 'cart/checkout_success.html')