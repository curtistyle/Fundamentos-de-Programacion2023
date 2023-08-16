""" ¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232? """

suma = 0
for index in range(300,1233):
    if ((index % 2) == 0):
        suma = suma + index

print(f"La suma asciende a {suma}.")