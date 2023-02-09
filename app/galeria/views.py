from django.views.generic import TemplateView
from .models import *
from .util import _Skip


# Create your views here.
class GaleriaCasablancaTemplateView(TemplateView):
    template_name = 'casablanca/casablanca.html'

    def get_context_data(self, **kwargs):
        instalacion = Instalacion.objects.get(pk=1)
        imagenes = Imagen.objects.filter(instalacion_id=1)
        first, last = imagenes.first(), imagenes.last()

        _skip = []
        for i in range(len(imagenes)):
            if imagenes[i].id == first.id:
                _now, _next, _previous = imagenes[i].id, imagenes[i + 1].id, last.id
                _skip.append(_Skip(_now, _next, _previous))
            elif imagenes[i].id == last.id:
                _now, _next, _previous = imagenes[i].id, first.id, imagenes[i - 1].id
                _skip.append(_Skip(_now, _next, _previous))
            else:
                _now, _next, _previous = imagenes[i].id, imagenes[i + 1].id, imagenes[i - 1].id
                _skip.append(_Skip(_now, _next, _previous))

        context = super().get_context_data(**kwargs)
        context['title'] = 'Santa María | Bar Casablanca'
        context['instalacion'] = instalacion
        context['imagenes'] = imagenes
        context['skip'] = _skip

        return context


class GaleriaCafeciudadTemplateView(TemplateView):
    template_name = 'cafeciudad/cafeciudad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Santa María | Cafeciudad'

        return context


class GaleriaIsabellaTemplateView(TemplateView):
    template_name = 'isabella/isabella.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Santa María | Isabella'

        return context


