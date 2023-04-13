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

**version 1** _(ciclo para)_
```
Algoritmo
	Definir Contador1, Contador2, Indice Como Entero;
	Definir Letra Como Caracter;
	
	Para Indice <- 1 Hasta 8 Hacer
		Escribir  "Ingrese una letra: ";
		Leer Letra;
		Segun Letra Hacer
			"a" : Contador1 <- Contador1 + 1; 
			"*" : Contador2 <- Contador2 + 1;
		FinSegun
	FinPara
	
	Escribir "Contador de (a):", Contador1;
	Escribir "Contador de (b):", Contador2;
FinAlgoritmo
```
## Ejercicio 7

7. ¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232?

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Suma, Indice Como Entero;

    Suma <- 0;

    Para Indice <- 300 Hasta 1232 Hacer
        Si ((Indice mod 2) = 0) Hacer
            Suma <- Suma + Indice;
        FinSi
    FinPara

    Escribir "La suma de los numeros pares comprendidos de 300 a 1232 es: ", Suma;
FinAlgoritmo
```

## Ejercicio 8

8. Se  efectúa  una  encuesta  entre  1200  usuarios  de  sistemas  operativos.  Las  respuestas están  codificadas  como  1,  2  ó  3  según  sea  el  elegido.  Preparar  un  algoritmo  para ingresarle las 120 respuestas, y muestre por pantalla el número del sistema preferido

**version 1** _(ciclo para)_
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

## Ejercicio 9

9. Desarrollar un algoritmo que determine en un conjunto de 100 números: \
    a) - Cuántos son mayores que 15. \
    b) - Cuántos son mayores que 50. \
    c) - Cuántos están comprendidos entre 25 y 45. 

```
Algoritmo
    Definir Numero, Indice, ContadorA, ContadorB, ContadoC Como Entero;

    ContadorA <- 0;
    ContadorB <- 0;
    ContadorC <- 0;

    Para Indice <- Hasta 100 Hacer
        Leer Numero;

        Si (Numero > 15) Entonces
            ContadorA <- ContadorA + 1;
        FinSi
        Si (Numero > 50) Entonces
            ContadorB <- ContadorB + 1;
        FinSi
        Si (Numero >= 25) y (Numero <= 45) Entonces
            ContadorC <- ContadorC + 1;
        FinSi
    FinPara

    Escribir "Numeros mayores que 15: ", ContadorA;
    Escribir "Numeros mayores que 50: ", ContadorB;
    Escribir "Numeros comprendidos entre 25 y 45: ", ContadorC;
FinAlgoritmo
```

## Ejercicio 10

10. Obtener un algoritmo que permita calcular la siguiente serie: h(n)=1 + ½ + 1/3 + ... + 1/n.

```
Algoritmo
    Definir Indice, Serie, N  Como Entero;

    Serie <- 0;

    Leer N;

    Si (N > 0) Entonces
        Para Indice <- 1 Hasta N Hacer
            Serie <- Serie + 1/Indice;
        FinPara
    SiNo
        Escribir "N debe ser mayor que 0.";
    FinSi

    Escribir "El resultado de la serie es: ", Serie;
FinAlgoritmo
```

## Ejercicio 11

11. Se leen 50 pares de Números, c/u de los cuales tienen 2 valores: x e y distintos. Se pide contar en cuantos pares x > y, y en cuantos y > x.

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Indice, Numero1, Numero2, Contador1, Contador2 Como Entero;

    Contador1 <- 0;
    Contador2 <- 0;
    Contador3 <- 0;

    Para Indice <- 1 Hasta 50 Hacer
        Leer Numero1, Numero2;

        Si (Numero1 > Numero2) Entonces
            Contador1 <- Contador1 + 1;
        SiNo
            Si (Numero1 < Numero2) Entonces
                Contador2 <- Contador2 + 1;
            SiNo
                Escribir "El par de numero no puede ser igual."
            FinSi
        FinSi
    FinPara
    
    Escribir "Hay ", Contador1 ," pares donde X > Y.";
    Escribir "Hay ", Contador2 ," pares donde X < Y.";
FinAlgoritmo
```

## Ejercicio 12

12.  En un colegio de 1000 alumnos se ha registrado, para cada uno de ellos hay un código señalando  su  comportamiento  académico.  Dicho  código  puede  tomar  valores  1,  2  o  3. Indicar  cuántos  alumnos  obtuvieron  cada  una  de  las  calificaciones  tratando  de  a  una calificación por vez.

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Indice, Contador1, Contador2, Contador3, Numero Como Entero;

    Contador1 <- 0;
    Contador2 <- 0;
    Contador3 <- 0;

    Para Indice <- 1 Hasta 100 Hacer
        Escribir "Ingrese el nivel de comportamiento del alumno (1/2/3): ";
        Leer Numero;
        
        Segun Numero Hacer
            1 : Contador1 <- Contador1 + 1;
            2 : Contador2 <- Contador2 + 1;
            3 : Contador3 <- Contador3 + 1;
        FinSegun
    FinPara

    Escribir Contador1 ," alumnos obtuvieron la calificacion 1.";
    Escribir Contador2 ," alumnos obtuvieron la calificacion 2.";
    Escribir Contador3 ," alumnos obtuvieron la calificacion 3.";
