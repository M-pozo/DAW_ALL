from django.db import migrations
from core.models import Modulo, ResAprendizaje, CritEvaluacion

#UD9.3.a BEGIN
def core(apps, schema_editor):
    modulo_servidor = Modulo.objects.create(codigo="0613",nombre="Desarrollo en entorno servidor")

    #RESULTADO DE APRENDIZAJE 0613.1
    ra0613_1 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.1", descripcion="Selecciona las arquitecturas y tecnologías de programación web en entorno servidor, analizando sus capacidades y características propias.")
    
    ce_ra06131_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="a", descripcion="Se han caracterizado y diferenciado los modelos de ejecución de código en el servidor y en el cliente web.", minimo=False)
    ce_ra06131_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="b", descripcion="Se han reconocido las ventajas que proporciona la generación dinámica de páginas.", minimo=False)
    ce_ra06131_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="c", descripcion="Se han identificado los mecanismos de ejecución de código en los servidores web.", minimo=False)
    ce_ra06131_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="d", descripcion="Se han reconocido las funcionalidades que aportan los servidores de aplicaciones y su integración con los servidores web.", minimo=False)
    ce_ra06131_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="e", descripcion="Se han identificado y caracterizado los principales lenguajes y tecnologías relacionados con la programación web en entorno servidor.", minimo=False)
    ce_ra06131_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="f", descripcion="Se han verificado los mecanismos de integración de los lenguajes de marcas con los lenguajes de programación en entorno servidor.", minimo=False)
    ce_ra06131_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_1, codigo="g", descripcion="Se han reconocido y evaluado las herramientas y frameworks de programación en entorno servidor.", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.2
    ra0613_2 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.2", descripcion="Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.")
    
    ce_ra06132_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="a", descripcion="Se han reconocido los mecanismos de generación de páginas web a partir de lenguajes de marcas con código embebido.", minimo=False) 
    ce_ra06132_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="b", descripcion="Se han identificado las principales tecnologías asociadas.", minimo=False) 
    ce_ra06132_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="c", descripcion="Se han utilizado etiquetas para la inclusión de código en el lenguaje de marcas.", minimo=False) 
    ce_ra06132_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="d", descripcion="Se ha reconocido la sintaxis del lenguaje de programación que se ha de utilizar.", minimo=False) 
    ce_ra06132_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="e", descripcion="Se han escrito sentencias simples y se han comprobado sus efectos en el documento resultante.", minimo=False) 
    ce_ra06132_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="f", descripcion="Se han utilizado directivas para modificar el comportamiento predeterminado.", minimo=False) 
    ce_ra06132_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="g", descripcion="Se han utilizado los distintos tipos de variables y operadores disponibles en el lenguaje.", minimo=False) 
    ce_ra06132_8 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_2, codigo="h", descripcion="Se han identificado los ámbitos de utilización de las variables.", minimo=False) 

    #RESULTADO DE APRENDIZAJE 0613.3
    ra0613_3 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.3", descripcion="Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.")
    
    ce_ra06133_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="a", descripcion="Se han utilizado mecanismos de decisión en la creación de bloques de sentencias.", minimo=False)  
    ce_ra06133_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="b", descripcion="Se han utilizado bucles y se ha verificado su funcionamiento.", minimo=False)  
    ce_ra06133_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="c", descripcion="Se han utilizado matrices (array) para almacenar y recuperar conjuntos de datos.", minimo=False)  
    ce_ra06133_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="d", descripcion="Se han creado y utilizado funciones.", minimo=False)  
    ce_ra06133_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="e", descripcion="Se han utilizado formularios web para interactuar con el usuario del navegador web.", minimo=False)  
    ce_ra06133_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="f", descripcion="Se han empleado métodos para recuperar la información introducida en el formulario.", minimo=False)  
    ce_ra06133_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_3, codigo="g", descripcion="Se han añadido comentarios al código.", minimo=False) 

    #RESULTADO DE APRENDIZAJE 0613.4
    ra0613_4 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.4", descripcion="Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.")
    
    ce_ra06134_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="a", descripcion="Se han identificado los mecanismos disponibles para el mantenimiento de la información que concierne a un cliente web concreto y se han señalado sus ventajas.", minimo=False)
    ce_ra06134_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="b", descripcion="Se han utilizado mecanismos para mantener el estado de las aplicaciones web.", minimo=False)
    ce_ra06134_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="c", descripcion="Se han utilizado mecanismos para almacenar información en el cliente web y para recuperar su contenido.", minimo=False)
    ce_ra06134_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="d", descripcion="Se han identificado y caracterizado los mecanismos disponibles para la autentificación de usuarios.", minimo=False)
    ce_ra06134_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="e", descripcion="Se han escrito aplicaciones que integren mecanismos de autentificación de usuarios.", minimo=False)
    ce_ra06134_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_4, codigo="f", descripcion="Se han utilizado herramientas y entornos para facilitar la programación, prueba y depuración del código.", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.5
    ra0613_5 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.5", descripcion="Desarrolla aplicaciones web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio.")
    
    ce_ra06135_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="a", descripcion="Se han identificado las ventajas de separar la lógica de negocio de los aspectos de presentación de la aplicación.", minimo=False)  
    ce_ra06135_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="b", descripcion="Se han analizado y utilizado mecanismos y frameworks que permiten realizar esta separación y sus características principales.", minimo=False)  
    ce_ra06135_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="c", descripcion="Se han utilizado objetos y controles en el servidor para generar el aspecto visual de la aplicación web en el cliente.", minimo=False)  
    ce_ra06135_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="d", descripcion="Se han utilizado formularios generados de forma dinámica para responder a los eventos de la aplicación web.", minimo=False)  
    ce_ra06135_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="e", descripcion="Se han identificado y aplicado los parámetros relativos a la configuración de la aplicación web.", minimo=False)  
    ce_ra06135_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="f", descripcion="Se han escrito aplicaciones web con mantenimiento de estado y separación de la lógica de negocio.", minimo=False)  
    ce_ra06135_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="g", descripcion="Se han aplicado los principios y patrones de diseño de la programación orientada a objetos.", minimo=False)  
    ce_ra06135_8 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_5, codigo="h", descripcion="Se ha probado y documentado el código.", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.6
    ra0613_6 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.6", descripcion="Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información.")
    
    ce_ra06136_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="a", descripcion="Se han analizado las tecnologías que permiten el acceso mediante programación a la información disponible en almacenes de datos.", minimo=False)
    ce_ra06136_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="b", descripcion="Se han creado aplicaciones que establezcan conexiones con bases de datos.", minimo=False)
    ce_ra06136_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="c", descripcion="Se ha recuperado información almacenada en bases de datos.", minimo=False)
    ce_ra06136_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="d", descripcion="Se ha publicado en aplicaciones web la información recuperada.", minimo=False)
    ce_ra06136_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="e", descripcion="Se han utilizado conjuntos de datos para almacenar la información.", minimo=False)
    ce_ra06136_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="f", descripcion="Se han creado aplicaciones web que permitan la actualización y la eliminación de información disponible en una base de datos.", minimo=False)
    ce_ra06136_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_6, codigo="g", descripcion="Se han probado y documentado las aplicaciones web.", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.7
    ra0613_7 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.7", descripcion="Desarrolla servicios web reutilizables y accesibles mediante protocolos web, verificando su funcionamiento.")
    
    ce_ra06137_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="a", descripcion="Se han reconocido las características propias y el ámbito de aplicación de los servicios web.", minimo=False)
    ce_ra06137_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="b", descripcion="Se han reconocido las ventajas de utilizar servicios web para proporcionar acceso a funcionalidades incorporadas a la lógica de negocio de una aplicación.", minimo=False)
    ce_ra06137_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="c", descripcion="Se han identificado las tecnologías y los protocolos implicados en el consumo de servicios web.", minimo=False)
    ce_ra06137_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="d", descripcion="Se han utilizado los estándares y arquitecturas más difundidos e implicados en el desarrollo de servicios web.", minimo=False)
    ce_ra06137_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="e", descripcion="Se ha programado un servicio web.", minimo=False)
    ce_ra06137_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="f", descripcion="Se ha verificado el funcionamiento del servicio web.", minimo=False)
    ce_ra06137_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="g", descripcion="Se ha consumido el servicio web.", minimo=False)
    ce_ra06137_8 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_7, codigo="h", descripcion="Se ha documentado un servicio web.", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.8
    ra0613_8 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.8", descripcion="Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.")
    
    ce_ra06138_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="a", descripcion="Se han identificado las diferencias entre la ejecución de código en el servidor y en el cliente web.", minimo=False)  
    ce_ra06138_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="b", descripcion="Se han reconocido las ventajas de unir ambas tecnologías en el proceso de desarrollo de programas.", minimo=False)  
    ce_ra06138_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="c", descripcion="Se han identificado las tecnologías y frameworks relacionadas con la generación por parte del servidor de páginas web con guiones embebidos.", minimo=False)  
    ce_ra06138_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="d", descripcion="Se han utilizado estas tecnologías y frameworks para generar páginas web que incluyan interacción con el usuario.", minimo=False)  
    ce_ra06138_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="e", descripcion="Se han utilizado estas tecnologías y frameworks, para generar páginas web que incluyan verificación de formularios.", minimo=False)  
    ce_ra06138_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="f", descripcion="Se han utilizado estas tecnologías y frameworks para generar páginas web que incluyan modificación dinámica de su contenido y su estructura.", minimo=False)  
    ce_ra06138_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_8, codigo="g", descripcion="Se han aplicado estas tecnologías y frameworks en la programación de aplicaciones web", minimo=False)

    #RESULTADO DE APRENDIZAJE 0613.9
    ra0613_9 = ResAprendizaje.objects.create(modulo=modulo_servidor, codigo="0613.9", descripcion="Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información")
    
    ce_ra06139_1 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="a", descripcion="Se han reconocido las ventajas que proporciona la reutilización de código y el aprovechamiento de información ya existente.", minimo=False)
    ce_ra06139_2 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="b", descripcion="Se han identificado tecnologías y frameworks aplicables en la creación de aplicaciones web híbridas.", minimo=False)
    ce_ra06139_3 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="c", descripcion="Se ha creado una aplicación web que recupere y procese repositorios de información ya existentes.", minimo=False)
    ce_ra06139_4 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="d", descripcion="Se han creado repositorios específicos a partir de información existente en almacenes de información.", minimo=False)
    ce_ra06139_5 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="e", descripcion="Se han utilizado librerías de código y frameworks para incorporar funcionalidades específicas a una aplicación web.", minimo=False)
    ce_ra06139_6 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="f", descripcion="Se han programado servicios y aplicaciones web utilizando como base información y código generados por terceros.", minimo=False)
    ce_ra06139_7 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="g", descripcion="Se han analizado y utilizado librerías de código relacionadas con Big Data e inteligencia de negocios, para incorporar análisis e inteligencia de datos proveniente de repositorios.", minimo=False)
    ce_ra06139_8 = CritEvaluacion.objects.create(resultado_aprendizaje=ra0613_9, codigo="h", descripcion="Se han probado, depurado y documentado las aplicaciones generadas.", minimo=False)

    return {
        "ra0613_1":ra0613_1,
    }
class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial')
    ]

    operations = [
        migrations.RunPython(core),
    ]
#UD9.3.a END