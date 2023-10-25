def promedio(lista : list, tamanio : int, campo : str):
    acumulador = 0
    for empleado in range(0, tamanio):
        acumulador += lista[empleado][campo]
    return acumulador / tamanio