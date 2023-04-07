# TP4 - Condicionales

## Ejercicio 1

1. Determinar si un número leído es positivo. 

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 0) Entonces
        Escribir "El numero ingresado es positivo.";
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
        Escribir Nombre, " gana mas de $30000.";
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
        Escribir Nombre, " gana mas de $30000.";
    SiNo
        Escribir Nombre, " gana menos de $30000.";
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
        Escribir Nombre, " gana mas de $30000.";
    SiNo
        Si (Sueldo = 30000) Entonces
            Escribir Nombre, " gana $30000.";
        SiNo
            Si (Sueldo > 0) y (Sueldo < 30000) Entonces
                Escribir Nombre, " gana menos $30000.";
            SiNo
                Escribir "¡Error!, el sueldo ingresado no es valido.";
            FinSi
        FinSi
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
        Escribir Numero1 ," es divisible por ", Numero2;
    FinSi
FinAlgoritmo
```

**version 2** _(condicional simple)_
```
Algoritmo
    Definir Numero1, Numero2 Como Entero;

    Leer Numero1, Numero2;

    Si ((Numero1 mod Numero2) = 0) Entonces
        Escribir Numero1 ," es divisible por ", Numero2;
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
        Escribir Numero1 ," es divisible por ", Numero2;
    SiNo
        Escribir Numero1 ," NO es divisible por", Numero2;
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
        Escribir "Los numeros son positivos y su promedio es: ", Promedio;
    SiNo
        Escribir "Los numeros No son positivos.";
    FinSi
FinAlgoritmo
```

## Ejercicio 6

6. Dados dos números si el primero es divisible por el segundo intercambiarlos

**version 1**_(condicional simple)_
```
Algoritmo
    Definir Numero1, Numero2, Auxiliar Como Real;

    Leer Numero1, Numero2;

    Si ((Numero1 mod Numero2) = 0) Entonces
        Auxiliar <- Numero1;
        Numero1 <- Numero2;
        Numero2 <- Auxiliar;
        
        Escribir "Se intercambambiaron los numeros, Numero1: ", Numero1 ," y Numero2: ", Numero2;
    FinSi
FinAlgoritmo
```
**version 2**_(condicional doble)_
```
Algoritmo ejercicio6
	Definir Numero1, Numero2, Auxiliar Como Real;
	
	Leer Numero1, Numero2;
    
	Si ((Numero1 mod Numero2) = 0) Entonces
        Auxiliar <- Numero1;
        Numero1 <- Numero2;
        Numero2 <- Auxiliar;
        
        Escribir "Se intercambambiaron los numeros, Numero1: ", Numero1 ," y Numero2: ", Numero2;
	SiNo
		Escribir "El primer numero no es divisible por el segundo";
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
            Escribir "El mayor es ", Numero1;
        SiNo
            Si (Numero2 > Numero3) y (Numero2 > Numero1) Entonces
                Escribir "El mayor es ", Numero2;
            SiNo
                Escribir "El mayor es ", Numero3;
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
            Escribir "El mayor es ", Numero1;
        SiNo
            Si (Numero2 > Numero3) y (Numero2 > Numero1) Entonces
                Escribir "El mayor es ", Numero2;
            SiNo
                Escribir "El mayor es ", Numero3;
            FinSi
        FinSi
    SiNo
        Escribir "Los numeros ingresados no son positivos.";
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
        Escribir "El numero ", Numero ," es multiplo de 5.";
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
	
	Leer Letra1, Letra2, Letra3;
	
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

## Ejercicio 11

11. Confeccionar un algoritmo tal que dados dos números enteros devuelva la suma de los mismos, si se cumple que el primero es menor que el segundo, en caso contrario devolver el producto de los mismos. 

```
Algoritmo
    Definir Numero1, Numero2, Producto, Suma Como Entero;

    Leer Numero1, Numero2;

    Si (Numero1 < Numero2) Entonces
        Suma <- Numero1 + Numero2;
        Escribir Suma;
    SiNo
        Producto <- Numero1 * Numero2;
        Escribir Producto;
    FinSi
FinAlgoritmo
```

## Ejercicio 12

12. Se ingresa el nombre, edad y dirección de dos socios, se pide mostrar los datos de socio más joven. 

