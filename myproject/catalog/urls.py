from django.urls import path
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, CategoryCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('create_product/', ProductCreateView.as_view(), name="create_product"),
    path('create_category/', CategoryCreateView.as_view(), name='create_category')
]