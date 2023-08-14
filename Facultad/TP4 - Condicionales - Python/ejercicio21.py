""" La tarifa de un TAXI en Europa es la siguiente: 
        - Una cantidad fija de 20 euros, sino se sobrepasan los 30 km. 
        - Para más de 30 km, se considerarán los siguientes supuestos: 
            ▪ Si no se sobrepasan los 100 km, 1 euro por km, que exceda de los 30, además 
              de los 20 euros. 
            ▪ Si sobrepasa los 100 km, 0,50 céntimos por km que exceda de los 100, 1 euro 
              por km desde los 30 a los 100 y los 20 euros. Diseñar un programa que pida los 
              kilómetros recorridos y calcule el total a pagar según la tarifa anterior. """

distancia = float(input("(METODO 1) Ingrese la distancia recorrida: "))

if (distancia <= 30):
    monto = distancia * 20
elif (distancia > 30) and (distancia <= 100):
    monto = (30 * 20) + (distancia - 30)
else:
    monto = (30 * 20) + 70 + ((distancia - 100) * 0.5)

print(f"Distancia recorrida: {distancia:.2f} km", f" Monto: ${monto:.2f}")
# ! otro metodo

distancia = float(input("(METODO 2) Ingrese la distancia recorrida: "))
    
if (distancia <= 30):
    monto = distancia * 20
    if (distancia > 30) and (distancia <= 100):
        monto = monto + (distancia - 30)
        if(distancia > 100):
            monto = monto + ((distancia - 100) * 0.5)

print(f"Distancia recorrida: {distancia:.2f} km", f" Monto: ${monto:.2f}")