```
Algoritmo
    Definir Nombre1, Direccion1, Nombre2, Direccion2 Como Cadena;
    Definir Edad1, Edad2 Como Entero;

    Leer Nombre1, Direccion1, Edad1; 
    Leer Nombre2, Direccion2, Edad2;

    Si (Edad1 < Edad2) Entonces
        Escribir Nombre1, "es el Socio mas Joven,  con la edad de ", Edad1, " años y direccion ", Direccion1;
    SiNo
        Escribir Nombre2, "es el Socio mas Joven,  con la edad de ", Edad2, " años y direccion ", Direccion2;
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
Algoritmo ejercicio13
    Definir Dia, Mes, Anio, siguienteDia, SiguienteMes, siguienteAnio Como Entero;
	
    siguienteDia <- 0;
    siguienteMes <- 0;
    siguienteAnio <- 0;
	
	Leer Dia, Mes, Anio;

    Si (Mes = 2) Entonces
        Si ((Anio mod 4) = 0) y (((anio mod 100) <> 0) o ((anio mod 400) = 0)) Entonces
            Si (Dia = 29) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDias <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        SiNo
            Si (Dia = 28) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        FinSi
    SiNo
        Si (Mes = 4) o (Mes = 6) o (Mes = 9) o (Mes = 11) Entonces
            Si (Dia = 30) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        SiNo
            Si (Dia = 31) Entonces
                Si (Mes = 12) Entonces
                    siguienteDia <- 1;
                    siguienteMes <- 1;
                    siguienteAnio <- Anio + 1;
                SiNo
                    siguienteDia <- Dia + 1;
                    siguienteMes <- Mes;
                FinSi
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        FinSi
    FinSi
	
    Si (siguienteAnio <> 0) Entonces
        Escribir 'El dia siguiente es: ', siguienteDia ,'/', siguienteMes ,'/', siguienteAnio;
    SiNo
        Escribir 'El dia siguiente es: ', siguienteDia ,'/', siguienteMes, '/', Anio;
    FinSi
FinAlgoritmo
```

## Ejercicio 14

14. Dados tres nombres de alumnos, mostrar si Mariana Ríos se encuentra entre ellos, de lo contrario emitir un mensaje “No existe”. 

**version 1**
```
Algoritmo
    Definir Nombre1, Nombre2, Nombre3 Como Cadena;

    Leer Nombre1, Nombre2, Nombre3;

    Si (Nombre1 = 'Mariana Ríos') Entonces
        Escribir "Mariana Ríos esta en la lista.";
    SiNo
        Si (Nombre2 = 'Mariana Ríos') Entonces
            Escribir "Mariana Ríos esta en la lista.";
        SiNo
            Si (Nombre3 = 'Mariana Ríos') Entonces
                Escribir "Mariana Ríos esta en la lista.";
            SiNo
                Escribir "No existe en la lista.";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```
**version 2**
```
Algoritmo
    Definir Nombre1, Nombre2, Nombre3 Como Cadena;

    Leer Nombre1, Nombre2, Nombre3;

    Si (Nombre1 = 'Mariana Ríos') o (Nombre2 = 'Mariana Ríos') o (Nombre3 = 'Mariana Ríos') Entonces
        Escribir "Mariana Ríos esta en la lista.";
    SiNo
        Escribir "No existe en la lista";
    FinSi
FinAlgoritmo
```

## Ejercicio 15

15. Calcular el descuento considerando que para un monto mayor de $1000.- el descuento es del 10%, caso contrario es del 2%. Se pide mostrar monto con descuento incluido.

**version 1**
```
Algoritmo
    Definir Descuento, Monto, Total Como Real;

    Leer Monto;

    Si (Monto > 1000) Entonces
        Descuento <- (10 * Monto) / 100;
        Total <- Monto - Descuento;
        Escribir "Monto mas el descuento del 10%: ", Total; 
    SiNo
        Descuento <- (2 * Monto) / 100;
        Total <- Monto - Descuento;
        Escribir "Monto mas el descuento del 2%: ", Total; 
    FinSi
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Descuento, Monto Como Real;
	
    Leer Monto;
	
    Si (Monto > 1000) Entonces
        Descuento <- Monto - (Monto * 0.1);
        Escribir "Monto: $", Monto ," el descuento del 10%: $", Descuento;  
    SiNo
        Descuento <- Monto - (Monto * 0.02);
        Escribir "Monto: $", Monto ," el descuento del 2%: $", Descuento; 
    FinSi
FinAlgoritmo
```

