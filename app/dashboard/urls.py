from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    # inicialización
    path('imagen/list/', ImagenListView.as_view(), name='imagen_list'),
    path('imagen/add/', ImagenCreateView.as_view(), name='imagen_create'),
    path('imagen/edit/<int:pk>', ImagenUpdateView.as_view(), name='imagen_update'),
    path('imagen/delete/<int:pk>', ImagenDeleteView.as_view(), name='imagen_delete'),

    path('instalacion/list/', InstalacionListView.as_view(), name='instalacion_list'),
    path('instalacion/add/', InstalacionCreateView.as_view(), name='instalacion_create'),
    path('instalacion/edit/<int:pk>', InstalacionUpdateView.as_view(), name='instalacion_update'),
    path('instalacion/delete/<int:pk>', InstalacionDeleteView.as_view(), name='instalacion_delete'),
]
