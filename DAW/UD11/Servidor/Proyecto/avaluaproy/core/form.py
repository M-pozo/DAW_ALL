from django import forms
from .models import Modulo, ResAprendizaje, CritEvaluacion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, ButtonHolder, Submit, HTML, Row

#UD7.3.a/UD7.3.b/UD7.5.c/UD7.5.d BEGIN
class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['codigo', 'nombre']

    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-3"),
                Div(Field('nombre'), css_class="col-9"),
                css_class="row"
            ),
        )

class ResAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ResAprendizaje
        fields = ['modulo', 'codigo', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(ResAprendizajeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-3"),
                Div(Field('modulo'), css_class="col-9"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('descripcion'),
            ),
        )

class CritEvaluacionForm(forms.ModelForm):
    class Meta:
        model = CritEvaluacion
        fields = ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']

    def __init__(self, *args, **kwargs):
        super(CritEvaluacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>

        self.helper.layout = Layout(
            Div(
                Field('resultado_aprendizaje'),
            ),
            Div(
                Div(Field('minimo'), css_class="col-3"),
                Div(Field('codigo'), css_class="col-9"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('descripcion'), 
            ),
        )

#UD7.3.a/UD7.3.b/UD7.5.c/UD7.5.d END