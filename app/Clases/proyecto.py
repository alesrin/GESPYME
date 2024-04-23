class Proyecto:
    #Declaramos el método constructor
    def __init__(self, id_proyecto : int, nombre_proyecto : str, empleados: list, manager : list):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.empleados = empleados
        self.manager = manager

def __str__(self):
    return f"Id Proyecto: {self.id_proyecto}\n" \
           f"Proyecto: {self.nombre_proyecto}\n" \
           f"Empleados: {self.empleados}\n" \
           f"Manager: {self.manager}\n"

