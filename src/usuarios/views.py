from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse(f"Bienvenido {request.user.username} 🎉")



import requests
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib import messages

class CustomLoginView(LoginView):
    # 🔹 PASAR LA CLAVE DE RECAPTCHA AL TEMPLATE
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY
        return context
    template_name = "registration/login.html"

# 🔹 VALIDAR EL RECAPTCHA AL ENVIAR EL FORM
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