## Ejercicio 16

16. Escribir un algoritmo en el que se introduzca el número de un mes (1 a 12) y visualice el Nº de días de ese mes. (no considerar año bisiesto).

**version 1**

```
Algoritmo
    Definir Mes Como Entero;

    Leer Mes;

    Si (Mes = 1) o (Mes = 3) o (Mes = 5) o (Mes = 7) o (Mes = 8) o (Mes = 10) o (Mes = 12) Entonces
        Escribir "31";
    SiNo
        Si (Mes = 2) Entonces
            Escribir "28";
        SiNo
            Escribir "30";
        FinSi
    FinSi
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Mes Como Entero;

    Leer Mes;

    Si (Mes = 4) o (Mes = 6) o (Mes = 9) o (Mes = 11) Entonces
        Escribir "30";
    SiNo
        Si (Mes = 2) Entonces
            Escribir "28";
        SiNo
            Escribir "31";
        FinSi
    FinSi
FinAlgoritmo
```


**version 3** 
```
Algoritmo   
    Definir Mes Como Entero;

    Leer Mes;

    Si (Mes = 1) Entonces
        Escribir "31";
    SiNo
        Si (Mes = 2) Entonces
            Escribir "28";
        SiNo
            Si (Mes = 3) Entonces
                Escribir "31";
            SiNo
                Si (Mes = 4) Entonces
                    Escribir "30";
                SiNo
                    Si (Mes = 5) Entonces
                        Escribir "31";
                    SiNo
                        Si (Mes = 6) Entonces
                            Escribir "30";
                        SiNo
                            Si (Mes = 7) Entonces
                                Escribir "31";
                            SiNo
                                Si (Mes = 8) Entonces
                                    Escribir "31";
                                SiNo
                                    Si (Mes = 9) Entonces
                                        Escribir "30";
                                    SiNo
                                        Si (Mes = 10) Entonces
                                            Escribir "31";
                                        SiNo
                                            Si (Mes = 11) Entonces
                                                Escribir "30";
                                            SiNo
                                                Si (Mes = 12) Entonces
                                                    Escribir "31";
                                                SiNo
                                                    Escribir "Mes fuera de rango.";
                                                FinSi
                                            FinSi
                                        FinSi
                                    FinSi
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```


**version 4** _(condicional segun)_

```
Algoritmo
    Definir Mes Como Entero;

    Leer Mes;

    Segun Mes Hacer
            1, 3, 5, 7, 8, 10, 12 : Escribir "31";
            4, 6, 9, 11 : Escribir "30";
            2 : Escribir "28";
        De otro modo:
            Escribir "Mes fuera de rango.";
    FinSegun
FinAlgoritmo
```


**version 4** _(condicional segun)_

```
Algoritmo
    Definir Mes Como Entero;

    Leer Mes;

    Segun Mes Hacer
        1 : 
            Escribir "31";
        2 : 
            Escribir "28";
        3 : 
            Escribir "31";
        4 : 
            Escribir "30";
        5 : 
            Escribir "31";
        6 : 
            Escribir "30";
        7 : 
            Escribir "31";
        8 : 
            Escribir "31";
        9 : 
            Escribir "30";
        10:
            Escribir "31";
        11:
            Escribir "30";
        12: 
            Escribir "31";
        De otro modo:
            Escribir "Mes fuera de rango.";
    FinSegun
FinAlgoritmo
```

## Ejercicio 17

17. Emular una calculadora en la cual se ingresan 2 números y el operador (*, /, +, -) e imprime el resultado.

**version 1**

```
Algoritmo
    Definir Numero1, Numero2, Resultado Como Real;
    Definir Operador Como Cadena;

    Leer Numero1, Numero2, Operador;

    Si (Operador = '+') Entonces
        Resultado <- Numero1 + Numero2;
        Escribir Resultado;
    SiNo
        Si (Operador = '-') Entonces
            Resultado <- Numero1 - Numero2;
            Escribir Resultado;
        SiNo
            Si (Operador = '*') Entonces
                Resultado <- Numero1 * Numero2;
                Escribir Resultado;
            SiNo
                Si (Operador = '/') y (Numero2 <> 0) Entonces   
                    Resultado <- Numero1 / Numero2;
                    Escribir Resultado;
                SiNo
                    Escribir "¡Operador incorrecto!";
                FinSi
            FinSI
        FinSi
    FinSi
FinAlgoritmo
```

