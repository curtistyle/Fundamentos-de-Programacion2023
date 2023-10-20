"""
Se leen los nombres, edades y alquileres que pagan los inquilinos de un edificio. Se pide calcular: 
    a- Total recaudado por el consorcio en concepto de alquileres. 
    b- Nombre del inquilino que paga el alquiler más caro. 
    c- Nombre y edad del inquilino más viejo. 
    d- Nombre y edad del inquilino más joven.
"""

tipo_inquilino = { 'nombre': str, 'edad' : int, 'alquiler' : float}

def insertar():
    alquilino = tipo_inquilino
    alquilino['nombre'] = int(input("Ingrese el nombre del alquilino: "))
    alquilino['edad'] = input("Ingrese la edad del alquilino: ")
    alquilino['alquiler'] = float(input("Ingrese  el alquiler: "))
    return alquilino

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        stock = insertar()  
        lista[indice] = stock
        opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0

def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] > mayor:
            mayor = lista[stock][campo]
            posicion = stock
    return posicion

def menor(lista : list, tamanio : int, campo : str):
    menor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] < menor:
            menor = lista[stock][campo]
            posicion = stock
    return posicion

def mostrar(lista : list, posicion : int):
    print(lista[posicion]['nombre'])
    print(lista[posicion]['edad'])
    print(lista[posicion]['alquiler'])
    print()

def total_acumulado(lista : list, tamanio : int, campo : str):
    acumulador = 0
    for alquilino in range(0, tamanio):
        acumulador += lista[alquilino][campo] 
    return acumulador


edificio = [0,0,0,0,0,0]

edificio = [
    { 'nombre': "Laura Díaz", 'edad' : 23, 'alquiler' : 3400 },
    { 'nombre': "Ana María Sánchez", 'edad' : 25, 'alquiler' : 2400 },
    { 'nombre': "Miguel Rodríguez", 'edad' : 18, 'alquiler' : 4300 },
    { 'nombre': "Elena Martínez", 'edad' : 45, 'alquiler' : 5000 },
    { 'nombre': "Sandra Rodríguez", 'edad' : 40, 'alquiler' : 1200 },
    { 'nombre': "Marta Díaz", 'edad' : 30, 'alquiler' : 4200 },
    
]

ultimo = len(edificio)

# TODO: a- Total recaudado por el consorcio en concepto de alquileres. 

total = total_acumulado(edificio, ultimo, 'alquiler')
print(f"El total recaudado por el consorcio es: ${total:.2f}", end="\n\n")

# TODO: b- Nombre del inquilino que paga el alquiler más caro.

inquilino = mayor(edificio, ultimo, 'alquiler')
print(f"El inquilino que paga el alquiler mas caro es: {edificio[inquilino]['nombre']}.", end="\n\n")

# TODO: c- Nombre y edad del inquilino más viejo. 

inquilino = mayor(edificio, ultimo, 'edad')
print("El inquilino mas viejo es: ")
print(f" - Nombre: {edificio[inquilino]['nombre']}")
print(f" - Edad: {edificio[inquilino]['edad']}", end="\n\n")

# TODO: d- Nombre y edad del inquilino más joven.

inquilino = menor(edificio, ultimo, 'edad')
print("El inquilino mas joven es: ")
print(f" - Nombre: {edificio[inquilino]['nombre']}")
print(f" - Edad: {edificio[inquilino]['edad']}", end="\n\n")