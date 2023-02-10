from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import InstalacionForm, ImagenForm
from app.galeria.models import Instalacion, Imagen


class ShowInst:
    def __int__(self, i1=None, i2=None, i3=None, i4=None):
        self.__i1, self.__i2, self.__i3, self.__i4 = i1, i2, i3, i4

    @property
    def i1(self):
        return self.__i1

    @property
    def i2(self):
        return self.__i2

    @property
    def i3(self):
        return self.__i3

    @property
    def i4(self):
        return self.__i4


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        gas = Instalacion.objects.filter(categoria_id=1)
        alo = Instalacion.objects.filter(categoria_id=2)
        tra = Instalacion.objects.filter(categoria_id=3)
        com = Instalacion.objects.filter(categoria_id=4)

        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['gas'] = gas
        context['alo'] = alo
        context['tra'] = tra
        context['com'] = com
        return context


class ImagenListView(ListView):
    model = Imagen
    template_name = 'imagen/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Imagen.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('imagen_create')
        context['list_url'] = reverse_lazy('imagen_list')
        context['entity'] = 'Categorías'
        context['entity2'] = 'Instalaciones'
        return context


class ImagenCreateView(CreateView):
    model = Imagen
    form_class = ImagenForm
    template_name = 'imagen/create.html'
    success_url = reverse_lazy('imagen_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('imagen_list')
        context['action'] = 'add'

        return context


class ImagenUpdateView(UpdateView):
    model = Imagen
    form_class = ImagenForm
    template_name = 'imagen/create.html'
    success_url = reverse_lazy('imagen_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('imagen_list')
        context['action'] = 'edit'
        return context


class ImagenDeleteView(DeleteView):
    model = Imagen
    template_name = 'imagen/delete.html'
    success_url = reverse_lazy('imagen_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('imagen_list')
        return context


class InstalacionListView(ListView):
    model = Instalacion
    template_name = 'instalacion/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Instalacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('instalacion_create')
        context['list_url'] = reverse_lazy('instalacion_list')
        context['entity'] = 'Categorías'
        return context


class InstalacionCreateView(CreateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'instalacion/create.html'
    success_url = reverse_lazy('instalacion_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('instalacion_list')
        context['action'] = 'add'
        return context


class InstalacionUpdateView(UpdateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'instalacion/create.html'
    success_url = reverse_lazy('instalacion_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar categorías'
        context['entity'] = 'Instalaciones'
        context['list_url'] = reverse_lazy('instalacion_list')
        context['action'] = 'edit'
        return context


class InstalacionDeleteView(DeleteView):
    model = Instalacion
    template_name = 'instalacion/delete.html'
    success_url = reverse_lazy('instalacion_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('instalacion_list')
        return context