**version 2**

```
Algoritmo
    Definir Operador Como Caracter;
    Definir Numero1, Numero2, Resultado Como Real

    Leer Operador, Numero1, Numero2;

    Segun Operador Hacer
        "+" : 
            Resultado <- Numero1 + Numero2;
            Escribir "Resultado: ", Resultado;
        "-" :
            Resultado <- Numero1 - Numero2;
            Escribir "Resultado: ", Resultado;
        "*" :
            Resultado <- Numero1 * Numero2;
            Escribir "Resultado: ", Resultado;
        "/" :
            Si (Numero2 <> 0) Entonces
                Resultado <- Numero1 / Numero2;
                Escribir "Resultado: ", Resultado;
            SiNo
                Escribir "No se puede dividir por 0";
            FinSi
    De otro modo:
        Escribir "Operador invalido";
    FinSegun 
FinAlgoritmo
```

**version 3**

```
Algoritmo
    Definir Operador : Como Caracter;
    Definir Numero1, Numero2 : Como Real

    Leer Operador, Numero1, Numero2;

    Segun Operador Hacer
        "+" : 
            Escribir "Resultado: ", Numero1 + Numero2;
        "-" :
            Escribir "Resultado: ", Numero1 - Numero2;
        "*" :
            Escribir "Resultado: ", Numero1 * Numero2;
        "/" :
            Si (Numero2 < > 0) Entonces
                Escribir "Resultado: ", Numero1 / Numero2;
            SiNo
                Escribir "No se puede dividir por 0";
            FinSi
    De otro modo:
        Escribir "Operador invalido";
    FinSegun 
FinAlgoritmo
```

## Ejercicio 18 

18. Leer dos números. Decir si el primero es divisible por el segundo, si esto se cumple decir 
si es un número par o impar.

```
Algoritmo
    Definir Numero1, Numero2 Como Real;

    Leer Numero1, Numero2;

    Si ((Numero1 mod Numero2) = 0) Entonces
        Si ((Numero1 mod 2) = 0) Entonces
            Escribir "El primer numero es par.";
        SiNo
            Escribir "El primer numero es impar.";
        FinSi
    SiNo
        Escribir "El primer numero no es divisible por el segundo.";
    FinSi
FinAlgoritmo
```

## Ejercicio 19

19. Leer un número, si dicho número está comprendido entre 23 y 54, decir si es múltiplo de 3 
o de 5.

**version 1** _(condicional simple)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 23) y (Numero <= 54) Entonces
        Si ((Numero mod 5) = 0) Entonces
            Escribir Numero, " es multiplo de 5";
        FinSi
    FinSi
FinAlgoritmo
```

**version 2** _(condicional compuesto)_
```
Algoritmo
    Definir Numero Como Real;

    Leer Numero;

    Si (Numero >= 23) y (Numero <= 54) Entonces
        Si ((Numero mod 5) = 0) Entonces
            Escribir Numero, " es multiplo de 5";
        SiNo
            Escribir Numero, " NO es multiplo de 5";
        FinSi
    Sino
        Escribir "El ", Numero , " no esta en el rango definido.";
    FinSi 
FinAlgoritmo   
```

## Ejercicio 20

20. Dadas las 4 notas obtenidas por un alumno, calcular e informar su promedio e informar 
una leyenda que indique si está aprobado o no. La condición de aprobación es obtener un 
promedio mayor o igual que 4.

```
Algoritmo
    Definir Nota1, Nota2, Nota3, Nota4, Promedio Como Real;

    Leer Nota1, Nota2, Nota3, Nota4;

    Promedio <- (Nota1 + Nota2 + Nota3 + Nota4) / 4;

    Si (Promedio >= 4) Entonces
        Escribir "Su promedio es: ", Promedio ,", usted esta aprobado.";
    SiNo
        Escribir "Su promedio es: ", Promedio ,", usted esta desaprobado." 
    FinSi
