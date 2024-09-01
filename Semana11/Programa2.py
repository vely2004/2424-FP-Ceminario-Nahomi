# Ordenación de arreglo Multidimencional
matriz = [
    [8, 10, 6],
    [3, 1, 2 ],
    [4, 7,11 ]
]

# Función para ordenar una fila específica de manera ascendente utilizando Bubble Sort
def ordenar_fila(matriz,fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1],matriz[fila][j]  # Intercambiar elementos
# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)
# Ordenar fila especifíca de la matriz
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)
# Mostrar la matriz con la fila específica ordenada
print("\nMatriz después de ordenar la fila 1:")
for fila in matriz:
    print(fila)