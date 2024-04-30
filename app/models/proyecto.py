from worker_user import Worker_User
from manager_user import Manager_User

class Proyecto:
    #definimos un metodo constructor
    def __init__(self, id_proyecto : str, nombre_proyecto : str, manager_proyecto : object, empleados : list, tareas : list):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.manager_proyecto = manager_proyecto
        self.empleados = empleados
        self.tareas = tareas

    #definimos una lista donde se guardarán todos los proyectos
    lista_proyectos = []
    
    #definimos un método para mostrar la información básica de los proyectos
    @classmethod
    def mostrar_info_basica_proyecto(self):
        print(f"ID: {self.id_proyecto}\nNombre: {self.nombre_proyecto}")
    
    #definimos un metodo para mostrar toda la informacion de un proyecto
    @classmethod
    def mostrar_info_completa_proyecto(self):
        print(f"ID: {self.id_proyecto}\nNombre: {self.nombre_proyecto}\nManager: {self.manager_proyecto}")
        print(f"\nTrabajadores: {self.empleados}\nTareas: {self.tareas}")
    
    #definimos un metodo para agregar un empleado a un proyecto
    @classmethod
    def agregar_empleado_a_proyecto(cls):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            cls.lista_proyectos
            id_proyecto = str(input("Introduce el ID del proyecto que quieres añadir un empleado"))
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    print("Lista de trabajadores: ")
                    Worker_User.lista_workers()
                    id_worker = input("Ingrese el ID del trabajador que desea añadir: ")
                    for worker in Worker_User.lista_workers:
                        if worker.id_worker == id_worker:
                            proyecto.empleados.append(worker)
                            #aumentamos el contador de proyectos del trabajador
                            worker.contador_proyectos_worker += 1
                            print("Trabajador añadido correctamente")
    
    #definimos un metodo para ostrar todos los proyectos
    @classmethod
    def mostrar_proyectos(cls):
        if len(cls.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                proyecto.mostrar_info_basica_proyecto()

    #definimos un metodo para eliminar un empleado a un proyecto
    @classmethod
    def eliminar_empleado_a_proyecto(cls):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            cls.lista_proyectos
            id_proyecto = str(input("Introduce el ID del proyecto que quieres eliminar un empleado"))
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    print("Lista de trabajadores: ")
                    Worker_User.lista_workers()
                    id_worker = input("Ingrese el ID del trabajador que desea eliminar: ")
                    for worker in proyecto.empleados:
                        if worker.id_worker == id_worker:
                            #disminuimos el contador de proyectos del trabajador
                            worker.contador_proyectos_worker -= 1
                            proyecto.empleados.remove(worker)
                            print("Trabajador añadido correctamente")

    #definimos un metodo para asignar un manager a un proyecto
    @classmethod
    def asignar_manager_a_proyecto(cls):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            cls.lista_proyectos
            id_proyecto = str(input("Introduce el ID del proyecto al que quieres asignar un manager"))
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    print("Lista de managers: ")
                    Manager_User.lista_managers()
                    id_manager = input("Ingrese el ID del manager que desea añadir: ")
                    for manager in Manager_User.lista_managers:
                        if manager.id_manager == id_manager:
                            proyecto.manager_proyecto = manager
                            #aumentamos el contador de proyectos del trabajador
                            manager.contador_proyectos_manager += 1
                            print("Manager asignado correctamente")

    #definimos un metodo para desasignar un manager a un proyecto
    @classmethod
    def desasignar_manager_a_proyecto(cls):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            cls.lista_proyectos
            id_proyecto = str(input("Introduce el ID del proyecto al que quieres desasignar un manager"))
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    id_manager = proyecto.manager_proyecto.id_manager
                    for manager in Manager_User.lista_managers:
                        if manager.id_manager == id_manager:
                            proyecto.manager_proyecto = manager
                            #aumentamos el contador de proyectos del trabajador
                            manager.contador_proyectos_manager += 1
                            proyecto.manager_proyecto = None
                            print("Manager asignado correctamente")                      
    
    #definimos un metodo para crear un nuevo proyecto
    @classmethod
    def crear_proyecto(cls):
        if len(cls.lista_proyectos) == 0:
           numero_proyecto = 1
           id_proyecto = "P" + str(numero_proyecto)
        else:
            numero_proyecto = len(cls.lista_proyectos) +1
            id_proyecto = "P" + str(numero_proyecto)
        nombre_proyecto = str(input("Introduce el nombre del proyecto: "))
        if cls.comprobar_nombre_proyecto(nombre_proyecto) == True:
            print("El nombre del proyecto ya existe")
        else:
             
        
    #definimos un metodo para comprobar si el nombre del proyecto ya existe
    @classmethod
    def comprobar_nombre_proyecto(cls, nombre_proyecto):
        for proyecto in cls.lista_proyectos:
            if proyecto.nombre_proyecto == nombre_proyecto:
                return True