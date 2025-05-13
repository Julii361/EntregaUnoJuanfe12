#Programa para crear LISTAS DE TAREAS en PYTHON

#Requsitos:
#1. Debo permitir que el usuario interactue con la app
# hasta que no elija SALIR

#2. Debo permitir: 
# crear una tarea
# consultar todas las tareas o pendientes
# modificar una tarea especifica
# eliminar una tarea especifica

#3. Una tarea debe recoger la siguiente información:
#id
#descripcion
#dia de la semana
#hora
#fecha

#4. Modifcar y eliminar se deben hacer por el ID

#5. El proyecto debe estar desplegado en GITHUB


#------------------------------------------------
opcion=None

print("TAREAS APP")
print("1. Crear una tarea")
print("2. Consultar una tarea")
print("3. Modificar una tarea")
print("4. Eliminar una tarea")
print("5. SALIR")

ListaTareas=[]
while opcion != 5:
    tarea={}
    opcion = int(input("Digita una opcion por favor: "))
    if opcion == 1:
     print("creando una tarea...")
     tarea ['id']=input("digita el id de la tarea:")
     tarea ['descripcion']=input("Digita una descripción:")
     tarea ['diaSemana']=input("Que dia es esta tarea")
     tarea ['hora'] = input("A que horas es la tarea")
     tarea ['fecha'] = input("Que fecha es el evento")
     ListaTareas.append(tarea)
    elif opcion == 2:
        print("consultando una tarea ")
        print(ListaTareas)
    elif opcion == 3:
        print("modificando una tarea ") 
    elif opcion == 4:
        print("eliminando tarea ")
    elif opcion == 5:
        print("saliendo")
        break
    else:
        print("Opcion invalida")


