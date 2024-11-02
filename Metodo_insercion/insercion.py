# Lista de números desordenados
numeros = [4, 1, 3, 10, 5, 7, 2, 9, 6, 8]

# Método de Ordenamiento de Inserción
def ordenamiento_insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Mover los elementos de arr[0..i-1] que son mayores que clave
        # a una posición adelante de su posición actual
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

# Ordenar la lista
ordenamiento_insercion(numeros)

# Mostrar la lista ordenada
print("Lista ordenada:", numeros)
