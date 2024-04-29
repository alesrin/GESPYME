
def convertir_listastr_a_lista_python():
    #estas 2 lineas cogen una lista escrita manualmente por el usuario y la convierten a una lista de python
    lista_trabajadores= input("\n¿Que trabajador o trabajadores quiere asignar a esta tarea?: \n") # tiene que intrdoducir una lista en plan Rafa,Juan,Alejandra
    lista_trabajadores= lista_trabajadores.split(",") 

    return lista_trabajadores
   

def hacer_lista_de_trabajadores_asignados_a_la_tarea(trabajadores_contratados):
   #AQUI SE ASIGNA A LOS TRABAJADORES A LA TAREA:

  #estas 3 lineas son para que el manager sepa a que trabajadores puede asignar la tarea
   print("Los trabajadores contratados son:") 
   for trabajador in trabajadores_contratados:
      print("-"+" "+trabajador)

   lista_trabajadores = convertir_listastr_a_lista_python() #poner esta función debería ser lo mismo que escribir las 3 lineas de abajo

   #estas 2 lineas cogen una lista escrita manualmente por el usuario y la convierten a una lista de python
   #lista_trabajadores= input("\n¿Que trabajador o trabajadores quiere asignar a esta tarea?: \n") # tiene que intrdoducir una lista en plan Rafa,Juan,Alejandra
   #lista_trabajadores= lista_trabajadores.split(",") 

   print()# He añadido este print para que no salga todo tan junto

   #Este bucle es para que no te asigne trabajadores que no estan contratados
   #Para salir de este bucle y continuar probando este programa copia y pega esto: Rafa,Juan,Alejandra

   while True:

       trabajadores_que_no_se_han_encontrado = 0 #variable nueva auxiliar, se convierte en 1 si ha habido algún trabajador en la lista que ha dado el usuario que no estaba en la lista de contratados
       for trabajador in lista_trabajadores:

           if trabajador in trabajadores_contratados:#Te comprueba si el trabajador esta en la lista de contratados y si no esta te lo dice
               pass #No quería que añadiese nada, pero si pongo break aquí no funciona
           else:
               print (f"No se ha encontrado al trabajador {trabajador} en la lista de trabajadores contratados")
               trabajadores_que_no_se_han_encontrado = 1
            
       if trabajadores_que_no_se_han_encontrado == 0:
           print(f"\nLos trabajadores que ha asignado a esta tarea son: \n{lista_trabajadores}") #Si todo sale bien te aparece esto
           break

       else: #si ha habido algún error te pide repetir
           print("\nNo se ha encontrado a uno o más de los trabajadores que ha asignado a esta tarea, por favor, vuelva a introducir")
           lista_trabajadores= input("¿Que trabajador o trabajadores quiere asignar a esta tarea?: \n") # tiene que intrdoducir una lista en plan Rafa,Juan,Alejandra
           lista_trabajadores= lista_trabajadores.split(",")
           print() # He añadido este print para que no salga todo tan junto



   #SIN TERMINAR, NO SE PORQUE, EL BUCLE WHILE HACE COMO QUE LOS IF NO EXISTIESEN.


   while True:

       #Necesito esta variable nueva ,entrada para poder hacer este bucle>
       entrada = str(input(f"\nSi quiere modificar esta lista escriba el input añadir o eliminar. Si ha terminado escriba el input end. (añadir / eliminar / end): "))

       if entrada.lower() == "añadir": #FALTA TERMINAR EL CÓDIGO DE ESTE  if

           print() #Para que no salga todo tan pegado

           print("La lista de trabajadores contratados")
           for trabajador in trabajadores_contratados:#Para que nos diga la lista de trabajadores contratados de la que puedes elegir
             print("-"+" "+trabajador)

           print("\nLa lista de trabajadores asignados a esta tarea")
           for trabajador in lista_trabajadores:#Para que nos diga que trabajadores ya hemos asignado a esta tarea
             print("-"+" "+trabajador)

           lista_trabajadores_añadidos = convertir_listastr_a_lista_python()#poner esta función debería ser lo mismo que escribir las 2  lineas de abajo
           #lista_trabajadores_añadidos = input("\n¿Que otro trabajador o trabajadores quiere asignar a esta tarea?: \n")#Incluyo esta variable nueva para poder añadir los nuevos trabajadores
           #lista_trabajadores_añadidos = lista_trabajadores_añadidos.split(",") #Incluyo esta variable nueva para poder añadir los nuevos trabajadores

           for trabajador in lista_trabajadores_añadidos: #Este bucle for comprueba que todos los trabajadores que el usuario quiere añadir estan en la lista de contratados
              if trabajador in trabajadores_contratados:
                 pass
           
              else:
                 print(f"\nEl trabajador {trabajador} que ha añadido no se encuentra en la lista de contratados")
                 lista_trabajadores_añadidos.remove(trabajador)
        
           lista_trabajadores_añadidos_0 = [] #Variable nueva auxiliar
           for trabajador in lista_trabajadores_añadidos: #Este bucle for comprueba que todos los trabajadores que el usuario quiere añadir NO estan repetidos (que no te sale una lista de trabajadores asignados a esta tarea así [Alejandra,Juan, Alejandra,Alejandra,Alejandra])
              if trabajador not in lista_trabajadores_añadidos_0:
                 lista_trabajadores_añadidos_0.append(trabajador)
           
           lista_trabajadores_añadidos = lista_trabajadores_añadidos_0
        

           lista_trabajadores = lista_trabajadores + lista_trabajadores_añadidos
           print(f"\nLa lista de trabajadores ha sido actualizada:{lista_trabajadores}")

       elif entrada.lower()  == "eliminar":  #FALTA TERMINAR EL CÓDIGO DE ESTE elif

           print()
           print("La lista de trabajadores contratados")
           for trabajador in trabajadores_contratados:#Para que nos diga la lista de trabajadores contratados de la que puedes elegir
             print("-"+" "+trabajador)

           print("\nLa lista de trabajadores asignados a esta tarea")
           for trabajador in lista_trabajadores:#Para que nos diga que trabajadores ya hemos asignado a esta tarea
             print("-"+" "+trabajador)

           #Aquí no he podido usar la función convertir_listastr_a_lista_python() porque pregunta "¿Que trabajador o trabajadores quiere AGREGAR a esta tarea?" y ahora estamos eliminando
           lista_trabajadores_eliminados = input("\n¿Que trabajador o trabajadores quiere eliminar de esta tarea?: \n")#Incluyo esta variable nueva para poder añadir los nuevos trabajadores
           lista_trabajadores_eliminados = lista_trabajadores_eliminados.split(",") #Incluyo esta variable nueva para poder eliminar trabajadores


           for trabajador in lista_trabajadores_eliminados:

               if len(lista_trabajadores)>1:#Para que no te pueda dejar con una lista de trabajores asignados a la tarea vacia. Es decir, que haya un trabajador mínimo asignado a la tarea.
               
                  if trabajador in lista_trabajadores: #Para que no te pueda quitar de la lista de trabajadores asignados un trabajador que no esta (si lo intenta te da error)
                   lista_trabajadores.remove(trabajador)
                   print(f"El trabajador {trabajador} se ha eliminado")
                  else:
                   print(f"\nEl trabajador que se ha querido eliminar {trabajador} no esta en la lista de tareas")

               else:
                  print(f"\nSe han eliminado todos los trabajadores que ha indicado excepto {lista_trabajadores}, ya que si no, no habría ningún trabajador asignado a esta tarea")
            
            
        
           print(f"\nLa lista de trabajadores ha sido actualizada:{lista_trabajadores}")
        
       
       elif entrada.lower() == "end":
           break

       else:
           print("No ha introducido ninguno de los inputs validos, por favor, inténtelo otra vez.")

   print(f"\nLos trabajadores que ha asignado a esta tarea son: \n{lista_trabajadores}\n")
   return lista_trabajadores 
   # con esta última linea le estoy diciendo a programa que si pongo variable_cualquiera = hacer_lista_de_trabajadores_asignados_a_la_tarea(trabajadores_contratados)
   # me entienda que variable_cualquiera = lista_trabajadores (específicamente, la lista_trabajadores  del final del programa)

#EJECUTA EL CÓDIGO COMENTADO EN ESTAS 2 LINEAS PARA COMPROBAR QUE FUNCIONA TODO EL CÓDIGO EN ESTE ARCHIVO
""" #He necesitado crear esta variable nueva, trabajadores_contratados. Es necesario saber que trabajadores tenemos contratados antes de decidir a donde los asignamos.
trabajadores_contratados =["Rafa","Juan", "Alejandra","Sandra","Lucia"] # Esto es un ejemplo, tenemos que conseguir que se haga esta lista automaticamente en el bloque de codigo de los trabajadores que tiene hecho David
hacer_lista_de_trabajadores_asignados_a_la_tarea(trabajadores_contratados) """