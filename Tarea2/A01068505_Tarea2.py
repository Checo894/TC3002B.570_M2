
# Tarea 2: Red de Hopfield - Módulo 2 - Inteligencia Artificial
# Hecho por: Sergio Eduardo Gutiérrez Torres
# Matrícula: A01068505
# Fecha: 28/09/2026
# Profesor: Adolfo Centeno Tellez


# ----- FUNCIONES -----

def productoExterior(vector):
    matriz = []

    for i in vector:
        fila = []

        for j in vector:
            fila.append(i * j)

        matriz.append(fila)

    return matriz

def sumaDeMatrices(matriz1, matriz2):
    suma = []

    for i in range(len(matriz1)):
        fila = []

        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])

        suma.append(fila)

    return suma

def diagonal0 (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):

            if i == j:
                matriz[i][j] = 0

    return matriz

def vectorXmatriz(vector, matriz):
    resultado = []

    for j in range(len(matriz[0])):
        suma = 0

        for i in range(len(vector)):
            suma += vector[i] * matriz[i][j]

        resultado.append(suma)

    return resultado

def funcionF(vector, estadoAnterior):
    for i in range(len(vector)):
        if vector[i] > 0:
            vector[i] = 1
        elif vector[i] < 0:
            vector[i] = -1
        else:
            vector[i] = estadoAnterior[i]

    return vector

def printMatriz(matriz):
    print("[")

    for i in range(len(matriz)):
        print("\t[", end="")

        for j in range(len(matriz[0])):
            print(matriz[i][j], end="")

            if j < len(matriz[0]) - 1:
                print(", ", end="")

        print("],")

    print("]")

def printVector(vector):
    print("[", end="")

    for i in range(len(vector)):
        print(vector[i], end="")

        if i < len(vector) - 1:
            print(", ", end="")

    print("]")

def leerMatrizTXT(nombre):
    matriz = []

    archivo = open(nombre, "r")

    for linea in archivo:
        fila = []

        numeros = linea.split()

        for numero in numeros:
            fila.append(int(numero))

        matriz.append(fila)

    archivo.close()

    return matriz

def matrizAVector(matriz):
    vector = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            vector.append(matriz[i][j])

    return vector


def vectorAMatriz(vector, filas, columnas):
    matriz = []
    posicion = 0

    for i in range(filas):
        fila = []

        for j in range(columnas):
            fila.append(vector[posicion])
            posicion += 1

        matriz.append(fila)

    return matriz


# ----- MAIN -----

print("\n")
print("Tarea 2: Red de Hopfield - Módulo 2 - Inteligencia Artificial")
print("Hecho por: Sergio Eduardo Gutiérrez Torres")
print("Profesor: Adolfo Centeno Tellez")

# Variables iniciales
print("\n>> Lectura de archivos:")

matrizA = leerMatrizTXT("A.txt")
print(" - Matriz A:")
printMatriz(matrizA)
x1 = matrizAVector(matrizA)

matrizE = leerMatrizTXT("E.txt")
print(" - Matriz E:")
printMatriz(matrizE)
x2 = matrizAVector(matrizE)

matrizI = leerMatrizTXT("I.txt")
print(" - Matriz I:")
printMatriz(matrizI)
x3 = matrizAVector(matrizI)

# print("\nNúmero de slots:", len(x1))
# print("\nNúmero de slots:", len(x2))
# print("\nNúmero de slots:", len(x3))

patrones = [x1, x2, x3]
nombresPatrones = ["A", "E", "I"]

# Primer paso
print("\n>> Primer paso: Productos exteriores")

productos = []

for i in range(len(patrones)):
    producto = productoExterior(patrones[i])
    productos.append(producto)

    print(" - Producto exterior de", nombresPatrones[i], "calculado")
    # printMatriz(producto)

# Segundo paso
print("\n>> Segundo paso: Suma de las matrices")
suma = productos[0]

for i in range(1, len(productos)):
    suma = sumaDeMatrices(suma, productos[i])
    # printMatriz(suma)

print("Matrices sumadas correctamente.")

# Tercer paso
print("\n>> Tercer paso: Diagonal de 0s, matriz t:")
t = diagonal0(suma)
print("Matriz 0s creada correctamente.")
# printMatriz(t)

# Cuarto paso
print("\n>> Cuarto paso: Reconocimiento de patrones de prueba:")

archivosPrueba = [
    ("A", "pruebaA.txt"),
    ("E", "pruebaE.txt"),
    ("I", "pruebaI.txt")
]

for nombrePrueba, archivoPrueba in archivosPrueba:

    print(" -- Probando patrón:", nombrePrueba,"--")

    prueba = leerMatrizTXT(archivoPrueba)

    print("-> Matriz de prueba:")
    printMatriz(prueba)

    u0 = matrizAVector(prueba)

    encontrado = False
    contador = 0
    maxIteraciones = 100

    while not encontrado and contador < maxIteraciones:

        contador += 1

        u0Xt = vectorXmatriz(u0, t)

        u1 = funcionF(u0Xt, u0)

        print(" - Iteración", contador,"...")

        if u1 == u0:
            encontrado = True
        else:
            u0 = u1

    if encontrado:
        reconocido = False

        for i in range(len(patrones)):
            if u1 == patrones[i]:
                print("-> Patrón reconocido:", nombresPatrones[i])
                print("-> Se encontró en", contador, "iteraciones.")
                reconocido = True

        if not reconocido:
            print("-> La red llegó a un estado estable.")
            print("-> El resultado no coincide con ningún patrón almacenado.")

    else:
        print("-> No se encontró un estado estable.")

    resultado = vectorAMatriz(u1, 8, 5)

    print("-> Resultado de la red:")
    printMatriz(resultado)
    print()
