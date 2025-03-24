from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, CategoryCreateView, \
    ProductUpdateView, ProductDeleteView, ProductsByCategoryView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('product/create/', ProductCreateView.as_view(), name="create_product"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name="update_product"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="delete_product"),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('category/<int:category_id>/list', ProductsByCategoryView.as_view(), name='products_by_category')
]