from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistroForm
from .models import Aspirante


@login_required
def home(request):
    return HttpResponse(f"Bienvenido {request.user.username} 🎉")


class CustomLoginView(LoginView):
    # 🔹 PASAR LA CLAVE DE RECAPTCHA AL TEMPLATE
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY
        return context
    template_name = "registration/login.html"

# 🔹 VALIDAR EL RECAPTCHA AL ENVIAR EL FORM - LOGIN
    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=data
        )
        result = r.json()

        if result.get('success'):
            return super().form_valid(form)
        else:
            messages.error(self.request, "Verifica que no eres un robot.")
            return redirect('login_basico')

# 🔹 FORMULARIO DE REGISTRO
class RegistroView(CreateView):
    template_name = "registration/register.html"
    form_class = RegistroForm
    success_url = reverse_lazy("login_basico")

    def form_valid(self, form):
        response = super().form_valid(form)  # Guarda el usuario

        Aspirante.objects.create(
            user=self.object,  # Usuario recién creado
            clave_elector=form.cleaned_data["clave_elector"],
            nombre=form.cleaned_data["nombre"],
            primer_apellido=form.cleaned_data["primer_apellido"],
            segundo_apellido=form.cleaned_data["segundo_apellido"],
            celular=form.cleaned_data["celular"],
            como_se_entero=form.cleaned_data["como_se_entero"]
        )

        return response