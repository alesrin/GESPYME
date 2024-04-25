

class Proyecto:
    def __init__(self, nombre, *lista_tareas): #Crear proyectos: Decir el nombre de proyecto y al menos una tarea
        self.nombre = nombre
        self.lista_tareas = list(lista_tareas) 
        #fdgdshgd prueba
    @classmethod 
    #Este método se asocia con la clase y no con los objetos  
    #Defino una función para que el usuario puedad agregar un nuevo trabajador

    def agregar_tarea(cls, tarea): #Añadir  tareas a un proyecto
        print("Introduce los datos de la nueva tarea:\n")
        #id_tarea = str(input("Introduce el ID de la nueva tarea:\n")) #ES UN DATO A INTRODUCIR?, segun las tabalas iniciales del proyecto en notion, es un valor autoincremental
        nombre_tarea = str(input("Introduce el nombre de la nueva tarea:"))
        tiempo_estimado = float(input("Introduce el tiempo estimado que lleva la tarea en horas:")) #ES FLOAT Y NO INT PARA QUE SE PUEDA DECIR 7,5 horas, por ejemplo
        
        #Las dos lineas de aquí abajo son necesarias para introducir la fecha de inicio, la expliación del metodo empleado
        #Esta en este enlace: https://www.w3schools.com/python/python_datetime.asp
        import datetime
        fecha_de_inicio = datetime.datetime(input("Introduce el año de inicio de la tarea:"),input("Introduce el més de inicio de la tarea:"),input("Introduce el dia de inicio de la tarea:"))

        #Aquí abajo hay que hacer el código que te devuelva la fecha de fin a partir de la fecha de inicio y del tiempo estimado
        fecha_de_fin = datetime.datetime(input("Introduce el año de fin de la tarea:"),input("Introduce el més de fin de la tarea:"),input("Introduce el dia de inicio de la tarea:"))
        
        #AQUI SE ASIGNA A LOS TRABAJADORES A LA TAREA: ESTA EL CÓDIGO HECHO EN EL DOCUMENTO "TRABAJADORES A LA TAREA" QUE TAMBIÉN HE AÑADIDO
        lista_trabajadores = []


        #Aquí abajo hay que hacer el código que calcule el coste de cada tarea.
        """for coste_de_trabajador_por_hora and tiempo_que_ha_dedicado_trabajador_a_la_tarea in coste_de_cada_trabajador_por_hora and tiempo_que_ha_dedicado_cada_trabajador_a_la_tarea :

            coste_tarea += coste_de_trabajador_por_hora * tiempo_que_ha_dedicado_trabajador_a_la_tarea 
            #Luego tenemos que hacer una opción que sustitulla el tiempo estimado por el tiempo real"""
        
        """ 
        float(coste_tarea)
        trabajador_nuevo = cls(nombre, edad, salario)
        lista_trabajadores.append(trabajador_nuevo) """
    
    @classmethod 
    def mostrar_trabajador(cls, lista_trabajadores):
        print("Lista de trabajadores:\n")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}")
            print()
            

trabajadores = []

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
        break
    








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
 """res que ha asignado a esta tarea son: \n{lista_trabajadores}")