
from fun_recu import *


estudiantes=["Ana", "Bruno", "Carla", "Diego"]
calificasiones=[[9,8,10],#ana
                [6,7,8],#Bruno
                [10,10,9],#Carla
                [7,6,5]#diego
                ]
materias=["matemática","historia","biología"]
list_menu=["----------------menu-------------------","1)Mostrar la lista de estudiantes y la matriz de calificaciones",
       "2)Ordenar a los estudiantes de mayor a menor según su promedio general",
       "3)Buscar un estudiante por nombre y mostrar sus calificaciones.",
       "4)Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece",
       "5)salir"," "]#las opciones del menu
rangos_menu=[1,2,3,4,5]


#Menu 
estado_menu=0
while estado_menu==0:
 funsion_print_lista(list_menu)
 opcion=int(input("Elegir una opcion del menu entre (1 - 5): "))
 while opcion>5 or opcion<1:
     print("Opcion no valida " )
     opcion=int(input("Elegir una opcion del menu entre (1 - 5): "))
 if opcion==1:
    Mostrar_estudiantes_materia_calificaciones(estudiantes,calificasiones,materias)
 elif opcion==2:
   ordenar_estudiantes_mayor_a_menor_promedio(estudiantes,calificasiones,promedio_lista(calificasiones))
 elif opcion==3:
    Buscar_estudiante_por_nombre_calificaciones(estudiantes,calificasiones)
 elif opcion==4:
    Buscar_calificación_matriz_mostrar_estudiante_materia(estudiantes,calificasiones,materias)
 elif opcion==5:
    estado_menu=1