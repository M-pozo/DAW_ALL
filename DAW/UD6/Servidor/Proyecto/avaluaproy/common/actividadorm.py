from core.models import Modulo, CritEvaluacion, ResAprendizaje
from programacion_didactica.models import InstEvaluacion

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
    return ResAprendizaje.objects.filter(codigo__istartswith="0612")

#5
def get_ie_I1_defensa():
    return Modulo.objects.all()

#6
def get_mod_id_lt_2_cod_des():
    return Modulo.objects.all()

#7
def get_mod_id_gt_2():
    return Modulo.objects.all()

#8
def get_mod_des_nom_des():
    return Modulo.objects.all()

#9
def get_ra_not_RA1():
    return Modulo.objects.all()

#10
def get_ra_cli_RA3():
    return Modulo.objects.all()

#11
def get_ce_RA06_not_cli():
    return Modulo.objects.all()

#12
def get_pon_ra_gt_5():
    return Modulo.objects.all()

#13
def get_ce_5_10_RA1():
    return Modulo.objects.all()

#14
def create_ie12():
    return Modulo.objects.all()

#15
def create_ud15_pon():
    return Modulo.objects.all()

#16
def update_last_ud():
    return Modulo.objects.all()

#17
def update_ce_RA2_x2():
    return Modulo.objects.all()

#18
def update_pon_ce_RA1_div2():
    return Modulo.objects.all()

#19
def delete_pon_ce_lt_5():
    return Modulo.objects.all()

#20
def delete_pon_ce_UD15():
    return Modulo.objects.all()
#UD6.6 END

