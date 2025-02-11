# Laura Daniela Marin Barragan 
# Parcial 

# Punto número uno
# Desarrollar un programa que determine si en una lista no existen elementos repetidos

mi_lst = ["hola", "hola", 5, 78, True]
mi_lst_2 = ["hola","no","tengo"]
def tiene_repeticiones(l):
    if len(l) != len(set(l)): #Con el set, que no permite elementos repetidos, se verifica si son o no iguales
        print("La lista tiene elementos repetidos")
    else:
        print("La lista no tiene elementos repetidos")

print("\n------------------Programa que evalúa si en una lista existen elementos repetidos------------------")
tiene_repeticiones(mi_lst)
tiene_repeticiones(mi_lst_2)


# Punto número dos
# Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe, debe imprimirla y si no existe, debe imprimir "no existe"
mi_lista_2 = ["hola","tos","sky","hey"]
mi_lista_3 = ["tos","sky","hey"]
def contiene_dos_o_mas_vocales(cadena):
    vocales = "AEIOUaeiou"
    contador = sum(1 for letra in cadena if letra in vocales) #Va a generar un 1 si la condición se cumple
    return contador >= 2

def eval(ls):
    evaluar = [cadena for cadena in ls if contiene_dos_o_mas_vocales(cadena)]
    if evaluar:
        for cadena in evaluar:
            print(cadena)
    else:
        print("No existe")
print("\n---------------------Programa que evalúa si en una lista hay cadenas con dos o más vocales-------------------------")
eval(mi_lista_2)
eval(mi_lista_3)


# Desarrollar un programa que dadas dos listas determine qué elemento tiene la primera lista que no tenga la segunda



#Desarrollar un algoritmo que calcule el promedio de matrices de reales

A = [
    [1,2],
    [3,4]
]
B = [
    [5,6],
    [7,8]
]
suma = [[A[i][j] + B[i][j] for j in range (len(A[0]))] for i in range (len(A))]
long_1 = len(A) * len(A[0]) #Me da el tamaño de la matriz
long_2 = len(B) * len(B[0])

    #Es el método de compresión para:
    #l = [], nueva lista vacía
    #for i i range (len(A)), que recorre la primera matriz
        #for j in range (len(A[0])), que recorre las columnas
        #l.append(A[i][j] + B[i][j]), que almacena la suma de cada elemento correspondiente en la nueva lista
promA = [[elemento / long_1 for elemento in fila] for fila in A]
promB = [[elemento / long_2 for elemento in fila] for fila in B]

print("\n---------------------Programa que devuelve el promedio de dos matrices-------------------------")
print(A)
print(B)
print(promA)
print(promB)

#Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el número que queda en la mitad del arreglo después de ser ordenado
promA = [[elemento //2 for elemento in fila] for fila in A]
promB = [[elemento //2 for elemento in fila] for fila in B]
