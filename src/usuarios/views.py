from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse(f"Bienvenido {request.user.username} 🎉")