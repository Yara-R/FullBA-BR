from django.urls import path
from app_FullBA import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('treino/', views.treino, name='treino'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('musculo/', views.smash, name='smash'),
    path('consumo_agua/', views.registro, name='registro_agua'),
    path('medidas/', views.medidas, name= 'medidas'),
    path('usuarios/', views.usuario, name= 'usuarios'),
    path('perfil/', views.perfil, name='perfil'),
    
]
