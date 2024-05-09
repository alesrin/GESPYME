from datetime import datetime as dt
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
   
    #definimos un metodo para mostrar la información completa de una tarea

        
    
    #definimos un metodo para añadir una tarea a la lista de tareas
    
    
    #definimos un método para mostrar todas las tareas

    
    #definimos un metodo para eliminar una tarea de la lista de tareas

                    
    #definimos un método para asignar un trabajador a la tarea
                                    
    #definimos un metodo para eliminar un trabajador ya sea manager o worker de una tarea
                        
    #definimos un método para modificar el estado de una tarea

    #definimos un método para calcular el coste de una tarea
    
    #definimos un método para mostrar las tareas de un trabajador

    #definimos un metodo para mostrar los trabajadores de una tarea
                
    #definimos un método para modificar los datos de una tarea
