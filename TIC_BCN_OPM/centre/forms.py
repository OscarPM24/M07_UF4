from django.forms import ModelForm
from .models import Usuari

class UsuariForm(ModelForm):
    class Meta:
        model = Usuari # Model del usuari
        fields = '__all__' # Agafem tots els camps
