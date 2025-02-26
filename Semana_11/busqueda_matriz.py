def buscar_valor(matriz, valor_buscado):
    """
    Busca un valor en una matriz bidimensional y muestra su posición si se encuentra.

    Args:
        matriz (list): La matriz bidimensional en la que buscar.
        valor_buscado (int): El valor que se va a buscar.
    """

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_buscado:
                print(f"Valor {valor_buscado} encontrado en la posición ({i}, {j})")
                return
    print(f"Valor {valor_buscado} no encontrado en la matriz")

# Ejemplo de uso
matriz = [[60, 70, 80], [90, 100, 110], [120, 130, 140]]
valor_a_buscar = 90

buscar_valor(matriz, valor_a_buscar)