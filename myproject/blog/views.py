from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import BlogForm
from .models import Blog


class BlogsListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(flag_publication=True)

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter_views += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blogs_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs_list')