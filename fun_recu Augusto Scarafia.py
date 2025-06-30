def funsion_print_lista(lista:list):
    for i in range(len(lista)):
            print(lista[i] )
            
def funsion_input_numero_valido(listaR:list)->int :
 #for i in range(len(listaR)):
    #print("las opsiones son:",listaR[i],end=" ")
 #opcion=int(input("Elegir una opcion del menu entre (1 - 5): "))
 valido=0
 while valido==0:
  for i in range(len(listaR)):
    print("las opsiones son:",listaR[i],end=" ")
  opcion=int(input("Elegir una opcion del menu entre (1 - 5): "))
  if opcion is listaR:
    for i in range(len(listaR)):
     opcion=listaR[i]
     valido=opcion
     valido=int
  else:
    print("Opcion no valida " )
  #while opcion>5 or opcion<1:
    
 return valido


def funsion_print_matriz(lista:list):
    for i in range(len(lista)):
         for j in range(len(lista[i])):
              print(lista[i][j])

def Mostrar_estudiantes_materia_calificaciones(lista1:list , lista2:list, lista3:list):
 print("Mostrar:estudiantes, materia y calificaciones.")
 for i in range(len(lista2)):
     print(lista1[i],end="| " )
     for j in range(len(lista2[i])):
          print(lista3[j],"| nota",lista2[i][j], end="| ") 
     print("")
 input("")

def promedio_lista(listaN:list)->list:
     lista_promedio=[]
     for i in range(len(listaN)):
         suma_columna = 0
         for j in range(len(listaN[i])):
             suma_columna += listaN[i][j]
             promedio=suma_columna/len(listaN[i])
         lista_promedio .append(promedio)
     return lista_promedio

def ordenar_estudiantes_mayor_a_menor_promedio(listaA:list,listaN:list,listaP:list):
    print("Ordenar estudiantes de mayor a menor según su promedio ")
    for i in range(0, len(listaP)-1):
      for j in range(0, len(listaP,)-i-1):
         if listaP[j]  < listaP[j+1] :
             listaP[j], listaP[j+1] = listaP[j+1], listaP[j]
             listaA[j],listaA[j+1]=listaA[j+1],listaA[j]
             listaN[j],listaN[j+1]=listaN[j+1],listaN[j]
    for i in range(len(listaP)):
      print("->",listaA[i],end=" | ") 
      print("promedio:",listaP[i],end="|") 
      print("--->",listaN[i])
    input("")

def Buscar_estudiante_por_nombre_calificaciones(listaA:list,listaN:list):
  contador=0
  while contador==0:
   Alumno=input("elegir estudiante: ")
   if Alumno in listaA:
    for i in range(len(listaA)):
     if Alumno==listaA[i]:
         print("->",listaA[i]," sus notas son:",end=" | ")
         for j in range(len(listaN[i])):
             print(listaN[i][j],end="| ")
         contador=1
   else: 
     print("error: no es un estudiante")
  input()

def Buscar_calificación_matriz_mostrar_estudiante_materia(listaA:list,listaN:list,listaM:list):
 contador=0
 while contador==0 :
      numero_valido=0
      print("Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece")
      Nota=int(input("Buscar calificación: "))
      for i in range(len(listaN)):
         for j in range(len(listaN[i])):
           if Nota==listaN[i][j]:
             print("encotrada:",listaN[i][j],"estudiante es:",listaA[i],"la materia es:",listaM[j])
             contador=1
             numero_valido+=1
      if numero_valido==0:
       print("error: ningun estudiante tiene esta calificación")
       numero_valido+=1
      input()