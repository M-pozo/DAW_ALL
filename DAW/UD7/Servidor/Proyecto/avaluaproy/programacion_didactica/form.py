from django import forms
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD

#UD7.3.a BEGIN
class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['codigo', 'nombre']

class InstEvaluacionForm(forms.ModelForm):
    class Meta:
        model = InstEvaluacion
        fields = ['codigo', 'nombre', 'descripcion']

class PondRAForm(forms.ModelForm):
    class Meta:
        model = PondRA
        fields = ['resultado_aprendizaje', 'porcentaje']
        
class PondCriterioForm(forms.ModelForm):
    class Meta:
        model = PondCriterio
        fields = ['criterio_evaluacion', 'unidad', 'porcentaje']
        
class PondCritUDForm(forms.ModelForm):
    class Meta:
        model = PondCritUD
        fields = ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']

#UD7.3.a END