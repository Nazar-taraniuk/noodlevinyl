from django.shortcuts import render, redirect
from .forms import VinylOrderForm
from django.contrib.auth.decorators import login_required
from .models import VinylOrder


@login_required
def create_vinyl_order(request):
    if request.method == 'POST':
        form = VinylOrderForm(request.POST, request.FILES)
        if form.is_valid():
            vinyl = form.save(commit=False)
            vinyl.user = request.user
            vinyl.save()
            return redirect('my_orders')  # сторінка з власними замовленнями
    else:
        form = VinylOrderForm()
    return render(request, 'create_vinyl_order.html', {'form': form})

@login_required
def my_orders(request):
    vinyls = VinylOrder.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'vinyls': vinyls})
