# TP4 - Condicionales

## Ejercicio 1

1. Determinar si un número leído es positivo. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir "El ingresado numero es positivo.";
    FinSi
FinAlgoritmo
```

**version 2**  _(condicional doble)_

```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir "El numero ingresado es positivo.";
    SiNo
        Escribir "El numero ingresado es negativo.";
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
        Escribir "El ", Numero ," es mayor a 10."; 
    FinSi
FinAlgoritmo
```

**version 2** _(condicional doble)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero > 10) Entonces
        Escribir "El Numero ingresado es Mayor a 10.";
    SiNo
        Escribir "El Numero ingresado es Menor a 10.";
    FinSi
FinAlgoritmo
```

**version 3** _(anidado)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero > 10) Entonces
        Escribir "El Numero ingresado es Mayor a 10.";
    SiNo 
        Si (Numero = 10) Entonces
            Escribir "El Numero ingresado es igual a 10.";
        SiNo
            Escribir "El Numero ingresado es menor a 10.";
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
        Escribir (Nombre, " gana mas de $30000.";
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
        Escribir (Nombre, " gana mas de $30000.";
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
        Escribir (Nombre, " gana mas de $30000.";
    SiNo
        Si (Sueldo = 30000) Entonces
            Escribir (Nombre, " gana $30000.";
        SiNo
            Si (Sueldo > 0) y (Sueldo < 30000) Entonces
                Escribir (Nombre, " gana menos $30000.";
            SiNo
                Escribir "¡Error!, el sueldo ingresado no es valido.";
    FinSi
FinAlgoritmo
```

## Ejercicio 4

4. Dados dos números si el primero es divisible por el segundo mostrar un mensaje que así 
lo indique. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero1, Numero2, Resultado Como Entero;

    Leer Numero1, Numero2;

    Resultado <- Numero1 mod Numero2;

    Si (Resultado = 0) Entonces
        Escribir (Numero1 ," es divisible por ", Numero2);
    FinSi
FinAlgoritmo
```

**version 2** _(condicional simple)_
```
Algoritmo
    Definir Numero1, Numero2 Como Entero;

    Leer Numero1, Numero2;

    Si ((Numero1 mod Numero2) = 0) Entonces
        Escribir (Numero1 ," es divisible por ", Numero2);
    FinSi
FinAlgoritmo
```

**version 3** _(condicional doble)_
```
Algoritmo
    Definir Numero1, Numero2, Resultado Como Entero;

    Leer Numero1, Numero2;

    Resultado <- Numero1 mod Numero2;

    Si (Resultado = 0) Entonces
        Escribir (Numero1 ," es divisible por ", Numero2);
    SiNo
        Escribir (Numero1 ," NO es divisible por", Numero2);
    FinSi
FinAlgoritmo
```

## Ejercicio 5

5. Ingresar un par de valores, emitirlos, y si ambos son positivos, emitir también su promedio.

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero1, Numero2, Promedio Como Real;

    Leer Numero1, Numero2;

    Escribir Numero1, Numero2;

    Si (Numero1 > 0) y (Numero2 > 0) Entonces
        Promedio <- (Numero1 + Numero2) / 2;
        Escribir Promedio;
    FinSi
FinAlgoritmo
```

**version 2** _(condicional doble)_
```
Algoritmo
    Definir Numero1, Numero2, Promedio Como Real;

    Leer Numero1, Numero2;

    Si (Numero1 > 0) y (Numero2 > 0) Entonces
        Promedio <- (Numero1 + Numero2) / 2;
        Escribir "Los numeros son positivos y su promedio es: ", Promedio);
    SiNo
        Escrbir "Los numeros No son positivos.";
    FinSi
FinAlgoritmo
```

## Ejercicio 6

6. Dados dos números si el primero es divisible por el segundo intercambiarlos

```
Algoritmo
    Definir Numero1, Numero2, Auxiliar Como Real;

    Leer Numero1, Numero2;

    Si ((Numero1 mod Numero2) = 0) Entonces
        Auxiliar <- Numero1;
        Numero1 <- Numero2;
        Numero2 <- Auxiliar;
        
        Escribir "Se intercambambiaron los numeros, Numero1: ", Numero1 ," y Numero2: ", Numero2);
    FinSi
FinAlgoritmo
```

## Ejercicio 7

7. Deducir si un número leído (distinto de cero) es positivo o negativo.

```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir "El numero ingresado en positivo.";
    SiNo
        Escribir "El numero ingresado es negativo.";
    FinSi
FinAlgoritmo
```

## Ejercicio 8

8. Dados tres números enteros positivos, determinar cuál es el mayor.

**version 1**
```
Algoritmo
    Definir Numero1, Numero2, Numero3 Como Real;

    Leer Numero1, Numero2, Numero3;

    Si (Numero1 > 0) y (Numero2 > 0) y (Numero3 > 0) Entonces
        Si (Numero1 > Numero2) y (Numero1 > Numero3) Entonces 
            Escribir "El mayor es ", Numero1);
        SiNo
            Si (Numero2 > Numero3) y (Numero2 > Numero1) Entonces
                Escribir "El mayor es ", Numero2);
            SiNo
                Escribir "El mayor es ", Numero3);
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Numero1, Numero2, Numero3 Como Real;

    Leer Numero1, Numero2, Numero3;

    Si (Numero1 > 0) y (Numero2 > 0) y (Numero3 > 0) Entonces
        Si (Numero1 > Numero2) y (Numero1 > Numero3) Entonces 
            Escribir "El mayor es ", Numero1);
        SiNo
            Si (Numero2 > Numero3) y (Numero2 > Numero1) Entonces
                Escribir "El mayor es ", Numero2);
            SiNo
                Escribir "El mayor es ", Numero3);
            FinSi
        FinSi
    SiNo
        Escribir "Los numeros ingresados no son positivos".)
    FinSi
