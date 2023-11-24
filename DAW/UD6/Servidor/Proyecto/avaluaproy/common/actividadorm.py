from core.models import Modulo, CritEvaluacion, ResAprendizaje
from programacion_didactica.models import InstEvaluacion, PondCritUD, PondCriterio, PondRA, Unidad

#UD6.6 BEGIN
#1
def get_modulos_all():
    return Modulo.objects.all()

#2
def get_ie_3():
    return InstEvaluacion.objects.all()[:3]

#3
def get_crit_min():
    return CritEvaluacion.objects.filter(minimo=True)

#4
def get_ra_not_0612():
    return ResAprendizaje.objects.exclude(codigo__startswith='0612')
#5
def get_ie_I1_defensa():
    return InstEvaluacion.objects.filter(codigo='I1', nombre__icontains='defensa')

#6
def get_mod_id_lt_2_cod_des():
    return Modulo.objects.filter(id__lt=2).order_by('-codigo')

#7
def get_mod_id_gt_2():
    return Modulo.objects.filter(id__gt=2)

#8
def get_mod_des_nom_des():
    return Modulo.objects.filter(nombre__icontains='desarrollo').order_by('nombre')

#9
def get_ra_not_RA1():
    return ResAprendizaje.objects.exclude(codigo__endswith='1')

#10
def get_ra_cli_RA3():
    return ResAprendizaje.objects.get(modulo__icontains='cliente', codigo__endswith='3')

#11
def get_ce_RA06_not_cli():
    return CritEvaluacion.objects.filter(resultado_aprendizaje__codigo__contains='06').exclude(modulo__nombre__icontains='cliente')

#12
def get_pon_ra_gt_5():
    return PondRA.objects.filter(resultado_aprendizaje__porcentaje__gte=5)

#13
def get_ce_5_10_RA1():
    return PondRA.objects.filter(
        porcentaje__range=[5, 10],
        criterio_evaluacion__resultado_aprendizaje__codigo__endswith='1',
        criterio_evaluacion__resultado_aprendizaje__modulo__codigo='0613'
    )

#14
def create_ie12():
    return InstEvaluacion.objects.create(codigo='I12', nombre='Nuevo instrumento 12', descripcion='Nuevo instrumento 12')

#15
def create_ud15_pon():
    ud15 = Unidad.objects.create(nombre='UD15', datos='Datos de tu elección')
    ce = CritEvaluacion.objects.create(nombre='Criterio de evaluación de tu elección')
    return PondRA.objects.create(unidad=ud15, criterio_evaluacion=ce, porcentaje=20)

#16
def update_last_ud():
    last_ud = Unidad.objects.last()
    last_ud.nombre += " (última)"
    last_ud.save()

#17
def update_ce_RA2_x2():
    ce_list = CritEvaluacion.objects.filter(
        resultado_aprendizaje__codigo__endswith='2',
        resultado_aprendizaje__modulo__codigo='0613'
    )
    for ce in ce_list:
        ce.ponderacion *= 2
        ce.save()

#18
def update_pon_ce_RA1_div2():
    ce_list = CritEvaluacion.objects.filter(
        resultado_aprendizaje__codigo__endswith='1',
        resultado_aprendizaje__modulo__codigo='0613',
        ponderacion__par=True
    )
    for ce in ce_list:
        ce.ponderacion /= 2
        ce.save()

#19
def delete_pon_ce_lt_5():
    PondCriterio.objects.filter(porcentaje__lt=5).delete()

#20
def delete_pon_ce_UD15():
    unidad = Unidad.objects.get(nombre__icontains='UD3')
    PondCritUD.objects.filter(unidad=unidad).delete()
#UD6.6 END

