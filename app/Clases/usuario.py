import
from worker_user import Worker_User
from manager_user import Manager_User
from administrador_user import Administrador_User

#Definimos la clase Usuario
class Usuario:
    #Definimos el metodo constructor
    def __init__(self, id_usuario : int, nombre_usuario : str, contrasena_usuario : str, tipo_usuario: str ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena_usuario = contrasena_usuario
        self.tipo_usuario = tipo_usuario
        

    #Definimos una lista vacia donde se guradarán los datos de los usuarios
    lista_usuarios = []

    #Definimos el metodo para mostrar la informacion de cada usuario
    def mostrar_datos_usuario(self):
        print(f"ID: {self.id_usuario} \nUsuario: {self.nombre_usuario}\nContraseña: {self.contrasena_usuario}\nTipo Usuario: {self.tipo_usuario}")

    #Definimos el metodo para agregar un usuario a la lista
    def agregar_usuario(self):
        if len(Usuario.lista_usuarios) == 0:
            numero_usuario = 1
            id_usuario = "U" + str(numero_usuario)
        else:
            numero_usuario = len(Usuario.lista_usuarios) +1
            id_usuario = "U" + str(numero_usuario)
            nombre = str(input("Introduce el nombre del usuario: "))
            if self.comprobar_nombre_usuario(nombre) == False:
                print("El nombre de usuario ya existe")
            else: 
                contrasena = pwd(input("Introduce la contraseña del usuario: "))
                confirmar_contrasena = pwd(input("Confirma la contraseña: "))
                if contrasena != confirmar_contrasena:
                    print("Las contraseñas no coinciden")
                else:
                    tipo_usuario = str(input("Introduce el tipo de usuario pueden ser administrador | worker | manager: "))
                    if tipo_usuario.lower() != "administrador" and tipo_usuario.lower() != "worker" and tipo_usuario.lower() != "manager":
                        print("Tipo de usuario incorrecto")
                    else:
                        #Creamos un objeto de la clase Usuario con los datos introducidos por el usuario
                        usuario = Usuario(id_usuario, nombre, contrasena, tipo_usuario)
                        #Agregamos el objeto a la lista de usuarios
                        Usuario.lista_usuarios.append(usuario)
                        print("Usuario agregado correctamente")
        



    #definimos un método para comprobar si el nombre de usuario ya existe en la lista de usuarios
    def comprobar_nombre_usuario(self, nombre_usuario):
        for usuario in Usuario.lista_usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return False
                
