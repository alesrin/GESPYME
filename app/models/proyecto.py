from models.tarea import Tarea
import os
from flask import json

# Obtén la ruta al directorio base de tu aplicación Flask
base_dir = os.path.abspath(os.path.dirname(__file__))

# Construye la ruta al archivo JSON dentro del directorio 'Datos' en la raíz de tu aplicación
data_proyecto = os.path.join(base_dir, 'Datos', 'data_proyecto.json')

class Proyecto:
    def __init__(self, id_proyecto, nombre_proyecto, manager_proyecto, empleados, tareas):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.manager_proyecto = manager_proyecto
        self.empleados = empleados  # Lista de empleados asociados al proyecto
        self.tareas = tareas  # Lista de tareas del proyecto

    @classmethod
    def cargar_proyectos(cls):
        # Verificar si el archivo JSON existe
        if not os.path.exists(data_proyecto):
            # Archivo no encontrado, crear el archivo con datos iniciales
            datos_iniciales = [
                {
                    "id_proyecto": "P1",
                    "nombre_proyecto": "Proyecto 1",
                    "manager_proyecto": "UM1",
                    "empleados": [],  # Lista de empleados inicialmente vacía
                    "tareas": ["T1", "T2"]
                }
            ]

            # Escribir los datos iniciales en el archivo JSON
            with open(data_proyecto, 'w') as file:
                json.dump(datos_iniciales, file, indent=4)

        # Cargar los proyectos desde el archivo JSON
        with open(data_proyecto, 'r') as json_file:
            proyecto_data = json.load(json_file)
            proyectos = []
            for proyecto_data in proyecto_data:
                # Crear un objeto Proyecto utilizando los datos del archivo JSON
                proyecto = cls(
                    proyecto_data['id_proyecto'],
                    proyecto_data['nombre_proyecto'],
                    proyecto_data['manager_proyecto'],
                    proyecto_data['empleados'],  # Lista de empleados
                    proyecto_data['tareas']  # Lista de tareas
                )
                proyectos.append(proyecto)
            return proyectos

    
    def guardar_proyectos(proyectos):
        peliculas_data = [proyecto.to_dict() for proyecto in data_proyecto]
        with open(data_proyecto, 'w') as json_file:
            json.dump(peliculas_data, json_file, indent=4)
    
    
    
                
    #definimos un metodo para agregar un empleado a un proyecto



    #definimos un metodo para eliminar un empleado a un proyecto

                                
    #definimos un metodo para asignar un manager a un proyecto


    #definimos un metodo para desasignar un manager a un proyecto
                 
        
    #definimos un metodo para asignar una tarea a un proyecto
    @classmethod
    def asignar_tarea_a_proyecto(cls, id_proyecto):
        if Tarea.lista_tareas == 0:
            print("No hay tareas")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    while True:
                        print("Estas son las tareas disponibles que no se han asignado a ningun proyecto")
                        for tarea in Tarea.lista_tareas:
                            if tarea.id_proyecto != "":
                                tarea.mostrar_informacion_basica_tarea()
                                id_tarea = str("Introduce el id de la tarea que quieres asignar: ")
                                for tarea in Tarea.lista_tareas:
                                    if tarea.id_tarea == id_tarea:
                                        proyecto.tareas.appendd(tarea)
                                        #asignamos el valor del id proyecto a la tarea que se va a asignar
                                        tarea.id_proyecto = id_proyecto
                                        print("Tarea asignada correctamente")
                                        opcion = str("¿Quieres asignar otra tarea? (s/n): ")
                                        if opcion.lower() == "n":
                                            break
                            else:
                                print("no existe una tarea con ese id")             
        
    #definimos un metodo para desasignar una tarea a un proyecto
    @classmethod
    def desasignar_tarea_a_proyecto(cls, id_proyecto):
        if Tarea.lista_tareas == 0:
            print("No hay tareas")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    while True:
                        print("Estas son las tareas de este proyecto")
                        for tarea in Tarea.lista_tareas:
                            if tarea.id_proyecto == id_proyecto:
                                tarea.mostrar_informacion_basica_tarea()
                                id_tarea = str("Introduce el id de la tarea que quieres desasignar: ")
                                for tarea in Tarea.lista_tareas:
                                    if tarea.id_tarea == id_tarea:
                                        proyecto.tareas.remove(tarea)
                                        #Quitamos la asignacion del proyecto en la tarea
                                        tarea.id_proyecto = ""
                                        print("Tarea desasignada correctamente")
                                        opcion = str("¿Quieres desasignar otra tarea? (s/n): ")
                                        if opcion.lower() == "n":
                                            break
                            else:
                                print("no existe una tarea con ese id")    
    
     #definimos un metodo para crear un nuevo proyecto

    #definimos un método para eliminar un proyecto en funcion de su ID

    #definimos un metodo para editar un proyecto

    #definimos un metodo para mostrar los trabajadores de un proyecto

    #definimos un metodo para mostrar las tareas de un proyecto

    #definimos un metodo para comprobar si el nombre del proyecto ya existe

    #definimos un metodo para comprobar si el proyecto tiene tareas
