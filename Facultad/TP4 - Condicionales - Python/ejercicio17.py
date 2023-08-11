""" Emular una calculadora en la cual se ingresan 2 números y el operador (*, /, +, -) e 
imprime el resultado """

print(" # Calculadora - Ingrese dos numeros. ")

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

operador = input("Ingres el operador: ")

if (numero2 != 0) and (operador != "/"):
    if (operador == "+"):
        print(f"(SUMA) Resultado: {(numero1 + numero2):.2f}")
    elif (operador == "-"):
        print(f"(RESTA) Resultado: {(numero1 - numero2):.2f}")
    elif (operador == "/"):
        print(f"(DIVISION) Resultado: {(numero1 / numero2):.2f}")
    elif (operador == "*"):
        print(f"(MULTIPLICAR) Resultado: {(numero1 * numero2):.2f}")
    else:
        print("Operador incorrecto.")
else:
    print("¡No se puede dividir por cero.!")