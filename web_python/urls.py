from django.urls import path
from webapp_python import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.results, name="cadastrar_produtos"),
    path('', views.sucess, name="sucess"),
    path('consulta/', views.consulta, name="consulta"),
]