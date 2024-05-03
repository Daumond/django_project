import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save()
        # Создаем и сохраняем токен подтверждения
        token = get_random_string(length=35)
        new_user.verification_token = token
        new_user.save()
        # Отправляем письмо с подтверждением
        current_site = get_current_site(self.request)
        mail_subject = 'Верификация аккаунта'
        message = (
            f'Поздравляем, Вы зарегистрировались на нашем портале!\n'
            f'Для подтверждения вашей электронной почты перейдите по следующей ссылке:\n'
            f'http://{current_site.domain}{reverse("users:verify_email", kwargs={"uid": new_user.pk, "token": token})}'
        )
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return response


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    """
    Генерация нового пароля и отправка его на почту пользователя
    """
    redirect('generate_new_password.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(9)])

            user = User.objects.get(email=email)

            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )

            user.set_password(new_password)
            user.save()
            return redirect(reverse('users:login'))
        except User.DoesNotExist:
            return redirect(reverse('users:login'))




class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = get_object_or_404(User, pk=uid, verification_token=token)
            user.is_active = True
            user.save()
            return render(request, 'users/registration_success.html')  # Покажем сообщение о регистрации
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')  # Покажем сообщение об ошибке