FinAlgoritmo
```

## Ejercicio 13

13. En una fábrica hay 4.000 obreros distribuidos en cinco secciones. Se requiere determinar cuántos obreros hay y el promedio de edad de los mismos por cada sección. Asumir que se tiene como entrada los siguientes datos para cada obrero: Nº de empleado, sección a la que pertenece y edad. 

**version 1** _(ciclo para)_
```
Algoritmo
    Definir Empleado, Seccion, Total, Edad Como Entero;
    Definir Promedio Como Real;
    Definir Seccion1, Seccion2, Seccion3, Seccion4, Seccion5 Como Entero;
    Definir Edad1, Edad2, Edad3, Edad4, Edad5 Como Entero;

    Seccion1 <- 0;
    Seccion2 <- 0;
    Seccion3 <- 0;
    Seccion4 <- 0;
    Seccion5 <- 0;
    Edad1 <- 0;
    Edad2 <- 0;
    Edad3 <- 0;
    Edad4 <- 0;
    Edad5 <- 0;
    Total <- 4000;

    Para Empleado <- 1 Hasta Total Hacer
        Escribir "Ingrese la seccion a la que pertenece el obrero: ";
        Leer Seccion
        Segun Seccion Hacer
            1 : 
                Seccion1 <- Seccion1 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad1 <- Edad1 + Edad;
                Leer Edad;
            2 : 
                Seccion2 <- Seccion2 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad2 <- Edad2 + Edad;
                Leer Edad;
            3 : 
                Seccion3 <- Seccion3 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad3 <- Edad3 + Edad;
                Leer Edad;
            4 : 
                Seccion4 <- Seccion4 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad4 <- Edad4 + Edad;
                Leer Edad;
            5 : 
                Seccion5 <- Seccion5 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad5 <- Edad5 + Edad;
                Leer Edad;
        FinSegun
    FinPara
    
    Promedio <- Edad1 / Seccion1;
    Escribir "En la seccion 1 hay ", Seccion1 ," obreros y su promedio de edad es de : ", Promedio ," Años.";

    Promedio <- Edad2 / Seccion2;
    Escribir "En la seccion 2 hay ", Seccion2 ," obreros y su promedio de edad es de : ", Promedio ," Años.";

    Promedio <- Edad3 / Seccion3;
    Escribir "En la seccion 3 hay ", Seccion3 ," obreros y su promedio de edad es de : ", Promedio ," Años.";

    Promedio <- Edad4 / Seccion4;
    Escribir "En la seccion 4 hay ", Seccion4 ," obreros y su promedio de edad es de : ", Promedio ," Años.";

    Promedio <- Edad5 / Seccion5;
    Escribir "En la seccion 5 hay ", Seccion5 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
FinAlgoritmo
```

## Ejercicio 14

14. Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales hasta el Nº 10. 
 - Ej : \
    5 por 1 es 5  \
    5 por 2 es 10 \
    5 por 3 es 15 

```
Algoritmo
    Definir IndiceA, IndiceB, Producto Como Entero;

    Para IndiceA <- 1 Hasta 10 Hacer
        Escribir "Tabla de multiplicar del ", IndiceA ,".";
        Para IndiceB <- Hasta 10 Hacer
            Producto <- IndiceA * IndiceB;
            Escribir IndiceA " por ", IndiceB ," es: ", Producto;
        FinPara
    FinPara
FinAlgoritmo
```

## Ejercicio 15

15. Construir  un  algoritmo  que  muestre  por  pantalla  las  tablas  de  multiplicar  usuales  para  valores comprendidos entre a y b. (a < b).

```
Algoritmo
    Definir NumeroA, NumeroB, IndiceA, IndiceB, Producto Como Entero

    Escribir "Ingrese el rango para desarrollar la tabla.";
    Escribir "A: ";
    Leer NumeroA;
    Escribir "B: ";
    Leer NumeroB;

    Si (NumeroA > NumeroB) Entonces
        Para IndiceA <- NumeroA Hasta NumeroB Hacer
            Escribir ">Tabla de multiplicar del ", IndiceA ,".<"
            Para IndiceB <- 1 Hasta 10 Hacer
                Producto <- IndiceA * IndiceB;
                Escribir IndiceA ," por ", IndiceB ," es igual a ", Producto;
            FinPara
        FinPara
    FinSi
FinAlgoritmo
```
