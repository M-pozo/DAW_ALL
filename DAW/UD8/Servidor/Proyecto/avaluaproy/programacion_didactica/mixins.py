from .models import PondRA, PondCriterio, PondCritUD
from django.db.models import Sum
from django.contrib import messages

#UD7.2.g, UD7.2.h, UD7.2.i BEGIN
"""class PonderacionRAMixin():
    def form_valid(self, form):
        porcentaje_total = PondRA.objects.exclude(self.get_object().pk).aggregate(Sum('porcentaje'))
        #print(porcentaje_total)
        if porcentaje_total['porcentaje__sum'] > 100:
            messages.error(self.request, "La suma de porcentaje esta por encima de 100")
            return self.form_invalid(form)
        return super().form_valid(form)"""
#UD7.2.g, UD7.2.h, UD7.2.i END

