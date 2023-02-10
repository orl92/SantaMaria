from django.forms import *

from app.galeria.models import *


class InstalacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Instalacion
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

    def clean(self):
        cleand = super().clean()
        name = cleand['name']
        name = str(name).replace(' ', '')
        if name.isalpha():
            pass
        else:
            self.add_error('name', 'El nombre no puede contener números o caracteres especiales.')
        try:
            id = self.initial['id']
        except Exception:
            id = None
        for c in Instalacion.objects.all():
            if id == c.id:
                pass
            else:
                if name.upper() == c.name.upper():
                    self.add_error('name', ' Ya existe una categoría con ese nombre.')

        return cleand

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ImagenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].widget.attrs['autofocus'] = True

    class Meta:
        model = Imagen
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
