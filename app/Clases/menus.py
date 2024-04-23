from usuario import Usuario
import os
class Menu:

    #creamos el menu inicial
    @classmethod
    def menu_inicial(cls):
        while True:
            print("¿Que quieres hacer?")
            print("1.- Crear usuario")
            print("2.- Iniciar sesion")
            print("3.- Salir")
            print("4.- listar usuarios")
            print("5.- modificar usuario")
            print("6.- eliminar usuario")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                Menu.limpiar_pantalla()
                Usuario.agregar_Usuario()
            elif opcion == 2:
                Menu.limpiar_pantalla()
                Usuario.iniciar_sesion()
            elif opcion == 3:
                Menu.limpiar_pantalla()
                print("Hasta luego")
                break
            elif opcion == 4:
                Menu.limpiar_pantalla()
                Usuario.mostrar_usuarios()
            elif opcion == 5:
                Menu.limpiar_pantalla()
                Usuario.modificar_Usuario()
            elif opcion == 6:
                Menu.limpiar_pantalla()
                Usuario.eliminar_Usuario()
            else:
                print("Opcion incorrecta")
                print()


    #Definimos una funcion que limpie la pantalla
    @classmethod
    def limpiar_pantalla(cls):
        os.system('cls' if os.name=='nt' else 'clear')