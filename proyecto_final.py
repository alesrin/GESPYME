#LA CLASS PROYECTO ESTA TODAVIA A MEDIAS, MIRA LA CLASE TAREA
class Proyecto:#OJO

    #n = 1

    def __init__(self, nombre, *lista_tareas): #Crear proyectos: Decir el nombre de proyecto y al menos una tarea. ESTA A MEDIAS, LO DE DECIR AL MENOS 1 TAREA. DE MOMENTO PUEDES PONER CUALQUIER TEXTO Y TE LO ACEPTA.
        self.nombre = nombre
        self.lista_tareas = list(lista_tareas)

        #TODAVÍA NO FUNCIONA ESTA PARTE DEL CÓDIGO:
        #if len(self.lista_tareas) <1 :

            #print("Por favor, introduzca al menos una tarea a este proyecto\n")
            #Proyecto.agregar_tarea()
        #else:
           #pass

        self.id_proyecto = 1 #EL ID DEL PROYECTO DEBE AUMENTAR UNA UNIDAD CADA VEZ QUE SE CREA UN PROYECTO
        
        #para comprobar si está funcionando, descomenta esto:
        #print(f"El nombre del proyecto es: {self.nombre}")
        #print(f"Su lista de tareas es: {self.lista_tareas}"
 
    #TODAVÍA NO FUNCIONA ESTA PARTE DEL CÓDIGO:
    def agregar_tarea(self): #MÉTODO PARA AÑADIR TAREAS a un proyecto, las creas usando la clase Tareas
     #Te dice el ID del proyecto. SIN TERMINAR
     print (f"Esta taréa pertenece al proyecto con ID: {self.id_proyecto}")

     print("Introduce los datos de la nueva tarea:\n")

     #agregar_a_lista_de_tareas_existentes()

     """ nueva_tarea = "tarea"+n
     lista_auxiliar = [nueva_tarea]
     for n in lista_auxiliar:
        n = Prueba()

     n += 1

    
         
class Prueba:

    a = 1

    def pr(cls):
        print(f"Se ha creado la Prueba{cls.a}")
        cls.a += 1

proyecto0 = Proyecto("Nombre de proyecto","tarea cualquiera")
proyecto0.agregar_tarea()
tarea3.pr() """

