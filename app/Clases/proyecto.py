from worker_user import Worker_User
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
    def agregar_empleado(cls):
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
                            print("Trabajador añadido correctamente")
    
    #definimos un metodo para ostrar todos los proyectos
    @classmethod
    def mostrar_proyectos(cls):
        if len(cls.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                proyecto.mostrar_info_basica_proyecto()