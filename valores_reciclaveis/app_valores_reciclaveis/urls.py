from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('valores_descricao', views.prestacao, name='prestacao')
]