class Tarea: # Las tareas son objetos que creamos dentro de cada proyecto.

    tareas_existentes = [] #Lista de todas las tareas que hemos creado con esta clase. ES UNA LISTA CUYOS ELEMENTOS SON OBJETOS

    #LOS VALORES POR DEFECTO SON NECESARIOS, SI NO LOS PONES TE DA ERROR.
    #Como lo tengo aquí hecho, puedes crear un objeto Tarea sin especificar sus atributos en la linea en la que lo creas [es decir, que no tienes que hacer:
    #Tarea(EF-234,"Hacer el catering",2,2024,04,...)]
    #Sin embargo, nada más crear el objeto Tarea, lo primero que te pide es que actualices los valores por defecto de sus atributos. (Es para lo que sirve el código especificado en def __init__)
    #Me parecia la forma más ordenada y facil de entender para este código.
    def __init__(self,id_tarea = 0,nombre_tarea =0,tiempo_estimado = 0,anio_0 = 0,mes_0 = 0,dia_0 = 0,anio_tope = 0,mes_tope = 0,dia_tope = 0,lista_trabajadores= []):
        
        self.id_tarea = str(input("Introduce el ID de la nueva tarea:")) #OJO,ES UN DATO A INTRODUCIR?, segun las tablas iniciales del proyecto en notion, es un valor autoincremental
        self.nombre_tarea = str(input("Introduce el nombre de la nueva tarea:")).capitalize() # hacemos que el input sea str y que autocorrija a la primera letra (que sea mayúscula) 
        self.tiempo_estimado = float(input("Introduce el tiempo estimado que lleva la tarea en horas:")) #ES FLOAT Y NO INT PARA QUE SE PUEDA DECIR 7,5 horas, por ejemplo
        
        #Las dos lineas de aquí abajo son necesarias para introducir la fecha de inicio, la explicación del metodo empleado está en este enlace: https://www.w3schools.com/python/python_datetime.asp
        import datetime
        self.fecha_de_inicio = datetime.datetime(int(input("Introduce el año de inicio de la tarea:")),int(input("Introduce el més de  inicio de la tarea EN NÚMERO:")),int(input("Introduce el dia de inicio de la tarea EN NÚMERO:")))

        self.fecha_limite = datetime.datetime(int(input("Introduce el año tope de fin de la tarea:")),int(input("Introduce el més  tope de fin de la tarea EN NÚMERO:")),int(input("Introduce el dia tope de inicio de la tarea EN NÚMERO:")))


        #He necesitado crear esta variable nueva, trabajadores_contratados. Es necesario saber que trabajadores tenemos contratados antes de decidir a donde los asignamos.Esto es un ejemplo, tenemos que conseguir que se haga esta lista automaticamente en el bloque de con el código que tiene hecho David.
        trabajadores_contratados =["Rafa","Juan", "Alejandra","Sandra","Lucia"]

        #ESTA EL CÓDIGO HECHO EN EL DOCUMENTO "TRABAJADORES_A_LA_TAREA" QUE TAMBIÉN HE AÑADIDO A LA CARPETA "GESPYME-Adrian". HE IMPORTADO EL CÓDIGO DE ESE ARCHIVO A ESTE CON ESTE COMANDO:
        import TRABAJADORES_A_LA_TAREA
        self.lista_trabajadores = TRABAJADORES_A_LA_TAREA.hacer_lista_de_trabajadores_asignados_a_la_tarea(trabajadores_contratados)
        #Con esta última linea le estoy diciendo que utilice la función "hacer_lista_de_trabajadores_asignados_a_la_tarea" que está en el archivo "TRABAJADORES_A_LA_TAREA". Y que guarde el resultado como self.lista_trabajadores

    """@classmethod
        def agregar_a_lista_de_tareas_existentes(cls):
         cls.tareas_existentes.append(Tarea())
         print("La lista de tareas existentes es:")
         print(cls.tareas_existentes)
         
        agregar_a_lista_de_tareas_existentes() """

    #Comando info_tarea te hace print de todos los atributos de la tarea
    #OJO,DE MOMENTO, SOLO HE HECHO QUE TE APARÉZCAN LAS VARIABLES PARA LAS QUE YA TENEMOS EL CÓDIGO HECHO, PERO MÁS ADELANTE TE DEBERÍA APARECER TODo.
    def info_tarea(self):
        print(f"\nEsta es toda la infromación de la tarea {self.nombre_tarea}:\n")
        print(f"-El id de la tarea es: {self.id_tarea}")
        print(f"-La duración estimada de la tarea es: {self.tiempo_estimado}")
        print(f"-La fecha de inicio de la tarea es: {self.fecha_de_inicio}")
        print(f"-La fecha tope de la tarea es: {self.fecha_limite}")
        print(f"-Los trabajadores asignados a esta tarea són:\n {self.lista_trabajadores}")
        print() #Un espacio para que no salga todo junto en la terminal


    #TODO LO QUE APARECE POR AQUÍ ABAJO YA SÓN IMPLEMENTACIONES FUTURAS.

    #Aquí abajo hay que hacer el código que te devuelva la fecha de fin a partir de la fecha de inicio y del tiempo estimado:
    fecha_de_fin = "05/12/2024" #ESTE DEBERÍA SER EL OUTPUT POR EJEMPLO
        
    # Código para calcular el coste de la tarea:

    #Esta lista de aquí abajo es un ejemplo del output que te debe dar mi código TRABAJADORES_A_LA_TAREA.   es una lista de los trabajadores que has asignado a la tarea que has creado con esta clase:
    lista_trabajadores = ["Rafa","Juan", "Alejandra"]
    coste_tarea = 0

    #Con este código Y SI YA TENEMOS CREADOS UNOS OBJETOS "Trabajador" CON TODOS SUS DATOS, ya deberíamos   poder calcular el coste de la tarea.
    #OJO, esta fórmula asume que todos los trabajadores dedican el mismo tiempo a una tarea. es decir, si   una tarea dura 16 horas, asume que todos los trabajadores que han sido asigandos a la tarea trabajan  16 horas completas
    #for trabajador in lista_trabajadores:
        #coste_tarea += trabajador.getAttribute(coste_hora_trabajador) * tiempo_estimado
        
    
    """ def asignar_trabajadores_a_tarea(self,trabajadores_contratados): 

 
        import TRABAJADORES_A_LA_TAREA
        TRABAJADORES_A_LA_TAREA.hacer_lista_de_trabajadores_asignados_a_la_tarea(trabajadores_contratados)
        
 """

    #Estado de tarea, inicialmente es False/ no terminada, implementar el código para que se pueda  modificar:
    #estado_tarea = False

    #if estado_tarea == False:
        #print("No terminada")
    #elif estado_tarea == True:
        #print("Terminada")
    #else:
        #print("La variable introducida para el estado de la tarea no es correcta, debería ser True o   False")
    
