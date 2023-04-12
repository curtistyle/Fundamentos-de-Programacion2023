# TP5 - Ciclos

## Ejercicio 1

1. Ingresar 5 pares de valores, en cada oportunidad emitir ambos valores y si ambos son positivos, emitir también su promedio.

**version 1** _(ciclo para)_
```
Algoritmo 
    Definir Numero1, Numero2, Promedio Como Real;
    Definir Indice Como Entero;

    Para Indice <- 1 Hasta 5 Hacer
        Leer Numero1, Numero2;
        Escribir Numero1, Numero2;

        Si (Numero1 > 0) y (Numero2 > 0) Entonces
            Promedio <- (Numero + Numero2) / 2;
            Escribir Promedio;
        FinSi
    FinPara
FinAlgoritmo
```

**version 2** _(ciclo mientras)_
```
Algoritmo
	Definir Numero1, Numero2, Promedio Como Real;
	Definir Indice Como Entero;
	
	Indice <- 1;
	
	Mientras  Indice <= 5 Hacer
		Leer Numero1, Numero2;
		Escribir Numero1, Numero2;

		Si (Numero1 > 0) y (Numero2 > 0) Entonces
			Promedio <- (Numero1 + Numero2) / 2;
			Escribir Promedio;
		FinSi
		Indice <- Indice + 0;
	FinMientras
FinAlgoritmo
```

**version 3** _(ciclo repetir...hasta)_
```
Algoritmo
	Definir Numero1, Numero2, Promedio Como Real;
	Definir Indice Como Entero;
	
	Indice <- 0;
	
	Repetir
		Indice <- Indice + 1;
		Leer Numero1, Numero2;
        Escribir Numero1, Numero2;
		
		Si (Numero1 > 0) y (Numero2 > 0) Entonces
			Promedio <- (Numero1 + Numero2) / 2;
			Escribir Promedio;
		FinSi
	Hasta Que Indice = 5;
FinAlgoritmo
```

## Ejercicio 2

2. Calcular la suma y el producto de los números pares comprendidos entre 20 y 500.

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Producto <- 1;
    Suma <- 0;
	
    Para Indice <- 20 Hasta 500 Hacer
        Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
    FinPara
FinAlgoritmo
```

**version 2** _(ciclo para)_
```
Algoritmo
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real; 
	
    Producto <- 1;
    Suma <- 0;
	
    Para Indice <- 20 Hasta 500 Con Paso 2 Hacer
		Suma <- Suma + Indice;
		Producto <- Producto * Indice;
    FinPara
	
    Escribir Suma, Producto;
FinAlgoritmo
```

**version 3** _(ciclo mientras)_

```
Algoritmo
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Indice <- 20;
    Producto <- 1;
    Suma <- 0;
	
    Mientras Indice <= 500 Hacer
        Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
        Indice <- Indice + 1;
    FinMientras
	
    Escribir Suma, Producto;
FinAlgoritmo
```

**version 4** _ciclo repetir...hasta_

```
Algoritmo
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Indice <- 19;
    Producto <- 1;
    Suma <- 0;
	
    Repetir
        Indice <- Indice + 1;
		Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
    Hasta Que Indice = 500;
	
    Escribir Suma, Producto;
FinAlgoritmo
```

## Ejercicio 3

3. Leer un lote de 475 valores de a uno por vez. Determinar y emitir el valor máximo del conjunto y el orden en que fue leído. Si hay más de un máximo considerar solo el primer valor hallado.

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Numero, Maximo, Indice, Orden Como Entero;
	
    Maximo <- 0;
    Para Indice <- 1 Hasta 475 Hacer
        
        Leer Numero;
		
        Si (Numero > Maximo) Entonces
            Maximo <- Numero;
            Orden <- Indice;
        FinSi
    FinPara
	
    Escribir "Valor maximo del lote es: ", Maximo ,", en el orden: ", Orden ,".";
```

