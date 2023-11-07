from django.urls import path
from webapp_python import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:weppapp_python_produtos_nome>/", views.results, name="results"),
]