FinAlgoritmo
```

## Ejercicio 21

21. La tarifa de un TAXI en Europa es la siguiente: 
- Una cantidad fija de 20 euros, sino se sobrepasan los 30 km. 
- Para más de 30 km, se considerarán los siguientes supuestos: 
    - Si no se sobrepasan los 100 km, 1 euro por km, que exceda de los 30, además de los 20 euros. 
    - Si sobrepasa los 100 km, 0,50 céntimos por km que exceda de los 100, 1 euro por km desde los 30 a los 100 y los 20 euros. Diseñar un programa que pida los kilómetros recorridos y calcule el total a pagar según la tarifa anterior. 


```
Algoritmo
    Definir Kilometros, Tarifa, Auxiliar_Kilometros Como Real;

    Leer Kilemetros;

    Si (Kilometros <= 30) Entonces
        Tarifa <- Kilometro * 20;
        Escribir "Kilometros Recorridos: ", Kilometros ," el monto a pagar es: ", Tarifa ," euros.";
    SiNo
        Si (Kilometros > 30) y (Kilometros <= 100) Entonces
            Auxiliar_Kilometros <- Kilometros - 30;
            Tarifa <- (Kilometros * 30) + Auxiliar_Kilometros;
            Escribir "Kilometros Recorridos: ", Kilometros ," el monto a pagar es: ", Tarifa ," euros.";
        SiNo
            Si (Kilometros > 100) Entonces
                Auxiliar_Kilometros <- Kilometros - 100;
                Tarifa <- (Kilometros * 30) + 70 + (Auxiliar_Kilometros * 0.50);
                Escribir "Kilometros Recorridos: ", Kilometros ," el monto a pagar es: ", Tarifa ," euros.";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

## Ejercicio 22

22.  Dados 3 números, informarlos en orden creciente.

```
Algoritmo
    Definir Numero1, Numero2, Numero3 Como Real;

    Leer Numero1, Numero2, Numero3;

    Si (Numero1 > Numero2) y (Numero2 > Numero3) Entonces
        Escribir Numero1, Numero2, Numero3;
    SiNo
        Si (Numero1 > Numero3) y (Numero3 > Numero2) Entonces
            Escribir Numero1, Numero3, Numero2;
        SiNo
            Si (Numero2 > Numero1) y (Numero1 > Numero3) Entonces
                Escribir Numero2, Numero1, Numero3;
            SiNo
                Si (Numero2 > Numero3) y (Numero3 > Numero1) Entonces
                    Escribir Numero2, Numero3, Numero1;
                SiNo
                    Si (Numero3 > Numero1) y (Numero1 > Numero2) Entonces
                        Escribir Numero3, Numero1, Numero2;
                    SiNo
                        Escribir Numero3, Numero2, Numero1;
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

## Ejercicio 23

23. De una prueba de nivel realizada a un alumno se conoce la cantidad total de preguntas realizadas y la cantidad de respuestas correctas. Informar el nivel registrado de acuerdo  a la siguiente escala:
- Muy Bueno si el porcentaje es mayor o igual a 90% 
- Bueno entre 70% y 90% 
- Regular entre 50% y 70% 
- Malo si el porcentaje es menor que 50% 

**version 1**

```
Algoritmo
    Definir Total, Correctas : Entero; 
    Definir Porcentaje : Real;

    Leer Total, Correctar;

    Porcentaje <- (Correctas * 100) / Total;

    Si (Porcentaje < 50) Entonces
        Escribir "Malo";
    SiNo
        Si (Porcentaje >= 50) y (Porcentaje < 70) Entonces
            Escribir "Regular";
        SiNo
            Si (Porcentaje >= 70) y (Porcentaje < 90) Entonces
                Escribir "Bueno";
            SiNo
                Escribir "Muy Bueno";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

## Ejercicio 24

24. Se realiza una encuesta de adaptación de tres productos (se ingresa el porcentaje de cada uno) y quiero determinar cual de ellos es el menos aceptado y el mas aceptado. Imprimir un mensaje indicando el nombre de los productos y sus porcentajes.

