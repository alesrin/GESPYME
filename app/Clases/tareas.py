import datetime
from worker_user import Worker_User
class Tarea:
    #definimos un metodo constructor
    def __init__(self, id_tarea, nombre_tarea, tiempo_estimado, fecha_inicio, fecha_fin, fecha_limite, coste_tarea, estado_tarea,id_proyecto,  trabajadores: list):
        self.id_teara = id_tarea
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
        print(f"ID {self.id_tarea}\nNombre {self.nombre_tarea}\nFecha_inicio {self.fecha_inicio}\nFecha fin {self.fecha_fin}")
    
    #definimos un metodo para mostrar toda la informacion de una tarea
    def mostrar_informacion_completa_tarea(self):
        print(f"ID {self.id_teara}\nNombre {self.nombre_tarea}\nTiempo estimado {self.tiempo_estimado}\nFecha inicio {self.fecha_inicio}\nFecha fin {self.fecha_fin}")
        print(f"Fecha limite {self.fecha_limite}\nCoste tarea {self.coste_tarea}\nTrabajadores {self.trabajadores}\nEstado tarea {self.estado_tarea}\nProyecto {self.id_proyecto}")
    
   
        