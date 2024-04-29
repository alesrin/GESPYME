from menus import Menu
from usuario import Usuario
from administrador_user import Administrador_User
from worker_user import Worker_User
from manager_user import Manager_User
class Usuario:
    #Definimos el metodo constructor
    def __init__(self, id_usuario : int, nombre_usuario : str, contrasena_usuario : str, tipo_usuario: str, id_empleado: str ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena_usuario = contrasena_usuario
        self.tipo_usuario = tipo_usuario
        self.id_empleado = id_empleado
        

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
                contrasena = str(input("Introduce la contraseña del usuario: "))
                confirmar_contrasena = str(input("Confirma la contraseña: "))
                if contrasena != confirmar_contrasena:
                    print("Las contraseñas no coinciden")
                else:
                    tipo_usuario = str(input("Introduce el tipo de usuario pueden ser administrador | worker | manager: "))
                    if tipo_usuario.lower() != "administrador" and tipo_usuario.lower() != "worker" and tipo_usuario.lower() != "manager":
                        print("Tipo de usuario incorrecto")
                    elif tipo_usuario.lower() == "administrador":
                        #Creamos un objeto de la clase Usuario con los datos introducidos por el usuario
                        id_empleado = id_usuario
                    else:
                        id_empleado =""
                    usuario = Usuario(id_usuario, nombre, contrasena, tipo_usuario,id_empleado)
                    #Agregamos el objeto a la lista de usuarios
                    Usuario.lista_usuarios.append(usuario)
                    print("Usuario agregado correctamente")
        
    #definimos un metodo para mostrar los usuarios
    @classmethod
    def mostrar_usuarios(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            #Creamos un bucle para que el usuario pueda ver todos los usuarios creados
            for usuario in Usuario.lista_usuarios:
                usuario.mostrar_datos_usuario()
    
    #definimos un metodo para eliminar un usuario en funcion de su id
    @classmethod
    def eliminar_usuario(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            print("Estos son los usuarios actualmente")
            #Creamos un bucle para que el usuario pueda ver todos los usuarios creados
            Usuario.mostrar_usuarios()
            id_a_borrar = str(input("Introduce el ID del usuario que desea eliminar: "))
            #Creamos un bucle para comprobar el id que deseamos eliminar
            for user in Usuario.lista_usuarios:
                if user.id_usuario == id_a_borrar.upper():
                    Usuario.lista_usuarios.remove(user)
                    print("El usuario " + str(user.nombre_usuario) + " ha sido eliminado correctamente")
                    break
                else:
                    print("No existe un usuario con el ID introducido")
                    break
    
    #Definimos un metodo que permita modificar un usuario en funcion de su id
    @classmethod
    def modificar_usuario(cls):
        #mostramos los managers que existen actualmente
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            Usuario.mostrar_usuarios()
            id_a_modificar = str(input("Introduce el id del usuario manager que desea modificar: "))
            #Creamos un bucle para comprobar el id que deseamos modificar
            for user in Usuario.lista_usuarios:
                if user.id_usuario == id_a_modificar.upper():
                    print("Estos son los datos del usuario seleccionado")
                    user.mostrar_datos_usuario()
                    #Creamos un bucle para que el usuario pueda modificar los datos
                    while True:
                        print("¿Que dato desea modificar?")
                        print("-. 1  usuario")
                        print("-. 2 contraseña")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre de usuario: "))
                            user.nombre_usuario = nuevo_nombre
                            print("El nombre de usuario ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nueva_contrasena = str(input("Introduce la nueva contraseña: "))
                            confirmar_contrasena = str(input("Confirma la contraseña: "))
                            if nueva_contrasena != confirmar_contrasena:
                                print("Las contraseñas no coinciden")
                            else:
                                user.contrasena = nueva_contrasena
                                print("La contrasena ha sido modificado correctamente")
                                opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                                if opcion.upper() == "S":
                                    continue
                                elif opcion.upper() == "N":
                                    break
    
    #Definimos un metodo para que el usuario inicie sesión
    @classmethod
    def iniciar_sesion(cls):
        usuario_inicio_sesion = str(input("Introduce el nombre de usuario: "))
        #comprobamos que el usuario existe en la lista de usuarios
        for usuario in Usuario.lista_usuarios:
            if usuario.nombre_usuario == usuario_inicio_sesion:
                contrasena_inicio_sesion = str(input("Introduce la contraseña: "))
                if usuario.contrasena_usuario == contrasena_inicio_sesion:
                    print("Sesión iniciada correctamente")
                    if usuario.tipo_usuario == "administrador":
                        Menu.menu_final_administrador
                    elif usuario.tipo_usuario == "worker":
                        Menu.menu_final_worker
                    elif usuario.tipo_usuario == "manager":
                        Menu.menu_usuario_manager()
                else:
                    print("La contraseña es incorrecta")
        else:
            print("El usuario no existe")
     

    #definimos una funcion para asigar un worker user a un usuario
    @classmethod
    def asignar_worker_usuario(cls):
        print("Estos son los usuarios que no tienen un empleado asignado")
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == "":
                usuario.mostrar_datos_usuarios()
        print("Estos son los trabajadores existentes actualmente")
        Worker_User.mostrar_workers()
        id_empleado_seleccionado = str(input("Por favor escribe el ID del trabajador que tendrá asignado a este usuario: "))
        if Usuario.comprobar_id_empleado(id_empleado_seleccionado == False):
            print("Ese usuario ya a sido asignado a un trabajador, por favor seleccione otro ID")
        else: 
            usuario.id_empleado = id_empleado_seleccionado
            print("El usuario ha sido asignado correctamente")
        
    #definimos una funcion para asigar un worker user a un usuario
    @classmethod
    def asignar_manager_usuario(cls):
        print("Estos son los usuarios que no tienen un empleado asignado")
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == "":
                usuario.mostrar_datos_usuarios()
        print("Estos son los managers existentes actualmente")
        Manager_User.mostrar_info_reducida_manager()
        id_empleado_seleccionado = str(input("Por favor escribe el ID del manager que tendrá asignado a este usuario: "))
        if Usuario.comprobar_id_empleado(id_empleado_seleccionado == False):
            print("Ese usuario ya a sido asignado a un manager, por favor seleccione otro ID")
        else: 
            usuario.id_empleado = id_empleado_seleccionado
            print("El usuario ha sido asignado correctamente")        
        
    #definimos un metodo para saber si el id_empleado ya está en uso
    def comprobar_id_empleado(self, id_empleado):
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == id_empleado:
                return False
            
            
    
    #definimos un método para comprobar si el nombre de usuario ya existe en la lista de usuarios
    def comprobar_nombre_usuario(self, nombre_usuario):
        for usuario in Usuario.lista_usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return False
    
    #definimos un método para que el usuario pueda recuperar su contraseña
    def recuperar_contraseña(cls):
        email_usuario = str("Por favor introduce el email para mandarle las instrucciones para recuperar su contraseña: ")
        for usuario in Usuario.lista_usuarios:
            if usuario.email_administrador == email_usuario:
                print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
            else:
                for worker in Worker_User.lista_workers:
                    if worker.email_worker == email_usuario:
                        print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
                    else:
                        for manager in Manager_User.lista_managers:
                            if manager.email_manager == email_usuario:
                                print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
                            else:
                                print("No existe ningun usuario con ese email, por favor pruebe otra cuenta")   
#definimos un objeto de tipo usuario y lo añadimos a la lista
usuario1 = Usuario("U1", "daniel", "daniel", "administrador","U1")
Usuario.lista_usuarios.append(usuario1)