FinAlgoritmo
```

# Ejercicio 9

9. Escribir  un  programa  que  muestre  un  mensaje  afirmativo  si  el  número  introducido  es 
múltiplo de 5.

*version 1* _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si ((Numero mod 5) = 0) Entonces
        Escribir "El numero ", numero ," es multiplo de 5.";
    FinSi
FinAlgoritmo
```

*version 2* _(condicional doble)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si ((Numero mod 5) = 0) Entonces
        Escribir "El numero ", numero ," es multiplo de 5.";
    SiNo
        Escribir "El numero ", numero ," NO es multiplo de 5";
    FinSi
FinAlgoritmo
```

## Ejercicio 10

10. Leer tres letras, encontrar y visualizar cuál viene primero en el alfabeto

```
Algoritmo ejercicio
	Definir Letra1, Letra2, Letra3 Como Caracter;
	
	Leer Letra1, Letra2;
	
	Si ((Letra1 < Letra2) & (Letra1 < Letra3)) Entonces
		Escribir "La letra ", Letra1, " viene Primero.";
	SiNo
		Si ((Letra2 < Letra1) y (Letra2 < Letra3)) Entonces 
			Escribir "La letra ", Letra2 ," viene Primero.";
		SiNo
			Escribir "La letra ", Letra3 ," viene Primero.";
		FinSi
	FinSi
FinAlgoritmo
```

## Ejercicio 13

13. Desarrollar un algoritmo que una vez leída una Fecha en formato dd/mm/aaaa, indique cual 
será la fecha un día después.

| # | MES | DURACION |
| - | --- | -------- |
| 1 | Enero  | 31 dias |
| 2 | Febrero | 28 dias o 29 año bisiesto |
| 3 | Marzo | 31 dias |
| 4 | Abril | 30 dias |
| 5 | Mayo | 31 dias |
| 6 | Junio | 30 dias |
| 7 | Julio | 31 dias |
| 8 | Agosto | 31 dias |
| 9 | Septiembre | 30 dias |
| 10 | Octubre | 31 dias |
| 11 | Noviembre | 30 dias |
| 12 | Diciembre | 31 dias |

 > **Año bisiesto** 
 > - Divisible entre 4 
 > - Divisible entre 400 
 > - No divisible entre 100 
 > 
 > p : Es divisible entre 4 \
 > q : Es divisible entre 400 \
 > r : Es divisible entre 100 ( ¬r : No es divisible entre 100 ). \
 > Entonces nos queda la siguiente proposicion. \
 > p ∧ (¬r ∨ q)




```
Algoritmo
    Definir Dia, Mes, Anio, siguienteDia, SiguienteMes, siguienteAnio Como Entero;

    siguienteDia <- 0;
    siguienteMes <- 0;
    siguienteAnio <- 0;

    Leer Dia, Mes, Anio;

    Si (Mes = 2) Entonces
        Si ((Anio mod 4) = 0) y (((anio mod 100) <> 0) o ((anio mod 400) = 0)) Entonces
            Si (Dia = 29) Entonces
                siguienteDia = 1;
                siguienteMes = Mes + 1;
            SiNo
                siguienteDias = Dia + 1;
                siguienteMes = Mes;
            FinSi
        SiNo
            Si (Dia = 28) Entonces
                siguienteDia = 1;
                siguienteMes = Mes + 1;
            SiNo
                siguienteDia = Dia + 1;
                siguienteMes = Mes;
            FinSi
        FinSi
    SiNo
        Si (Mes = 4) o (Mes = 6) o (Mes = 9) o (Mes = 11) Entonces
            Si (Dia = 30) Entonces
                siguienteDia = 1;
                siguienteMes = Mes + 1;
            SiNo
                iguienteDia = Dia + 1;
                siguienteMes = Mes;
            FinSi
        SiNo
            Si (Dia = 31) Entonces
                Si (Mes = 12) Entonces
                    siguienteDia = 1;
                    siguienteMes = 1;
                    siguienteAnio = Anio + 1;
                SiNo
                    siguienteDia = Dia + 1;
                    siguienteMes = Mes;
                FinSi
            SiNo
                siguienteDia = Dia + 1;
                siguienteMes = Mes;
            FinSi
        FinSi
    FinSi

    Si (siguienteAnio <> 0) Entonces
        Escribir ('El dia siguiente es: ', siguienteDia ,'/', siguienteMes ,'/', siguienteAnio);
    SiNo
        Escribir ('El dia siguiente es: ', siguienteDia ,'/', siguienteMes, '/', Anio);
    FinSi;
FinAlgoritmo
```

