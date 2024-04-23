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

    def __str__(self):
        return "ID: " + str(self.id_usuario) + " Usuario: " + str(self.nombre_usuario) + " Contraseña: " + str(self.contrasena_usuario) + " Tipo Usuario: " + str(self.tipo_usuario)

    #Definimos el metodo para agregar un usuario al diccionario
    @classmethod
    def agregar_Usuario(cls):
        if len(Usuario.lista_usuarios) == 0:
            id_usuario = 1
        else:
            id_usuario = len(Usuario.lista_usuarios) + 1
        print("Bienvenido al registro de usuarios")
        tipo_usuario = str(input("¿Que tipo de usuario desea registrar? manager o empleado: "))
        #si el tipo de usuario es manager comenzamos con su registro
        if tipo_usuario == "manager":
            nombre_usuario = str(input("Introduce el nombre del usuario a registrar: "))
            #comprobamos que el usuario este disponible
            if nombre_usuario in Usuario.lista_usuarios:  #preguntar a Alejandra(no funciona)
                print("El usuario ya existe")
            else:
                contrasena_usuario = str(input("Introduce la contraseña del usuario a registrar: "))
                comprobar_contraseña = str(input("Introduce de nuevo la contraseña: "))
                if contrasena_usuario != comprobar_contraseña:
                    print("Las contraseñas no coinciden")
                else:   
                    #Creamos un objeto Usuario con los datos y lo añadimos a la lista
                    nuevo_usuario = Usuario(id_usuario, nombre_usuario, contrasena_usuario, tipo_usuario)
                    #Agregamos el usuario a la lista
                    Usuario.lista_usuarios.append(nuevo_usuario)
                    print("Usuario " + str(nombre_usuario) +  " registrado correctamente")
        elif tipo_usuario == "empleado":
            print("En proceso....")
        else:
            print("El tipo de usuario no es correcto")
               


    #Definimos el metodo para eliminar un usuario de la lista
    @classmethod
    def eliminar_Usuario(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            id_usuario = int(input("Introduce el id del usuario que quieres eliminar"))
            Usuario.lista_usuarios.remove(id_usuario)
            print("El usuario ha sido eliminado corectamente")


    #Definimos un metodo para mostrar los datos de los  usuarios de la lista
    @classmethod 
    def mostrar_usuarios(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay usuarios registrados")
        else:
           for i, usuario in enumerate(Usuario.lista_usuarios, start=1): #preguntar a Alejandra
            print(f"Usuario {i}:")
            print(f"ID: {usuario.id_usuario}")
            print(f"Usuario: {usuario.nombre_usuario}")
            print(f"Contraseña: {usuario.contrasena}")
            print()


    #definimos un método para iniciar sesión
    @classmethod
    def iniciar_sesion(cls):
        if len(Usuario.lista_usuarios)==0:
            print("\nNo hay usuarios registrados\n")
        else:
            usuario_inicio = str(input("Introduce el usuario: "))
            contrasena_inicio = str(input("Introduce la contraseña: "))
            #recorremos la lista de usuarios
            for usuario_a_comprobar in Usuario.lista_usuarios:
                #comprobamos si el usuario y la contraseña son correctos
                if usuario_a_comprobar.nombre_usuario == usuario_inicio and usuario_a_comprobar.contrasena_usuario == contrasena_inicio: #preguntar a alejandra
                    print("Bienvenido " + usuario_a_comprobar.nombre_usuario)