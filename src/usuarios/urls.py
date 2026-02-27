from django.urls import path
from .views import CustomLoginView, RegistroView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login_basico'),
    path('registro/', RegistroView.as_view(), name='registro'),
]