from datetime import datetime as dt
from worker_user import Worker_User
from manager_user import Manager_User
class Tarea:
    #definimos un metodo constructor
    def __init__(self, id_tarea : str, nombre_tarea : str, tiempo_estimado : int, fecha_inicio : dt, fecha_fin : dt,
                 fecha_limite : dt, coste_tarea : float, estado_tarea: bool ,id_proyecto: str, trabajadores: list):
        self.id_tarea = id_tarea
        self.nombre_tarea = nombre_tarea
        self.tiempo_estimado = tiempo_estimado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_limite = fecha_limite
        self.coste_tarea = coste_tarea
        self.estado_tarea = estado_tarea
        self.id_proyecto = id_proyecto
        self.trabajadores = trabajadores
    
    #definimos una lista donde guardaremos las tareas
    lista_tareas = []
    #definimos un metodo para mostrar la información básica de una tarea
    def mostrar_informacion_basica_tarea(self):
        print(f"ID : {self.id_tarea}\n Nombre {self.nombre_tarea}\nFecha inicio: {self.fecha_inicio}\Fecha fin: {self.fecha_fin}")
    
    #definimos un metodo para mostrar la información completa de una tarea
    def mostrar_informacion_completa_tarea(self):
        print(f"ID : {self.id_tarea}\n Nombre {self.nombre_tarea}\nTiempo estimado en días: {self.tiempo_estimado}\nFecha inicio: {self.fecha_inicio}\Fecha fin: {self.fecha_fin}")
        print(f"Fecha límite {self.fecha_limite}\nCoste: {self.coste_tarea}\nEstado: {self.estado_tarea}\nProyecto: {self.id_proyecto}\nTrabajadores: \n{self.trabajadores}")
        
    
    #definimos un metodo para añadir una tarea a la lista de tareas
    @classmethod
    def añadir_tarea(cls):
        if len(cls.lista_tareas) == 0:
            numero_tarea = 1
            id_tarea = "T" + str(numero_tarea)
        else:
            numero_tarea = len(cls.lista_tareas) +1
            id_tarea = "T" + str(numero_tarea)
        nombre_tarea = str(input("Introduce el nombre de la tarea: "))
        tiempo_estimado = dt.strptime(input("Introduce los días estimados que se tardarán en realizar la tarea: "),'%d')
        fecha_inicio = dt.strptime(input("Introduce la fecha de inicio de la tarea (dia/mes/año): "), '%d/%m/%y')
        fecha_fin = dt.strptime(input("Introduce la fecha de fin de la tarea (dia/mes/año): "), '%d/%m/%y')
        fecha_limite = dt.strptime(input("Introduce la fecha límite para poder realizar la tarea(dia/mes/año): "), '%d/%m/%y')
        coste_tarea = 0
        estado_tarea = False
        proyecto = ""
        trabajadores = []
        #creamos una tarea con los datos obtenidos y la añadimos a la lista de tareas
        nueva_tarea = Tarea(id_tarea, nombre_tarea, tiempo_estimado, fecha_inicio, fecha_fin, fecha_limite, coste_tarea,estado_tarea,proyecto,trabajadores)
        print("Tarea creada correctamente")
    
    #definimos un método para mostrar todas las tareas
    @classmethod
    def mostrar_tareas(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            for tareas in cls.lista_tareas:
                tareas.mostrar_informacion_basica_tarea() 
    
    #definimos un metodo para eliminar una tarea de la lista de tareas
    @classmethod
    def eliminar_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No hay tareas para eliminar")
        else:
            id_a_eliminar = str(input("Por favor introduce el ID de la tarea que desea eliminar: "))
            for tareas in cls.lista_tareas:
                if tareas.id_tarea == id_a_eliminar:
                    cls.lista_tareas.remove(tareas)
                    print("Tarea eliminada correctamente")
    #definimos un método para asignar un trabajador a la tarea
    @classmethod
    def asignar_trabajador_a_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            id_tarea = str("Introduce el id de la tarea a la que se le quiere añadir trabajadores")
            for tarea in cls.lista_tareas:
                if tarea.id_tarea == id_tarea:
                    if len(Worker_User.lista_workers) == 0:
                        print("No existen trabajadores todavia")
                    else:
                        while True:
                            print("Estos son los trabajadores existentes actualmente")
                            Worker_User.lista_workers()
                            id_trabajador = str(input("Introduce el id del trabajador que quieres añadir a la tarea: "))
                            for trabajador in Worker_User.lista_workers:
                                if trabajador.id_worker == id_trabajador:
                                    tarea.trabajadores.append(trabajador)
                                    #aumentamos el contador de tareas del trabajador en 1
                                    trabajador.contador_tareas_worker += 1
                                    print("Trabajador añadido correctamente")
                                    opcion = str("¿Quieres añadir otro trabajador? (S/N): ")
                                    if opcion == "S":
                                        continue
                                    else:
                                        break
    #definimos un metodo para asignar un manager a una tarea
    @classmethod
    def asignar_manager_a_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            id_tarea = str("Introduce el id de la tarea a la que se le quiere añadir un manager")
            for tarea in cls.lista_tareas:
                if tarea.id_tarea == id_tarea:
                    if len(Worker_User.lista_workers) == 0:
                        print("No existen trabajadores todavia")
                    else:
                        while True:
                            print("Estos son los managers existentes actualmente")
                            Manager_User.lista_managers()
                            id_manager = str(input("Introduce el id del manager que quieres añadir a la tarea: "))
                            for manager in Manager_User.lista_managers:
                                if manager.id_worker == id_manager:
                                    tarea.trabajadores.append(manager)
                                    #aumentamos el contador de tareas del manager en 1
                                    manager.contador_tareas_manager += 1
                                    print("Manager añadido correctamente")
    

                     