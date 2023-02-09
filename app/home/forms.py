from django.forms import *

from .models import *


class ReservacionRestForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instalacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Restaurante
        fields = '__all__'
        widgets = {
            'num_movil': IntegerField(
                attrs={
                    'placeholder': 'Número del móvil',
                    'mensaje': TextInput(
                        attrs={
                            'placeholder': 'Datos extras...'
                        }
                    )
                }
            )
        }
