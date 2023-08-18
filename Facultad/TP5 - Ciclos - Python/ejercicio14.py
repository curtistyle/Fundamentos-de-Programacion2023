"""  Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales hasta el 
        Nº 10. 
        Ej. 
            5 por 1 es 5 
            5 por 2 es 10
            5 por 3 es 15  
"""

for x in range(1,11):
    print(f"Tabla del {x}.")
    for y in range(1,11):
        print(f"{x} x {y} : {x*y}")

