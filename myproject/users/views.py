from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from .settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm, UserForm
from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = 'Спасибо за регистрацию на нашем сервисе!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('users:user_detail', args=[self.kwargs.get('pk')])
