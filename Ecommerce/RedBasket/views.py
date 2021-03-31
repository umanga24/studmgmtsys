from django.shortcuts import render
from django.http import JsonResponse
import json

from RedBasket.models import Product, Orderiteam, Order, ShippingAddress


def store(request):
    products = Product.objects.all
    return render(request, 'RB/store.html',{'products': products})

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete=False)
        items = order.orderiteam_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items' : items, 'order':order}
    return render(request, 'RB/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete=False)
        items = order.orderiteam_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items' : items, 'order':order}
    return render(request, 'RB/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderIteam, created = Orderiteam.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderIteam.quantity = (orderIteam.quantity + 1)
    elif action == 'remove':
        orderIteam.quantity = (orderIteam.quantity - 1)

    orderIteam.save()


    if orderIteam.quantity <= 0:
        orderIteam.delete()

    return JsonResponse('Ieam was added', safe=False)

