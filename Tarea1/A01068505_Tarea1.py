
# Tarea 1: Red de Hopfield - Módulo 2 - Inteligencia Artificial
# Hecho por: Sergio Eduardo Gutiérrez Torres
# Matrícula: A01068505
# Fecha: 21/09/2026
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

def funcionF(vector):
    for i in range(len(vector)):
        if vector[i] > 0:
            vector[i] = 1
        elif vector[i] < 0:
            vector[i] = -1

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


# ----- MAIN -----

print("\n")
print("Tarea 1: Red de Hopfield - Módulo 2 - Inteligencia Artificial")
print("Hecho por: Sergio Eduardo Gutiérrez Torres")
print("Profesor: Adolfo Centeno Tellez")

# Variables iniciales
print("\nVariables iniciales:")
x1 = [1,1,1,-1]
x2 = [-1,-1,-1,1]

print(" - Vector x1:")
printVector(x1)
print(" - Vector x2:")
printVector(x2)

# Primer paso
print("\nPrimer paso: Producto exterior de x1 y x2")
x1Xx1 = productoExterior(x1)
x2Xx2 = productoExterior(x2)

print(" - Matriz x1Xx1:")
printMatriz(x1Xx1)
print(" - Matriz x2Xx2:")
printMatriz(x2Xx2)

# Segundo paso
print("\n - Segundo paso: Suma de las matrices:")
suma = sumaDeMatrices(x1Xx1,x2Xx2)
printMatriz(suma)

# Tercer paso
print("\n - Tercer paso: Diagonal de 0s, matriz t:")
t = diagonal0(suma)
printMatriz(t)

# Cuarto paso
print("\n - Cuarto paso: Hallar el más parecido a A")

A = [[1,1,1,-1], [-1,-1,-1,-1]]

for i in range(len(A)):
    print("\n",i+1,". Hallando el más parecido a A",A[i],":")
    encontrado = False
    u0 = A[i]
    contador = 0

    while not encontrado:
        contador += 1
        u0Xt = vectorXmatriz(u0,t)
        print("Vector u",contador-1,"* t:")
        printVector(u0Xt)

        u1 = funcionF(u0Xt)
        print("Vector u",contador,":")
        printVector(u1)

        if u1 == u0:
            encontrado = True
            print("-> El vector más parecido a A",A[i],"se encontró en",contador,"iteraciones.")
        else:
            print("-> El vector u1 no es igual a u0, se repite el proceso.")
            u0 = u1
