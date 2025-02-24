from django.forms import ModelForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = {"title", "content", "preview", "flag_publication"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            'placeholder': 'Введите заголовок блога',
            'class': "form-control"
        })

        self.fields["content"].widget.attrs.update({
            'placeholder': "Напишите содержимое блога",
            'class': "form-control"
        })

        self.fields["preview"].widget.attrs.update({
            'class': "form-control"
        })


class BlogCreateView(CreateView):
    template_name = 'blog/blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs_list')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blogs_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs_list')
