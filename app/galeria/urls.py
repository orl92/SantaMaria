from django.urls import path
from .views import *

urlpatterns = [
    path('casablanca', GaleriaCasablancaTemplateView.as_view(), name='casablanca'),
    path('cafeciudad', GaleriaCafeciudadTemplateView.as_view(), name='cafeciudad'),
    path('isabella', GaleriaIsabellaTemplateView.as_view(), name='isabella'),
]
