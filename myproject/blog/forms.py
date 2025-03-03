from django.forms import ModelForm

from .models import Blog


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