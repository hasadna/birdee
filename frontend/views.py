from account.forms import AccountCreationForm
from account.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/main.html'


class AccountRegisterView(CreateView):
    model = Account
    form_class = AccountCreationForm
    template_name = 'registration/register.html'
