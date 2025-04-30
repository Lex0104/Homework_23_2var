from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product, Contacts, Category


def home(request):
    latest_products = Product.objects.order_by('created_at')[:5]
    products_list = Product.objects.all()

    for product in latest_products:
        print(
            f'{product.name_product}: {product.description}. Дата создания: {product.created_at}. Цена: {product.price}')

    paginator = Paginator(products_list, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'home.html', {'products': products})


def contacts(request):
    contacts_list = Contacts.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Мы обязательно с вами свяжемся.")
    return render(request, 'contacts.html', {'contacts': contacts_list})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product_name': product.name_product,
        'description': product.description,
        'image': product.image,
        'category': product.category,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at
    }
    return render(request, 'product_detail.html', context=context)


def add_product(request):

    if request.method == 'POST':
        name_product = request.POST.get('name_product')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)
        product = Product(
            name_product=name_product,
            category=category,
            description=description,
            price=price,
            image=image,
        )

        product.save()
        return HttpResponse(f"Товар {name_product} успешно добавлен!")
    category = Category.objects.all()
    return render(request, 'add_product_user.html', {'categories': category})


def add_category(request):

    if request.method == "POST":
        name_category = request.POST.get('name_category')
        description = request.POST.get("description")

        category = Category(
            name_category = name_category,
            description = description
        )

        category.save()
        return HttpResponse(f"Категория {name_category} успешно добавлена!")
    return render(request, 'add_category_user.html')
