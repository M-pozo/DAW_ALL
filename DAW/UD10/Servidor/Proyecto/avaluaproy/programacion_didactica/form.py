from django import forms
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, ButtonHolder, Submit, HTML, Row
from django.contrib.messages import constants as messages

#UD7.3.a/UD7.3.b/UD7.5.c/UD7.5.d BEGIN
class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['codigo', 'nombre']
    
    def __init__(self, *args, **kwargs):
        super(UnidadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-2"),
                Div(Field('nombre'), css_class="col-10"),
                css_class="row"
            ),
        )

class InstEvaluacionForm(forms.ModelForm):
    class Meta:
        model = InstEvaluacion
        fields = ['codigo', 'nombre', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super(InstEvaluacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-2"),
                Div(Field('nombre'), css_class="col-10"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('descripcion'),
            ),
        )

class PondRAForm(forms.ModelForm):
    class Meta:
        model = PondRA
        fields = ['resultado_aprendizaje', 'porcentaje']
    
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if porcentaje  < 0 or porcentaje > 100:
            raise forms.ValidationError("El porcentaje debe estar entre 0 y 100.")
        return porcentaje
    
    def __init__(self, *args, **kwargs):
        super(PondRAForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('resultado_aprendizaje'), css_class="col-9"),
                Div(Field('porcentaje'), css_class="col-3"),
                css_class="row"
            ),
        )
        
class PondCriterioForm(forms.ModelForm):
    class Meta:
        model = PondCriterio
        fields = ['criterio_evaluacion', 'porcentaje']
    
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if porcentaje  < 0 or porcentaje > 100:
            raise forms.ValidationError("El porcentaje debe estar entre 0 y 100.")
        return porcentaje
    
    def __init__(self, *args, **kwargs):
        super(PondCriterioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('criterio_evaluacion'), css_class="col-9"),
                Div(Field('porcentaje'), css_class="col-3"),
                css_class="row"
            ),
        )
        
class PondCritUDForm(forms.ModelForm):
    class Meta:
        model = PondCritUD
        fields = ['criterio_evaluacion', 'unidad', 'porcentaje']
    
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if porcentaje  < 0 or porcentaje > 100:
            raise forms.ValidationError("El porcentaje debe estar entre 0 y 100.")
        return porcentaje
    
    def __init__(self, *args, **kwargs):
        super(PondCritUDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Field('unidad'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('criterio_evaluacion'), css_class="col-9"),
                Div(Field('porcentaje'), css_class="col-3"),
                css_class="row"
            ),
        )

#UD7.3.a/UD7.3.b/UD7.5.c/UD7.5.d END