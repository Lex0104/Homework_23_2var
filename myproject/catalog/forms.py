from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Product, Category
from .validators import validate_price


class ProductForm(ModelForm):

    restriction = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

    def clean_name_product(self):

        name_product = self.cleaned_data['name_product']

        if any(restricted_term in name_product.lower() for restricted_term in self.restriction):
            raise ValidationError("Имя содержит недопустимое(ые) слово(а)")
        return name_product

    def clean_description(self):

        description = self.cleaned_data['description']

        if any(restricted_term in description.lower() for restricted_term in self.restriction):
            raise ValidationError("Описание содержит недопустимое(ые) слово(а)")
        return description

    def clean_price(self):

        price = self.cleaned_data['price']
        validate_price(price)
        return price

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


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

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