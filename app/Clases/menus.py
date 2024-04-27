from usuario import Usuario
from manager_user import Manager_User
from administrador_user import Administrador_User
from worker_user import Worker_User
import os
class Menu:


    @classmethod
    def menu_pruebas(cls):
        while True:
            print("Hola MAJO, QUENQUIERES PROBAR")
            print("-. 1 Menu usuarios workers")
            print("-. 2 menu usuarios manager")
            print("-. 3 Menu usuarios administradores")
            print("-. 4 Menu principal")
            print("-. 5 Salir")
            opcion = int(input("Introduce la opción que quieres probar guapo ♥: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                cls.menu_final_worker()
            elif opcion == 2:
                cls.limpiar_pantalla()
                cls.menu_final_manager()
            elif opcion == 3:
                cls.limpiar_pantalla()
                cls.menu_final_administrador()
            elif opcion == 4:
                cls.limpiar_pantalla()
                cls.menu_inicial()
            elif opcion == 5:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
        
    #definimos el menu inicial de usuarios
    @classmethod
    def menu_principal(cls):
        while True:
            print("Hola, Bienvenido a GESPYME")
            print("-. 1 Iniciar sesión")
            print("-. 2 Registrase")
            print("-. 3 recuperar contraseña")
            print("-. 3 Salir")
            opcion = int(input("Elije que quieres hacer: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Usuario.iniciar_sesion()
            elif opcion == 2:
                cls.limpiar_pantalla()
                Usuario.registrar_usuario()
            elif opcion == 3:
                cls.limpiar_pantalla()
                Usuario.recuperar_contraseña()
            elif opcion == 4:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
                
    
    #definimos el menú final de los administradores
    @classmethod
    def menu_final_administrador(cls):
        while True:
            print("-. 1 Crear un  Manager")
            print("-. 2 Eliminar un Manager")
            print("-. 3 Modificar los datos de un Manager")
            print("-. 4 mostrar Managers creados")
            print("-. 5 Asignar un usuario de inicio de sesion a un Manager")
            print("-. 6 Añadir un administrador al sistema")
            print("-. 7 Crear usuario en el sistema")
            print("-. 8 Acceder a funcionalidades de Manager")
            print("-. 9 Salir")
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Manager_User.añadir_manager()
            elif opcion == 2:
                cls.limpiar_pantalla()
                Manager_User.eliminar_manager()
            elif opcion == 3:
                cls.limpiar_pantalla()
                Manager_User.modificar_manager()
            elif opcion == 4:
                cls.limpiar_pantalla()
                Manager_User.mostrar_managers()
            elif opcion == 5:
                cls.limpiar_pantalla()
                Usuario.asignar_manager_usuario()
            elif opcion == 6:
                cls.limpiar_pantalla()
                Administrador_User.añadir_administrador()
            elif opcion == 7:
                cls.limpiar_pantalla()
                Usuario.agregar_usuario()
            elif opcion == 8:
                cls.limpiar_pantalla()
                Manager_User.menu_final_manager()
            elif opcion == 9:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
    
    #definimos el menú final del usuario manager
    @classmethod
    def menu_final_manager(cls):
        while True:
            print("-. 1 Crear worker")
            print("-. 2 Eliminar worker")
            print("-. 3 Modificar datos worker")
            print("-. 4 Listar workers")
            print("-. 5 Asignar usuario de inicio de seión a worker")
            print("-. 6 Crear Proyecto nuevo")
            print("-. 7 Modificar proyecto")
            print("-. 8 Eliminar proyecto")
            print("-. 9 Crear tarea")
            print("-. 10 Modificar datos tarea")
            print("-. 11 Eliminar tarea")
            print("-. 12 Asignar trabajador a tarea")
            print("-. 13 Eliminar trabajador de tarea")
            print(".- 14 Salir")
            opcion = int(input("Por favor introduce una opción: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Worker_User.añadir_worker()
            elif opcion == 2:
                cls.limpiar_pantalla()
                Worker_User.borrar_worker()
            elif opcion == 3:
                cls.limpiar_pantalla()
                Worker_User.modificar_usuario_worker()
            elif opcion == 4:
                cls.limpiar_pantalla()
                Worker_User.mostrar_info_reducida_worker()
            elif opcion == 5:
                cls.limpiar_pantalla()
                Usuario.asignar_worker_usuario()
            elif opcion == 6:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 7:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 8:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 9:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 10:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo") 
            elif opcion == 11:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 12:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 13:
                cls.limpiar_pantalla()
                print("Opcion en desarrollo")
            elif opcion == 14:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break                    

    #Definimos el menú final de un worker
    @classmethod
    def menu_final_worker(cls):
        while True:
            print("-.1 Mostrar tareas asignadas")
            print("-. 2 Salir")
            opcion = int(input("Elije que quieres hacer: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                print("Funcion en proceso...")
            elif opcion == 2:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
            
    #Definimos una funcion que limpie la pantalla
    @classmethod
    def limpiar_pantalla(cls):
        os.system('cls' if os.name=='nt' else 'clear')
        
#definimos el main
if __name__ == "__main__":
    #creamos un objeto de la clase menu
    Menu.limpiar_pantalla()
    Menu.menu_pruebas()
    
    