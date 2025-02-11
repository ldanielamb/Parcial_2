# Desarrollar un programa que dadas dos listas determine qué elemento tiene la primera lista que no tenga la segunda
lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = [1,2,3,4,5,6,7,8]
def diferencia (l1,l2):
    diferencia = set(l1) - set(l2)
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

# Desarrollaar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el número que queda en la mitad del arreglo después de ser ordenado

             


