from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Order
# Create your views here.

class MyOrderView(DeleteView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True).first()
