""" Dada la siguiente situación: se dispone de un mazo de cartas españolas. Se debe sacar 
la primera carta y separarla. Luego sacar de a una carta por vez hasta encontrar una del 
mismo palo y número mayor a la primera. El problema planteado es determinar cuántas 
cartas fue necesario extraer del mazo. """

# inicializar varibles

indice = 1

numero = int(input("Ingrese el numero de la carta: "))
palo = input("Ingrese el palo de la carta (oro, espada, copa, basto): ")

auxNumero = numero + 1
auxPalo = palo
print(f"Se separo del mazo el {auxNumero - 1} de {auxPalo}.")

print(f"palo {palo}, numero {numero}, auxpalo {auxPalo}, numero {auxNumero}")

while not ((auxPalo == palo) and (auxNumero == numero)):
    numero = int(input("Ingrese el numero de la carta: "))
    palo = input("Ingrese el palo de la carta (oro, espada, copa, basto): ")
    indice += 1
    
print(f"Fueron necesario sacar {indice - 1} cartas del mazo.")

