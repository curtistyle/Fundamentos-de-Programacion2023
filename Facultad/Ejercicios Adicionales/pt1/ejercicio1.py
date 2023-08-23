totalCostos = 0
totalPersonal = 0
auxCostos = 0
auxPersonal = None

for index in range(1,6):
    nombreCompleto = input("Nombre completo del responsable de la obra: ")
    print(f"Ingrese los datos de la obra ({index}).")
    costos = float(input("Costos de la obra: $"))
    personal = int(input("Cantidad de Personal involucrado en la obra: "))
    
    if (nombreCompleto == "Maria Paez"):
        auxCostos = costos
        auxPersonal = personal
    
    totalCostos += costos
    totalPersonal += personal

print("Total de fondos de la obra: ", totalCostos)
print("Total de personal de las obras: ", totalPersonal)

if (auxCostos != 0):
    print("Maria Paez tiene un cargo en la obra.")
    print(f"Su porcentaje de inversion en la obra con respecto a las demas: {(auxCostos * 100)/totalCostos}%")
    print("Cantidad de personal a cargo de Maria Paez: ", auxPersonal)


        