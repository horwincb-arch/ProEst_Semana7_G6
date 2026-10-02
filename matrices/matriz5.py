"""
Dada una matriz de Identidad nxn
mostrar en color azul solo la diagonal de 1
"""
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

print("La matriz de identidad es: ")
for fila in matriz:
    print(fila)