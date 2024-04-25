#from menus import Menu #preguntar a alejandra, sigue dando fallo
#from trabajador import Trabajador #preguntar a alejandra
class Usuario:
    #Definimos el metodo constructor
    def __init__(self, id_usuario : int, nombre_usuario : str, contrasena_usuario : str, tipo_usuario: str):
        id_usuario = id_usuario
        nombre_usuario = nombre_usuario
        contrasena_usuario = contrasena_usuario
        tipo_usuario = tipo_usuario
        

    #Definimos una lista vacia donde se guradarán los datos de los usuarios
    lista_usuarios = []

    #Definimos el metodo para mostrar la informacion de cada usuario

    def mostrar_datos_usuario(self):
        return "ID: " + str(self.id_usuario) + " Usuario: " + str(self.nombre_usuario) + " Contraseña: " + str(self.contrasena_usuario) + " Tipo Usuario: " + str(self.tipo_usuario)

