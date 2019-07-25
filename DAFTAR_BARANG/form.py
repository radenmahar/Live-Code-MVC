from django import forms
from .models import DaftarBarang

class InputBarang(forms.ModelForm):

    class Meta:
        model = DaftarBarang
        fields = ('picture', 'nama', 'moto', 'harga')