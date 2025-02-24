from django.urls import path
from .apps import BlogConfig
from .views import BlogsListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogsListView.as_view(), name='blog_list'),
    path('blogs/create/', BlogCreateView.as_view(), name='add_blog'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]