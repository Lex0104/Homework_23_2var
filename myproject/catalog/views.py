from django import forms
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .models import Product, Contacts, Category


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        contacts_list = Contacts.objects.all()
        return render(request, self.template_name, {'contacts': contacts_list})

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Мы обязательно с вами свяжемся.")


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ("name_product", "description", "image", "price", "category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name_product"].widget.attrs.update({
            'placeholder': 'Введите название продукта',
            'class': "form-control"
        })

        self.fields["description"].widget = forms.Textarea(attrs={'rows': 3})

        self.fields["description"].widget.attrs.update({
            'placeholder': "Введите описание продукта",
            'class': "form-control"
        })

        self.fields["category"].widget.attrs.update({
            'class': "form-select",
        })

        self.fields["price"].widget.attrs.update({
            'placeholder': "Введите цену продукта",
            'class': "form-control"
        })

        self.fields["image"].widget.attrs.update({
            'class': "form-control"
        })


class ProductCreateView(CreateView):
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('category:home')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name_category", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name_category"].widget.attrs.update({
            'placeholder': 'Введите название категории',
            'class': "form-control"
        })

        self.fields["description"].widget = forms.Textarea(attrs={'rows': 3})

        self.fields["description"].widget.attrs.update({
            'placeholder': 'Введите описание категории',
            'class': "form-control"
        })

class CategoryCreateView(CreateView):
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:create_product')