from django.db import migrations
from core.models import CritEvaluacion, ResAprendizaje, Modulo
from core.migrations.core_migracion_inicial import core
from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD

#UD9.3.b BEGIN
def programacion_didactica(apps, schema_editor):
    #UNIDADES
    unidad1 = Unidad.objects.create(codigo="UT1", nombre="ARQUITECTURAS Y TECNOLOGÍAS WEB")
    unidad2 = Unidad.objects.create(codigo="UT2", nombre="FUNDAMENTOS DE PROGRAMACIÓN WEB")
    unidad3 = Unidad.objects.create(codigo="UT3", nombre="PORTFOLIO ESTRUCTURAS DE CONTROL")
    unidad4 = Unidad.objects.create(codigo="UT4", nombre="PORTFOLIO ESTRUCTURAS DE DATOS Y FORMULARIOS")
    unidad5 = Unidad.objects.create(codigo="UT5", nombre="PORTFOLIO ACCESO A DATOS Y OBJETOS DEL NAVEGADOR")
    unidad6 = Unidad.objects.create(codigo="UT6", nombre="MULTICAPA DATOS Y MODELO DE OBJETOS DEL DOCUMENTO (DOM)")
    unidad7 = Unidad.objects.create(codigo="UT7", nombre="MULTICAPA VISTAS Y CONTROLADORES, EVENTOS E INTERACTIVIDAD ")
    unidad8 = Unidad.objects.create(codigo="UT8", nombre="MULTICAPA AUTENTIFICACIÓN Y SEGURIDAD")
    unidad9 = Unidad.objects.create(codigo="UT9", nombre="SERVICIOS WEB INTRODUCCIÓN Y CONSUMO")
    unidad10 = Unidad.objects.create(codigo="UT10", nombre="SERVICIOS WEB Y APLICACIONES WEB REACTIVAS")
    unidad11 = Unidad.objects.create(codigo="UT11", nombre="SERVICIOS WEB AUTENTIFICACIÓN Y SEGURIDAD ")
    unidad12 = Unidad.objects.create(codigo="UT12", nombre="APLICACIONES WEB HÍBRIDAS")

    #INSTRUMENTOS DE EVALUACIÓN
    InstEvaluacion.objects.create(codigo="I1", nombre="Cuestionarios", descripcion="Realización de cuestionarios sobre los contenidos conceptuales de una unidad didáctica.")  
    InstEvaluacion.objects.create(codigo="I2", nombre="Defensa de proyecto", descripcion="Mediante sesiones de evaluación orales y sumarizadoras, el alumnado podrá defender oralmente las tareas realizadas, y responder a preguntas conceptuales concretas. Servirán como doble validación de las actividades realizadas.")  
    InstEvaluacion.objects.create(codigo="I3", nombre="Realización de proyectos", descripcion="Serán los conjuntos de tareas vertebradoras en las que el alumnado desarrollará los conceptos y destrezas a adquirir, en forma de producto final.")  
    InstEvaluacion.objects.create(codigo="I4", nombre="Actividades de profundización", descripcion="Se trata de actividades opcionales, que extenderán determinados aspectos tratados durante la realización de las tareas de proyecto.")  
    InstEvaluacion.objects.create(codigo="I5", nombre="Pruebas objetivas de verificación", descripcion="Se trata de pruebas prácticas, a realizar en el aula, con un tiempo acotado. Se utilizarán para verificar que se han alcanzado los objetivos, con especial atención a los especificados como fundamentales. Se pueden llevar a cabo con los recursos proporcionados por el profesorado y las actividades realizadas previamente por el alumnado. La no superación de alguno de los objetivos de estas pruebas implica la recuperación de las actividades correspondientes. Normalmente se realizará tras finalizar un bloque de unidades.")  
    InstEvaluacion.objects.create(codigo="I6", nombre="Participación en debates y foros", descripcion="Ya sea de forma presencial o mediante la plataforma digital del centro, se valorará la participación en debates, intercambio de ideas, así como propuestas de mejora y de nuevas tecnologías.")  
    InstEvaluacion.objects.create(codigo="I7", nombre="Cumplimiento de los plazos de entrega", descripcion="Se entenderá que el alumnado cumple los plazos de entrega si no se producen retrasos en la fechas de entrega establecidas, exceptuando los casos que puedan ser justificados.")      

    #PONDERACIÓN DE RA
    ra0613_1 = ResAprendizaje.objects.get(codigo="0613.1")
    ra0613_2 = ResAprendizaje.objects.get(codigo="0613.2")
    ra0613_3 = ResAprendizaje.objects.get(codigo="0613.3")
    ra0613_4 = ResAprendizaje.objects.get(codigo="0613.4")
    ra0613_5 = ResAprendizaje.objects.get(codigo="0613.5")
    ra0613_6 = ResAprendizaje.objects.get(codigo="0613.6")
    ra0613_7 = ResAprendizaje.objects.get(codigo="0613.7")
    ra0613_8 = ResAprendizaje.objects.get(codigo="0613.8")
    ra0613_9 = ResAprendizaje.objects.get(codigo="0613.9")
    PondRA.objects.create(resultado_aprendizaje = ra0613_1, porcentaje=2.5)
    PondRA.objects.create(resultado_aprendizaje = ra0613_2, porcentaje=2.5)
    PondRA.objects.create(resultado_aprendizaje = ra0613_3, porcentaje=10)
    PondRA.objects.create(resultado_aprendizaje = ra0613_4, porcentaje=20)
    PondRA.objects.create(resultado_aprendizaje = ra0613_5, porcentaje=15)
    PondRA.objects.create(resultado_aprendizaje = ra0613_6, porcentaje=15)
    PondRA.objects.create(resultado_aprendizaje = ra0613_7, porcentaje=25)
    PondRA.objects.create(resultado_aprendizaje = ra0613_8, porcentaje=5)
    PondRA.objects.create(resultado_aprendizaje = ra0613_9, porcentaje=5)

    #PONDERACIÓN DE CRITERIOS DE EVALUACIÓN
    #RA 1
    ce_ra06131_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="a")
    ce_ra06131_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="b")
    ce_ra06131_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="c")
    ce_ra06131_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="d")
    ce_ra06131_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="e")
    ce_ra06131_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="f")
    ce_ra06131_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="g")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_1, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_2, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_3, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_4, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_5, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_6, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06131_7, porcentaje=14.3)

    #RA 2
    ce_ra06132_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="a")
    ce_ra06132_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="b")
    ce_ra06132_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="c")
    ce_ra06132_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="d")
    ce_ra06132_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="e")
    ce_ra06132_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="f")
    ce_ra06132_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="g")
    ce_ra06132_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="h")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_1, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_2, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_3, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_4, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_5, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_6, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_7, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06132_8, porcentaje=12.5)

    #RA 3
    ce_ra06133_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="a")
    ce_ra06133_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="b")
    ce_ra06133_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="c")
    ce_ra06133_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="d")
    ce_ra06133_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="e")
    ce_ra06133_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="f")
    ce_ra06133_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="g")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_1, porcentaje=10)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_2, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_3, porcentaje=30)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_4, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_5, porcentaje=30)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_6, porcentaje=15)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06133_7, porcentaje=5)

    #RA 4
    ce_ra06134_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="a")
    ce_ra06134_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="b")
    ce_ra06134_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="c")
    ce_ra06134_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="d")
    ce_ra06134_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="e")
    ce_ra06134_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="f")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_1, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_2, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_3, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_4, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_5, porcentaje=55)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06134_6, porcentaje=25)

    #RA 5
    ce_ra06135_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="a")
    ce_ra06135_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="b")
    ce_ra06135_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="c")
    ce_ra06135_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="d")
    ce_ra06135_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="e")
    ce_ra06135_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="f")
    ce_ra06135_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="g")
    ce_ra06135_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="h")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_1, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_2, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_3, porcentaje=10)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_4, porcentaje=30)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_5, porcentaje=10)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_6, porcentaje=35)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_7, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06135_8, porcentaje=5)

    #RA 6
    ce_ra06136_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="a")
    ce_ra06136_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="b")
    ce_ra06136_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="c")
    ce_ra06136_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="d")
    ce_ra06136_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="e")
    ce_ra06136_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="f")
    ce_ra06136_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="g")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_1, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_2, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_3, porcentaje=30)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_4, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_5, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_6, porcentaje=30)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06136_7, porcentaje=5)

    #RA 7
    ce_ra06137_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="a")
    ce_ra06137_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="b")
    ce_ra06137_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="c")
    ce_ra06137_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="d")
    ce_ra06137_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="e")
    ce_ra06137_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="f")
    ce_ra06137_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="g")
    ce_ra06137_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="h")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_1, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_2, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_3, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_4, porcentaje=2.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_5, porcentaje=75)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_6, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_7, porcentaje=5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06137_8, porcentaje=5)

    #RA 8
    ce_ra06138_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="a")
    ce_ra06138_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="b")
    ce_ra06138_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="c")
    ce_ra06138_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="d")
    ce_ra06138_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="e")
    ce_ra06138_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="f")
    ce_ra06138_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="g")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_1, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_2, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_3, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_4, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_5, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_6, porcentaje=14.3)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06138_7, porcentaje=14.3)

    #RA 9
    ce_ra06139_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="a")
    ce_ra06139_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="b")
    ce_ra06139_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="c")
    ce_ra06139_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="d")
    ce_ra06139_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="e")
    ce_ra06139_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="f")
    ce_ra06139_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="g")
    ce_ra06139_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="h")
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_1, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_2, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_3, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_4, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_5, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_6, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_7, porcentaje=12.5)
    PondCriterio.objects.create(criterio_evaluacion=ce_ra06139_8, porcentaje=12.2)

    #PONDERACIÓN DE CRITERIOS DE EVALUACIÓN POR UNIDAD
    #RA 1
    ce_ra06131_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="a")
    ce_ra06131_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="b")
    ce_ra06131_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="c")
    ce_ra06131_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="d")
    ce_ra06131_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="e")
    ce_ra06131_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="f")
    ce_ra06131_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_1, codigo="g")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_1, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_2, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_3, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_4, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_5, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_6, unidad=unidad1, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06131_7, unidad=unidad1, porcentaje=14.3)
    #RA 2
    ce_ra06132_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="a")
    ce_ra06132_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="b")
    ce_ra06132_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="c")
    ce_ra06132_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="d")
    ce_ra06132_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="e")
    ce_ra06132_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="f")
    ce_ra06132_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="g")
    ce_ra06132_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_2, codigo="h")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_1, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_2, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_3, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_4, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_5, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_6, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_7, unidad=unidad2, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06132_8, unidad=unidad2, porcentaje=12.5)
    #RA 3
    ce_ra06133_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="a")
    ce_ra06133_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="b")
    ce_ra06133_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="c")
    ce_ra06133_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="d")
    ce_ra06133_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="e")
    ce_ra06133_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="f")
    ce_ra06133_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_3, codigo="g")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_1, unidad=unidad3, porcentaje=10)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_2, unidad=unidad3, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_3, unidad=unidad3, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_4, unidad=unidad3, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_5, unidad=unidad4, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_6, unidad=unidad4, porcentaje=15)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06133_7, unidad=unidad3, porcentaje=5)
    #RA 4
    ce_ra06134_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="a")
    ce_ra06134_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="b")
    ce_ra06134_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="c")
    ce_ra06134_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="d")
    ce_ra06134_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="e")
    ce_ra06134_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_4, codigo="f")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_1, unidad=unidad4, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_2, unidad=unidad4, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_3, unidad=unidad4, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_4, unidad=unidad8, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_4, unidad=unidad11, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_5, unidad=unidad8, porcentaje=55)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_5, unidad=unidad11, porcentaje=55)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06134_6, unidad=unidad12, porcentaje=25)
    #RA 5
    ce_ra06135_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="a")
    ce_ra06135_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="b")
    ce_ra06135_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="c")
    ce_ra06135_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="d")
    ce_ra06135_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="e")
    ce_ra06135_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="f")
    ce_ra06135_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="g")
    ce_ra06135_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_5, codigo="h")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_1, unidad=unidad6, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_2, unidad=unidad6, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_3, unidad=unidad7, porcentaje=10)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_4, unidad=unidad7, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_5, unidad=unidad6, porcentaje=10)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_5, unidad=unidad9, porcentaje=10)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_6, unidad=unidad6, porcentaje=35)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_7, unidad=unidad6, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_8, unidad=unidad6, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06135_8, unidad=unidad7, porcentaje=5)
    #RA 6
    ce_ra06136_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="a")
    ce_ra06136_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="b")
    ce_ra06136_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="c")
    ce_ra06136_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="d")
    ce_ra06136_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="e")
    ce_ra06136_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="f")
    ce_ra06136_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_6, codigo="g")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_1, unidad=unidad5, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_1, unidad=unidad6, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_2, unidad=unidad5, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_2, unidad=unidad6, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_2, unidad=unidad9, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_3, unidad=unidad5, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_3, unidad=unidad6, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_4, unidad=unidad5, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_4, unidad=unidad6, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_5, unidad=unidad5, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_5, unidad=unidad6, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_6, unidad=unidad5, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_6, unidad=unidad7, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_6, unidad=unidad9, porcentaje=30)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_7, unidad=unidad5, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06136_7, unidad=unidad9, porcentaje=5)
    #RA 7
    ce_ra06137_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="a")
    ce_ra06137_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="b")
    ce_ra06137_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="c")
    ce_ra06137_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="d")
    ce_ra06137_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="e")
    ce_ra06137_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="f")
    ce_ra06137_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="g")
    ce_ra06137_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_7, codigo="h")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_1,unidad=unidad10, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_2,unidad=unidad10, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_3,unidad=unidad10, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_4,unidad=unidad10, porcentaje=2.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_5,unidad=unidad10, porcentaje=75)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_6,unidad=unidad10, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_7,unidad=unidad11, porcentaje=5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06137_8,unidad=unidad10, porcentaje=5)
    #RA 8
    ce_ra06138_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="a")
    ce_ra06138_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="b")
    ce_ra06138_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="c")
    ce_ra06138_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="d")
    ce_ra06138_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="e")
    ce_ra06138_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="f")
    ce_ra06138_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_8, codigo="g")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_1, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_2, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_3, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_4, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_5, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_6, unidad=unidad7, porcentaje=14.3)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06138_7, unidad=unidad7, porcentaje=14.3)
    #RA 9
    ce_ra06139_1 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="a")
    ce_ra06139_2 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="b")
    ce_ra06139_3 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="c")
    ce_ra06139_4 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="d")
    ce_ra06139_5 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="e")
    ce_ra06139_6 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="f")
    ce_ra06139_7 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="g")
    ce_ra06139_8 = CritEvaluacion.objects.get(resultado_aprendizaje=ra0613_9, codigo="h")
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_1, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_2, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_3, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_4, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_5, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_5, unidad=unidad8, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_6, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_7, unidad=unidad12, porcentaje=12.5)
    PondCritUD.objects.create(criterio_evaluacion=ce_ra06139_8, unidad=unidad12, porcentaje=12.2)


class Migration(migrations.Migration):

    dependencies = [
        ('programacion_didactica', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(programacion_didactica),
    ]
#UD9.3.b END