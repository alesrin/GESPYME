from usuario import Usuario
from manager_user import Manager_User
from administrador_user import Administrador_User
from worker_user import Worker_User
import os
class Menu:

    #creamos el menu inicial
    @classmethod
    def menu_inicial(cls):
        while True:
            print("¿Que quieres hacer?")
            print("1.- Iniciar sesion")
            print("2.- Crear usuario")
            print("3.- Recuperar contraseña")
            print("4.- Salir")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                Menu.limpiar_pantalla()
                Usuario.iniciar_sesion()
            elif opcion == 2:
                Menu.limpiar_pantalla()
                Usuario.agregar_Usuario()
            elif opcion == 3:
                Menu.limpiar_pantalla()
                print("Funcion en desarrollo")
            elif opcion == 4:
                Menu.limpiar_pantalla()
                print("Hasta luego")
                break
            else:
                print("Opcion incorrecta")
                print()
        
    #creamos el menu de operaciones CRUD de usuario_manager
    @classmethod
    def menu_usuario_manager(cls):
        while True:
            print("Bienvenido al menú de gestión de usuarios Managers")
            print("-. 1 Añadir usuario manager")
            print("-. 2 Eliminar usuario manager")
            print("-. 3 Modificar usuario manager")
            print("-. 4 Mostrar usuarios manager")
            print("-. 5 Salir")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                Menu.limpiar_pantalla()
                Manager_User.añadir_manager()
            elif opcion == 2:
                Menu.limpiar_pantalla()
                Manager_User.borrar_manager()
            elif opcion == 3:
                Menu.limpiar_pantalla()
                Manager_User.modificar_usuario_manager()
            elif opcion == 4:
                Menu.limpiar_pantalla()
                Manager_User.mostrar_managers()
            elif opcion == 5:
                Menu.limpiar_pantalla()
                print("Hasta luego")
                break
        
    #creamos el menu de operaciones CRUD de usuario administrador
    @classmethod
    def menu_usuario_administrador(cls):
        while True:
            print("Bienvenido al menú de gestión de usuarios Administradores")
            print("-. 1 Añadir usuario administrador")
            print("-. 2 Eliminar usuario administrador")
            print("-. 3 Modificar usuario administrador")
            print("-. 4 Mostrar usuarios administrador")
            print("-. 5 Salir")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                Menu.limpiar_pantalla()
                Administrador_User.añadir_administrador()
            elif opcion == 2:
                Menu.limpiar_pantalla()
                Administrador_User.borrar_administrador()
            elif opcion == 3:
                Menu.limpiar_pantalla()
                Administrador_User.modificar_usuario_administrador()
            elif opcion == 4:
                Menu.limpiar_pantalla()
                Administrador_User.mostrar_administradores()
            elif opcion == 5:
                Menu.limpiar_pantalla()
                print("Hasta luego")
                break

    #creamos el menu de operaciones CRUD de usuario administrador
    @classmethod
    def menu_usuario_worker(cls):
        while True:
            print("Bienvenido al menú de gestión de usuarios Workers")
            print("-. 1 Añadir usuario worker")
            print("-. 2 Eliminar usuario worker")
            print("-. 3 Modificar usuario worker")
            print("-. 4 Mostrar usuarios worker")
            print("-. 5 Salir")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                Menu.limpiar_pantalla()
                Worker_User.añadir_worker
            elif opcion == 2:
                Menu.limpiar_pantalla()
                Worker_User.borrar_worker()
            elif opcion == 3:
                Menu.limpiar_pantalla()
                Worker_User.modificar_usuario_worker()
            elif opcion == 4:
                Menu.limpiar_pantalla()
                Worker_User.mostrar_workers()
            elif opcion == 5:
                Menu.limpiar_pantalla()
                print("Hasta luego")
                break
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
                cls.menu_usuario_worker()
            elif opcion == 2:
                cls.limpiar_pantalla()
                cls.menu_usuario_manager()
            elif opcion == 3:
                cls.limpiar_pantalla()
                cls.menu_usuario_administrador()
            elif opcion == 4:
                cls.limpiar_pantalla()
                cls.menu_inicial()
            elif opcion == 5:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
        
    #definimos el menu inicial de usuarios
    @classmethod
    def menu_usuario(cls):
        while True:
            print("Hola, Bienvenido a GESPYME")
            print("-. 1 Iniciar sesión")
            print("-. 2 Registrase")
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
    Menu.menu_inicial()
    
    