**version 1**
```
Algoritmo
    Definir Producto1, Producto2, Producto3 Como Cadena;
    Definir Porcentaje1, Porcentaje2, Porcentaje3 Como Real;

    Leer Producto1, Porcentaje1;
    Leer Producto2, Porcentaje2;
    Leer Producto3, Porcentaje3;

    Si (Porcentaje1 < Porcentaje2) y (Porcentaje2 < Porcentaje3) Entonces
        Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
        Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
    SiNo
        Si (Porcentaje1 < Porcentaje3) y (Porcentaje3 < Porcentaje2) Entonces
            Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";   
            Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%."; 
        SiNo
            Si (Porcentaje2 < Porcentaje1) y (Porcentaje1 < Porcentaje3) Entonces
                Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
            SiNo
                Si (Porcentaje2 < Porcentaje3) y (Porcentaje3 < Porcentaje1) Entonces
                    Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                    Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                SiNo
                    Si (Porcentaje3 < Porcentaje1) y (Porcentaje1 < Porcentaje2) Entonces
                        Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                        Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";
                    SiNo
                        Si (Porcentaje3 < Porcentaje2) y (Porcentaje2 < Porcentaje1) Entonces
                            Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                            Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Producto1, Producto2, Producto3 Como Cadena;
    Definir Porcentaje1, Porcentaje2, Porcentaje3 Como Real;

    Leer Producto1, Porcentaje1;
    Leer Producto2, Porcentaje2;
    Leer Producto3, Porcentaje3;

    Si (Porcentaje1 >= 0) y (Porcentaje2 >= 0) y (Porcentaje3 >= 0) Entonces
        Si (Porcentaje1 < Porcentaje2) y (Porcentaje2 < Porcentaje3) Entonces
            Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
            Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
        SiNo
            Si (Porcentaje1 < Porcentaje3) y (Porcentaje3 < Porcentaje2) Entonces
                Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";   
                Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%."; 
            SiNo
                Si (Porcentaje2 < Porcentaje1) y (Porcentaje1 < Porcentaje3) Entonces
                    Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                    Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
                SiNo
                    Si (Porcentaje2 < Porcentaje3) y (Porcentaje3 < Porcentaje1) Entonces
                        Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                        Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                    SiNo
                        Si (Porcentaje3 < Porcentaje1) y (Porcentaje1 < Porcentaje2) Entonces
                            Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                            Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";
                        SiNo
                            Si (Porcentaje3 < Porcentaje2) y (Porcentaje2 < Porcentaje1) Entonces
                                Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                                Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                            SiNo
                                Si (Porcentaje1 = Porcentaje2) y (Porcentaje2 < Porcentaje3) Entonces
                                    Escribir "Los productos ", Producto1 ," y ", Producto2 , " tienen un porcentaje de aceptacion de ", Porcentaje1;
                                    Escrbir "El producto ", Producto3 , " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
                                SiNo
                                    Si (Porcentaje1 = Porcentaje3) y (Porcentaje3 < Porcentaje2) Entonces
                                        Escribir "Los productos ", Producto1 ," y ", Producto2 , " tienen un porcentaje de aceptacion de ", Porcentaje1;
                                        Escrbir "El producto ", Producto3 , " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
                                    SiNo
                                        Escribir "Los productos ", Producto2 ," y ", Producto3 , " tienen un porcentaje de aceptacion de ", Porcentaje2;
                                        Escrbir "El producto ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                                    FinSi
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    SiNo
        Escribir "Los valores ingresado son incorrectos";
    FinSi
FinAlgoritmo
```

## Ejercicio 25

25. Se desea escribir el nombre del dia de la semana en funcion de un numero del dia, introducido por teclado, donde 1 es el Domingo, 2 es Lunes, y asi sucecivamente.


**version 1**
```
Algoritmo
    Definir Dia Como Entero;

    Leer Dia;

    Segun Dia Hacer
        1 : Escribir "Domingo";
        2 : Escribir "Lunes";
        3 : Escribir "Martes";
        4 : Escribir "Miercoles";
        5 : Escribir "Jueves";
        6 : Escribir "Viernes";
        7 : Escribir "Sabado";
    De otro modo:
        Escribir "Dato invalido.";
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Dia Como Entero;

    Leer Dia;

    Si (Dia = 1) Entonces
        Escribir "Domingo";
    SiNo
        Si (Dia = 2) Entonces
            Escribir "Lunes";
        SiNo
            Si (Dia = 3) Entonces
                Escribir "Martes";
            SiNo
                Si (Dia = 4) Entonces 
                    Escribir "Miercoles";
                SiNo
                    Si (Dia = 5) Entonces
                        Escribir "Jueves";
                    SiNo
                        Si (Dia = 6) Entonces
                            Escribir "Viernes";
                        SiNo
                            Si (Dia = 7) Entonces
                                Escribir "Sabado";
                            SiNo
                                Escribir "Dato invalido.";
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```
