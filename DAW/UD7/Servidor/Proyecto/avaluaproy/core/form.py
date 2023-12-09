from django import forms
from .models import Modulo, ResAprendizaje, CritEvaluacion

#UD7.3.a BEIGN
class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['codigo', 'nombre']

class ResAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ResAprendizaje
        fields = ['modulo', 'codigo', 'descripcion']

class CritEvaluacionForm(forms.ModelForm):
    class Meta:
        model = CritEvaluacion
        fields = ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']

#UD7.3.a END