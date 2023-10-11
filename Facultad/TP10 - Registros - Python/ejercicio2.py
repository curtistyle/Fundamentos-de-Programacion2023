



def insertar_poliza(indice : int):
    poliza = {
    'numero': 0,
    'nombre': "",
    'direccion': "",
    'nacimiento': "",
    'monto': 0.0,
    'cuota': 0.0
}
    poliza['numero'] = indice
    poliza['nombre'] = input("Ingrese el Nombre: ")
    poliza['direccion'] = input("Ingrese la Direccion: ")
    poliza['nacimiento'] = int(input("Ingrese el anio de Nacimiento: "))
    poliza['monto'] = float(input("Ingrese la cantidad asegurada: "))
    poliza['cuota'] = float(input("Ingrese la cuota: "))
    return poliza

def cargar_poliza(lim,polizas):
    opcion=input("Ingrese s para cargar una persona:  ")
    while ( (opcion == 's') and (lim < len(polizas)) ):
        polizas[lim]=insertar_poliza(lim)
        lim+=1
        print()
        if lim<(len(polizas)):
            opcion=input("Ingrese s para cargar una persona:  ")
    return limite

def mayor_edad_70(polizas,limite):
    for indice in range(0,limite):
        print(".>>>>",polizas)
        poliza = polizas[indice]
        edad = 2023 - poliza["nacimiento"]
        edad = 71
        print("Nombre: ", polizas[indice]['nombre'])
        print("Direccion: ",polizas[indice]['direccion'])
        

def menor_cuota_30(polizas, limite):
    for poliza in range(0,limite):
       if (polizas[poliza]['cuota']) < 30:
            print("Nombre: ", polizas[poliza]['nombre'])

def mayor_monto(polizas, limite):
    for poliza in range(0,limite):
       if (polizas[poliza]['monto']) > 100000:
            print("Nombre: ", polizas[poliza]['nombre'])
         

def mostrar_asegurados(polizas, limite):
    for poliza in range(0, limite):
        if (polizas[poliza]['nombre'] == 'Pedro Fernandez'):
            print(f"{polizas[poliza]['nombre']} esta asegurado en la compania.")



polizas = [0, 0, 0, 0]
limite=0
print("Ingrese las polizas.")
limite = cargar_poliza(limite, polizas)
print()
print(polizas)
print("Personas mayor a 70 anios: ")
mayor_edad_70(polizas,limite)
print()
print("Personas cuyas cuotas es menor a $30.00: ")
menor_cuota_30(polizas, limite)
print()
print("Personas que tienen un monto asegurado mayor a $100.000: ")
mayor_monto(polizas, limite)
# TODO : Determina si Pedro Fernandez esta registrado en la aseguradora.
mostrar_asegurados(polizas, limite)