def ordenar_fila(matriz, numero_fila):
    """
    Ordena una fila específica de una matriz bidimensional en orden ascendente.

    Args:
        matriz (list): La matriz bidimensional.
        numero_fila (int): El índice de la fila que se va a ordenar.
    """

    fila_a_ordenar = matriz[numero_fila]
    fila_ordenada = sorted(fila_a_ordenar)  # Usando la función sorted de Python
    matriz[numero_fila] = fila_ordenada

# Ejemplo de uso
matriz = [[35, 45, 55], [20, 30, 40], [80, 90, 95]]
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)