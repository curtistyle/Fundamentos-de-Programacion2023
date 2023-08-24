""" Escribir un procedimiento tipo calculadora donde se le da como entrada dos números y el 
tipo de operación y esta devuelve el resultado. """


def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def dividir(a,b):
    return a / b

def multiplicar(a,b):
    a * b
    
def operador(op,a,b):
    if (op == '+'):
        return suma(a,b)
    elif (op == '-'):
        return resta(a,b)
    elif (op == '/'):
        if (b != 0):
            return dividir(a,b)
        else:
            return 'No se puede dividir por 0'
    elif (op == '*'):
        return multiplicar(a,b)
    else:
        return 'Operador incorrecto!.'
    

while True:
    x = float(input("Ingrese el primer numero: "))
    op = input("ingrese el operador: ")
    y = float(input("Ingrese el segundo numero: "))
    print("RESULTADO: ", operador(x,y,op))
    