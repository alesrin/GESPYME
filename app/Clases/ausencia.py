import datetime
#Declaramos el método constructor
class Ausencia:
    def __init__(self, id_ausencia : int, trabajador: object , fecha_inicio : datetime, fecha_fin : datetime, duracion: datetime, motivo : str):
        self.id_ausencia = id_ausencia
        self.trabajador = trabajador
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.duracion = duracion
        self.motivo = motivo