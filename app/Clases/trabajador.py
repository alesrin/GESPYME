from menus import Menu
class Trabajador:
    #Creamos el constructor del objeto
    def __init__(self, id_trabajador : int, nombre_trabajador : str, apellido_1 : str, apellido_2 : str, horas_semanales : float, coste_hora : float, puesto_trabajo : str, contador_tareas: int, email : str):
        self.id_trabajador = id_trabajador
        self.nombre_trabajador = nombre_trabajador
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.horas_semanales = horas_semanales
        self.coste_hora = coste_hora
        self.puesto_trabajo = puesto_trabajo
        self.contador_tareas = contador_tareas
        self.email = email

    #preguntar a alejandra como implementar herencia con Trabajador

    #Creamos un constructor vacio
    def __init_(self):
        self.id_trabajador = 0
        self.nombre_trabajador = ""
        self.apellido_1 = ""
        self.apellido_2 = ""
        self.horas_semanales = 0
        self.coste_hora = 0
        self.puesto_trabajo = ""
        self.contador_tareas = 0
        self.email = ""
    #Metodo para mostrar los datos del trabajador en formato legible
    def __str__(self) -> None:
        print ("ID: ",self.id_trabajador,"\nNombre: ",self.nombre_trabajador, "\nPrimer apellido: ",self.apellido_1, 
              "\nSegundo apellido: ",self.apellido_2, "\nHoras semanales",self.horas_semanales,"\nCoste hora: ",self.coste_hora,  
              "\nPuesto de trabajo: ", self.puesto_trabajo,"\nContador de tareas: ",self.contador_tareas,"\nCorreo: ",self.email)
        
    #creamos una lista vacion donde guradaremos la informacion de todos los trabajadores
    lista_trabajadores = []
   
   #Definimos una funcion para crear un nuevo trabajador y añadirlo al diccionario
    @classmethod
    def nuevo_trabajador(self):
        #Asignamos al trabajador un id autoincremental
        if len(Trabajador.listar_trabajadores) == 0:
            id_trabajador = 1
        else:
            id_trabajador = len(Trabajador.lista_trabajadores) + 1   
            #Pedimos los demas datos por teclado
        print("Introduzca los siguientes datos para registrarse:\n")
        nombre = str(input("\tNombre: ")).upper()
        apellido1 = str(input("\tPrimer Apellido: ")).upper()
        apellido2 = str(input("\tSegundo Apellido: ")).upper()           
        horas_semanales = float(input("\tHoras semanales: "))
        coste_hora = float(input("\tCoste/Hora: "))
        puesto = str(input("\tPuesto de trabajo: ")).upper()
        contador_tareas = 0
        email = str(input("\tDireccion E-mail: ")).upper()
        #Creamos un nuevo trabajador y lo añadimos al diccionario
        nuevo_trabajador = Trabajador(id_trabajador, nombre, apellido1, apellido2, horas_semanales, coste_hora, puesto, contador_tareas, email)
        #Mostramos un mensaje de que el trabajador se ha registrado correctamente
        Menu.limpiar_pantalla()
        print("Registro completado correctamente")


    @classmethod
    def listar_trabajadores(self):
        if len(Trabajador.lista_trabajadores)==0:
            print("\nNo hay trabajadores registrados\n")
        else:
            print("\nLista de trabajadores\n")
            for trabajador in  enumerate(Trabajador.lista_trabajadores, start=1):
                print(f"ID: {trabajador.id_trabajador}")
                print(f"Nombre: {trabajador.nombre_trabajador}")
                print(f"Primer Apellido: {trabajador.apellido_1}")
                print(f"Segundo Apellido: {trabajador.apellido_2}")
                print(f"Horas Semanales: {trabajador.horas_semanales}")
                print(f"Coste Hora: {trabajador.coste_hora}")
                print(f"Puesto de trabajo: {trabajador.puesto_trabajo}")
                print(f"Tareas Asignadas: {trabajador.contador_tareas}")
                print(f"Email: {trabajador.email}")
                print()


    #Definimos una funcion que permita al usuario eliminar un trabajador en funcion de su id
    @classmethod
    def eliminar_trabajador(self):
        if len(Trabajador.llista_tranajadores)==0:
            print("\nNo hay trabajadores registrados\n")
        else:
            print("Estos son los trabajadores en el sistema actualmente\n")
            Trabajador.listar_trabajadores()
            id_eliminar = int(input("\nEscriba el ID del trabajador que desea dar de eliminar: "))
            if id_eliminar in Trabajador.diccionario_trabajadores:
                del Trabajador.lista_trabajadores.index[id_eliminar]
            else:
                print("No existe un trabajador con ese ID")

    #definimos una funcion que permita al usuario modificar los datos de un trabajador
    @classmethod
    def modificar_datos_trabajador(self):
        if len(Trabajador.diccionario_trabajadores)==0:
            print("\nNo hay trabajadores registrados\n")
        else:
            print("Estos son los trabajadores en el sistema actualmente\n")
            Trabajador.listar_trabajadores()
            id_modificar = int(input("\nEscriba el ID del trabajador que desea modificar: "))
            trabajador = Trabajador.lista_trabajadores.index[id_modificar]
            while True:
                print("\nLos campos que puede cambiar son los siguientes")
                print("\t1-nombre_trabajador: " + str(trabajador.nombre_trabajador))
                print("\t2-apellido_1: " + str(trabajador.apellido_1))
                print("\t3-Apellido_2: " + str(trabajador.apellido_2))
                print("\t4-horas_semanalaes: " + str(trabajador.horas_semanales))
                print("\t5-coste_hora: " + str(trabajador.coste_hora))
                print("\t6-puesto_trabajo: " + str(trabajador.puesto_trabajo))
                print("\t7Nº Tareas asignadas: " + str(trabajador.contador_tareas))
                print("\t8-email: " + str(trabajador.email))
                dato_a_modificar = str(input("\nElija el parametro que desea modificar: "))
                nuevo_valor = str(input("Introduce el nuevo valor: ")) 
                setattr(trabajador, dato_a_modificar,  nuevo_valor)
                print(f"El nuevo valor del dato: " + dato_a_modificar + " es " + nuevo_valor)
                continuar = input("\nDesea seguir modificando? s/n: ")
                if continuar.lower() == 'n':
                    print("Volviendo  al menu de gestion de trabajadores...")
                    Menu.limpiar_pantalla()