#Para comprobar si funciona la clase proyecto, descomenta y ejecuta la línea de código de abajo:          
#proyecto1 = Proyecto("proyecto cualquiera","Ver tiendas" ,"hacer compra", "labar perro")

#Creamos 2 tareas
tarea1 = Tarea() 
tarea2 = Tarea()

#Comprobamos si se han creado correctamente imprimiendo sus atributos con el método info_tarea()
tarea1.info_tarea()
tarea2.info_tarea()

tareas_existentes = [tarea1,tarea2]
print(tareas_existentes)

#OJO,OJO. AHORA EL SIGUIENTE PASO ES HACER QUE ESTO SE CONSIGA AUTOMÁTICAMENTE/CON UN MÉTODO DE LA CLASE PROYECTO:
""" nueva_tarea = input("introduzca el nombre de la nueva tarea")
nueva_tarea.split() #ESTA LINEA ELIMINA LOS ESPACIOS BLANCOS DEL NOMBRE DE LA NUEVA TAREA Y LOS REEMPLAZA POR COMAS, SI CONSIGUES QUE LO REEMPLACE POR _ O QUE SIMPLEMENTE LO ELIMINE YA ESTARÍA.
lista_auxiliar = [nueva_tarea]
for elemento in lista_auxiliar:
    elemento = Tarea()
    Tarea.tareas_existentes.append(elemento) #ESTA LINEA SE SUPONE QUE TIENE QUE HACER QUE SE AÑADA LA NUEVA TAREA CREADA A LA LISTA DE TAREAS EXISTENTES QUE APARECE EN LA CLASE TAREAS """

    
   







""" trabajadores = []

while True:
    print("Selecciona una de las siguientes opciones:\n")
    print("1 - Agregar trabajador\n")
    print("2 - Mostrar trabajadores\n")
    print("3 - Salir\n")
    
    opcion = int(input("Escribe el número vinculado a la opción que deseas: \n"))
    
    if opcion == 1:
        Proyecto.agregar_trabajador(trabajadores)
    elif opcion == 2:
        Proyecto.mostrar_trabajador(trabajadores)
    elif opcion == 3:
        break """
    








""" nombre_proyecto = input (str("Introduzca el nombre del proyecto: "))



# Que te pida las tareas de las que forma parte el proyecto, debe pedirte tareas hasta que metas el input 
#“end” (Por ejemplo). Con eso, se crea un nuevo diccionario con la clave tarea que hayas introducido .

comando_lista_tareas = 1 # palabra clave que acaba con el bucle, debe de ser igual a "end" para que acabe el bucle.

while comando_lista_tareas != "end":

    nombre_tarea = input(str("Introduzca el nombre de la tarea: "))
    id_tarea = input(int("Introduzca el ID de la tarea: "))
    tiempo_estimado = input(float("Introduzca el tiempo estimado de la tarea EN HORAS: "))
    trabajador_añadido = input(int("Introduzca el trabajador que quiera asignar a esta tarea: "))

    while trabajador_añadido != "end"

    trabajador_añadido = input(int("Introduzca otro trabajador al que quiera asignar a esta tarea (si no quiere asignar ningún otro trabajador a esta tarea intruduzca "end"): "))




        if 

    coste_tarea = 
 """