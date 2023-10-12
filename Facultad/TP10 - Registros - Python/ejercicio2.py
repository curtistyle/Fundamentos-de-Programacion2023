"""Supongamos que definimos un arreglo de 1000 pólizas de seguro de vida, cada una posee Nº de 
póliza, nombre del asegurado, dirección, año de nacimiento, cantidad asegurada y cuota. Codificar 
un algoritmo que permita ingresar pólizas en la estructura anterior. Además, se pide: 

    - Mostrar los nombre y direcciones de las personas que cumplen 70 años en el 
    corriente año. 
    - Mostrar las personas cuya cuota es menor a $ 30.00. 
    - Mostrar las personas que tengan asegurada un monto mayor a $100.000 
      ordenados alfabéticamente 
    - Mostrar si Pedro Fernández está asegurado en la compañía."""

tipo_poliza = {
    'numero': int,
    'nombre': str,
    'direccion': str,
    'nacimiento': str,
    'monto': float,
    'cuota': float
}

def insertar_poliza(indice : int):
    poliza = tipo_poliza
    poliza['numero'] = indice
    poliza['nombre'] = input("Ingrese el Nombre: ")
    poliza['direccion'] = input("Ingrese la Direccion: ")
    poliza['nacimiento'] = int(input("Ingrese el anio de Nacimiento: "))
    poliza['monto'] = float(input("Ingrese la cantidad asegurada: "))
    poliza['cuota'] = float(input("Ingrese la cuota: "))
    return poliza

def cargar_polizas(polizas : list, tamanio : int):
    ultimo = 0
    opcion = input("Ingrese s para cargar una poliza:  ")
    while (((opcion == 's') or (opcion == 'S')) and (ultimo < tamanio)):
        polizas[ultimo] = insertar_poliza(ultimo)
        ultimo += 1
        print()
        if ultimo < tamanio:
            opcion = input("Ingrese 's' para cargar una poliza: ")
    return ultimo

def mayor_edad(polizas : list, tamanio : int):
    for poliza in range(0, tamanio):
        if (2023 - polizas[poliza]['nacimiento']) > 70:
            print("Nombre: ", polizas[poliza]['nombre'])
            print("Direccion: ",polizas[poliza]['direccion'])
        

def menor_cuota(polizas : list, tamanio : int):
    for poliza in range(0, tamanio):
       if (polizas[poliza]['cuota']) < 30:
            print("Nombre: ", polizas[poliza]['nombre'])

def mayor_monto(polizas : list, tamanio : int):
    for poliza in range(0, tamanio):
       if (polizas[poliza]['monto']) > 100000:
            print("Nombre: ", polizas[poliza]['nombre'])
         

def mostrar_asegurados(polizas : list, tamanio : int):
    for poliza in range(0, tamanio):
        if (polizas[poliza]['nombre'] == 'Pedro Fernandez'):
            print(f"{polizas[poliza]['nombre']} esta asegurado en la compania.")


polizas = [0, 0, 0, 0]
print("Ingrese las polizas.")
TAMANIO = len(polizas)
limite = cargar_polizas(polizas, TAMANIO)
print()

print("Personas mayor a 70 anios: ")
mayor_edad(polizas, limite)
print()
print("Personas cuyas cuotas es menor a $30.00: ")
menor_cuota(polizas, limite)
print()
print("Personas que tienen un monto asegurado mayor a $100.000: ")
mayor_monto(polizas, limite)
# TODO : Determina si Pedro Fernandez esta registrado en la aseguradora.
mostrar_asegurados(polizas, limite)