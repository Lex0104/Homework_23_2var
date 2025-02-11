from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Contacts


def home(request):
    latest_products = Product.objects.order_by('created_at')[:5]

    for product in latest_products:
        print(
            f'{product.name_product}: {product.description}. Дата создания: {product.created_at}. Цена: {product.price}')

    return render(request, 'home.html')


def contacts(request):
    contacts_list = Contacts.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Мы обязательно с вами свяжемся.")
    return render(request, 'contacts.html', {'contacts': contacts_list})
