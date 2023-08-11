"""Un millonario excéntrico tenía tres hijos: Carlos,  José y Marta. Al morir dejó el siguiente 
legado: A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. A 
Marta le dejo la mitad de lo que le dejó a José. Preparar un algoritmo para darle la suma 
a repartir e imprima cuanto le tocó a cada uno. """

legado = float(input("Ingrese la herencia del millonario: "))

carlos = 1/3
jose = 4/3
martina = 1/2

carlos = legado * carlos
jose = carlos * jose
martina = jose * martina

print(f"A Carlos le corresponde: ${carlos:.2f}.")
print(f"A jose: ${jose:.2f}.")
print(f"Y a Martina: ${martina:.2f}.")




