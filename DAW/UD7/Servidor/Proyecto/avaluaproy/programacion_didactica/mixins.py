from .models import PondRA, PondCriterio, PondCritUD
from django.core.exceptions import ValidationError
from django.db.models import Sum

#UD7.2.g, UD7.2.h, UD7.2.i BEGIN
class PonderacionRAMixin():
    model = PondRA
    def validar_porcentaje():
            porcentaje_total = 101
            if porcentaje_total > 100:
                raise ValidationError("La suma de porcentaje esta por encima de 100")
            return porcentaje_total
#UD7.2.g, UD7.2.h, UD7.2.i END