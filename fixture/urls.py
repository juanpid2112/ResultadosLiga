from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartidosActuales.as_view(), name='partidos-actuales'),
    path('partido/<int:id>/', views.PartidoEspecifico.as_view(), name='partido-especifico'),
]