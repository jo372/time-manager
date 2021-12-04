from django.urls import reverse_lazy
from django.views.generic import CreateView 
from core.forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = '../templates/registration/register.html'
    success_url = reverse_lazy('login')