**version 2** _(ciclo mientras)_
```
Algoritmo
	Definir Numero, Maximo, Indice, Orden Como Entero;
	
	Maximo <- 0;
	Indice <- 1;
	Mientras Indice <= 10 Hacer
		
        Leer Numero;
		
		Si (Numero > Maximo) Entonces
			Maximo <- Numero;
			Orden <- Indice;
		FinSi
		Indice <- Indice + 1;
	FinMientras
	
	Escribir "Valor maximo del lote es: ", Maximo ,", en el orden: ", Orden ,".";
FinAlgoritmo
```

**version 3** _(ciclo repetir...hasta)_
```
Algoritmo
	Definir Numero, Maximo, Indice, Orden Como Entero;
	
	Maximo <- 0;
	Indice <- 0;
	Repetir
		Indice <- Indice + 1;

		Leer Numero;
		
        Si (Numero > Maximo) Entonces
			Maximo <- Numero;
			Orden <- Indice;
		FinSi
	Hasta Que Indice = 475;
	
	Escribir "Valor maximo del lote es: ", Maximo ,", en el orden: ", Orden ,".";    
FinAlgoritmo
```

## Ejercicio 4

4. Ingresar un Nº y un carácter y mostrar dicho carácter repetido tantas veces como indica el Nº.


**version 1** _(ciclo para)_
```
Algoritmo
    Definir Numero, Indice Como Entero;
    Definir Letra Como Caracter;

    Leer Numero, Letra;

    Para Indice <- 1 Hasta Numero Hacer
        Escribir Letra;
    FinPara
FinAlgoritmo
```

**version 2** _(ciclo mientras)_

```
Algoritmo
    Definir Numero, Indice Como Entero;
    Definir Letra Como Caracter;

    Leer Numero, Letra;

    Indice <- 0;

    Mientras (Indice <= Numero) Hacer
        Escribir Letra;
        Indice <- Indice + 1;
    FinMientras
FinAlgoritmo
```

**version 3** _(ciclo repetir...hasta)_

```
Algoritmo
    Definir Numero, Indice Como Entero;
    Definir Letra Como Caracter;

    Leer Numero, Letra;

    Indice <- 0;

    Repetir
        Indice <- Indice + 1;
        Escribir Letra;
    Hasta Que (Indice = Numero)
FinAlgoritmo
```

## Ejercicio 5

5. Hacer un programa que lea 100 Números, indique cuáles son múltiplos de 2 y contarlos.

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Numero Como Real;
    Definir Indice, Contador Como Entero;

    Contador <- 0;
    Para Indice <- 1 Hasta 100 Hacer
        Leer Numero;
        Si ((Numero mod 2) = 0) Entonces
            Escribir "El numero ", Numero ," es multiplo de 2.";
            Contador <- Contador + 1;            
        FinSi
    FinPara
    Escribir "Cantidad de numeros multiplo de 2: ", Contador;
FinAlgoritmo
```

## Ejercicio 6 

6. Hacer un programa que lea 8 caracteres e indique que cantidad de ‘*’ y que cantidad de 
letras ‘a’ aparecen. 


## Ejercicio 7

7. ¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232?

## Ejercicio 8

8. Se  efectúa  una  encuesta  entre  1200  usuarios  de  sistemas  operativos.  Las  respuestas están  codificadas  como  1,  2  ó  3  según  sea  el  elegido.  Preparar  un  algoritmo  para ingresarle las 120 respuestas, y muestre por pantalla el número del sistema preferido

```
Algoritmo
    Definir IndiceA, IndiceB, Windows, MacOS, Linux, Opcion Como Entero;

    Windows <- 0;
    MacOS <- 0;
    Linux <- 0;

    Para IndiceA <- 1 Hasta 3 Hacer
        Escribir "Usuario (",1,"): ";
        Para IndiceB <- 1 Hasta 3 Hacer
            Escribir "Ingrese un numero, opcion: Windows (1), MacOS(2), Linux(3): "
            Leer Opcion;

            Segun Opcion Hacer
                1 : Windows <- Windows + 1;
                2 : MacOS <- MacOS + 1;
                3 : Linux <- Linux + 1;
            De Otro modo:
                
            FinSegun
        FinPara
    FinPara
    Para
FinAlgoritmo
```

