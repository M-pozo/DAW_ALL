from core.models import Modulo, CritEvaluacion, ResAprendizaje
from programacion_didactica.models import InstEvaluacion, PondCritUD, PondCriterio, PondRA, Unidad

#UD6.6 BEGIN
#1--
def get_modulos_all():
    return Modulo.objects.all()

#2--
def get_ie_3():
    return InstEvaluacion.objects.all()[:3]

#3--
def get_crit_min():
    return CritEvaluacion.objects.filter(minimo=True)

#4--
def get_ra_not_0612():
    return ResAprendizaje.objects.exclude(codigo__startswith='0612')
#5--
def get_ie_I1_defensa():
    return InstEvaluacion.objects.filter(codigo='I1', nombre__contains='defensa')

#6--
def get_mod_id_lt_2_cod_des():
    return Modulo.objects.filter(id__lt=2).order_by('-codigo')

#7--
def get_mod_id_gt_2():
    return Modulo.objects.filter(id__gt=2)

#8--
def get_mod_des_nom_des():
    return Modulo.objects.filter(nombre__contains='desarrollo').order_by('nombre')

#9--
def get_ra_not_RA1():
    return ResAprendizaje.objects.exclude(codigo__endswith='1')

#10--
def get_ra_cli_RA3():
    return ResAprendizaje.objects.get(modulo__nombre__contains='cliente', codigo__endswith='3')

#11--
def get_ce_RA06_not_cli():
    return CritEvaluacion.objects.filter(resultado_aprendizaje__codigo__contains='06').exclude(resultado_aprendizaje__modulo__nombre__icontains='cliente')

#12--
def get_pon_ra_gt_5():
    return PondRA.objects.filter(porcentaje__gte=5)

#13--
def get_ce_5_10_RA1():
    return PondRA.objects.filter(porcentaje__range=(5, 10), resultado_aprendizaje__codigo__endswith='1', resultado_aprendizaje__modulo__codigo='0613')

#14--
def create_ie12():
    InstEvaluacion.objects.create(codigo='I12', nombre='Nuevo instrumento 12', descripcion='Nuevo instrumento 12')

#15 error
def create_ud15_pon():
        PondRA.objects.create(criterio_evaluacion=CritEvaluacion.objects.create(codigo='0633.3', descripcion='Prueba'), unidad=Unidad.objects.create(codigo='UT33', nombre='Prueba'), porcentaje=20)

#UD6.6 END

