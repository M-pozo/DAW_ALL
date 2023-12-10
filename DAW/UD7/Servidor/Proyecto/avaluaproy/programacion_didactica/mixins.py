from django.contrib.messages import constants as messages

#UD7.2.g, UD7.2.h, UD7.2.i BEGIN
class PonderacionRAMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los RAs en el módulo supera el 100%."
            messages.error(self.request, error_message)

class  PonderacionCEMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los CR's en el módulo supera el 100%."
            messages.error(self.request, error_message)

class  PonderacionCEUDMixin():
    def validacion(self):
        porcentaje_total = sum(self.porcentaje)
        if porcentaje_total > 100:
            error_message = "La suma de las ponderaciones de los CR's en el módulo supera el 100%."
            messages.error(self.request, error_message)
#UD7.2.g, UD7.2.h, UD7.2.i END