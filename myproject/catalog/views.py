from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import ProductForm, CategoryForm, ProductModeratorForm
from .models import Product, Contacts


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.groups.filter(name='Product Moderator').exists():
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор продуктов').exists()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:create_product')


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