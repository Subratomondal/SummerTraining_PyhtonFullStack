from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, OrderItem
from .forms import OrderForm
from users.models import BuyerProfile

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.user.is_authenticated or not hasattr(request.user, 'buyerprofile'):
        return redirect('login')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # Create order
            order = Order.objects.create(
                buyer=request.user,
                total_amount=total_price,
                status='Placed'
            )

            # Create order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            return render(request, 'orders/order_success.html', {
                'product': product,
                'order': order
            })

    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {
        'product': product,
        'form': form
    })

