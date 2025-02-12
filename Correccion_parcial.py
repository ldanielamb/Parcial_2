# Desarrollar un programa que dadas dos listas determine qué elemento tiene la primera lista que no tenga la segunda
def diferencia (l1,l2):
    if len(set(l1)) == len(set(l2)):
        diferencia = set(l1) - set(l2)
    else: 
        diferencia = set(l2) - set(l1)
    return list(diferencia)
print("\n----------------Programa que determina el elemento que falta en una lista----------------")
entrada = list(input("Digite los elementos de su lista separado por espacios: ").split())
entrada_2 = list(input("Digite los elementos de su lista separado por espacios: ").split())
print(f"La diferencia entre las dos listas es: {diferencia(entrada,entrada_2)}")

# Desarrollar un algoritmo que calcule el promedio de arreglos de reales
def es_numero(entrada):
    l = []
    for elemento in entrada:
        if elemento.isnumeric() == True:
            num = int(elemento)
            l.append(num)
    return l

print("\n----------------Programa que calcula el promedio de arreglos de reales----------------")
entrada = list(input("Digite su lista separada con espacios: ").split())
entrada_2 = list(input("Digite su lista separada por espacios: ").split())
es_numero(entrada_2)
def calcular_promedio(p1,p2):
    prom = sum(p1+p2) / (len(p1)+len(p2))
    return prom
print(f"El promedio es: {calcular_promedio(es_numero(entrada), es_numero(entrada_2))}")

# Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el número que queda en la mitad del arreglo después de ser ordenado.
def es_int(lista):
    l = []
    for elemento in lista:
        if elemento.isnumeric():
            l.append(int(elemento))
    return l
def orden(lista):
    ordenado = sorted(lista)
    return ordenado
def mediana(lista):
    x = len(lista) // 2
    return lista[x]
print("\n----------------Programa que calcula la mediana de arreglo de enteros----------------")
entrada = list(input("Digite su lista separada con espacios: ").split())
print (f"La mediana es: {mediana(orden(es_int(entrada)))}")


#Suma y mediana de matrices

A = [
    [1,2],
    [3,4]
]
B = [
    [5,6],
    [7,8]
]
suma = [[A[i][j] + B[i][j] for j in range (len(A[0]))] for i in range (len(A))]
long = len(A) * len(A[0])
promA = [[elemento / long for elemento in fila] for fila in A]

print("\n---------------------Programa que devuelve el promedio de dos matrices-------------------------")
print("La matriz 1 es: ")
for fila in A:
    print(fila)
print("La matriz 2 es: ")
for fila in B:
    print(fila)
print("El promedio es: ")
for A in promA:
    print(A)

#
def ingresar_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

#print("Su matriz es: ")
#for f in ingresar_matriz():
    print(f)




             


