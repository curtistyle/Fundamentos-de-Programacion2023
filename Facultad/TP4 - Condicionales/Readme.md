# TP4 - Condicionales

## Ejercicio 1

1. Determinar si un número leído es positivo. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir ("El ingresado numero es positivo.");
    FinSi
FinAlgoritmo
```

**version 2**  _(condicional doble)_

```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir ("El numero ingresado es positivo.");
    SiNo
        Escribir ("El numero ingresado es negativo.");
    FinSi
FinAlgoritmo
```

## Ejercicio 2

2. Mostrar si un número es mayor que 10. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero > 10) Entonces
        Escribir ("El ", Numero ," es mayor a 10."); 
    FinSi
FinAlgoritmo
```

**version 2** _(condicional doble)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero > 10) Entonces
        Escribir ("El Numero ingresado es Mayor a 10.");
    SiNo
        Escribir ("El Numero ingresado es Menor a 10.");
    FinSi
FinAlgoritmo
```

**version 3** _(anidado)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero > 10) Entonces
        Escribir ("El Numero ingresado es Mayor a 10.");
    SiNo 
        Si (Numero = 10) Entonces
            Escribir ("El Numero ingresado es igual a 10.");
        SiNo
            Escribir ("El Numero ingresado es menor a 10.");
    FinSi
FinAlgoritmo
```

## Ejercicio 3

3. Leer el nombre y sueldo de una persona mostrar si este gana más de 30.000 pesos. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Nombre Como Cadena;
    Definir Sueldo Como Real;

    Leer Nombre, Sueldo;

    Si (Sueldo > 30000) Entonces
        Escribir (Nombre, " gana mas de $30000.");
    FinSi
FinAlgoritmo
```
**version 2** _(condicional doble)_
```
Algoritmo
    Definir Nombre Como Cadena;
    Definir Sueldo Como Real;

    Leer Nombre, Sueldo;

    Si (Sueldo > 30000) Entonces
        Escribir (Nombre, " gana mas de $30000.");
    FinSi
FinAlgoritmo
```
**version 3** _(anidados)_
```
Algoritmo
    Definir Nombre Como Cadena;
    Definir Sueldo Como Real;

    Leer Nombre, Sueldo;

    Si (Sueldo > 30000) Entonces
        Escribir (Nombre, " gana mas de $30000.");
    SiNo
        Si (Sueldo = 30000) Entonces
            Escribir (Nombre, " gana $30000.");
        SiNo
            Si (Sueldo > 0) y (Sueldo < 30000) Entonces
                Escribir (Nombre " gana menos $30000.");
            SiNo
                Escribir ("¡Error!, el sueldo ingresado no es valido.");
    FinSi
FinAlgoritmo
```

## Ejercicio 4

4. 


```
Algoritmo
    Definir 
FinAlgoritmo
```