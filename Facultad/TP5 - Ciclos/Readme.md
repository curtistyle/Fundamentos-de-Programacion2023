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

## Ejercicio 16

16. Dada una secuencia de caracteres acabada en #, mostrar los números (0..9) que en ella aparecen.

```
Algoritmo
	Definir Letra Como Caracter;
	Definir Contador Como Entero;
	
	Contador <- 0;
	
	Repetir
		Escribir " > Ingrese un catacter: ";
		Leer Letra;
		Si (Letra > '0') y (Letra < '9') Entonces
			Contador <- Contador + 1;
		FinSi
	Hasta Que (Letra = '#')
	
	Escribir "Los caracteres comprendidos entre 0..9 aparecen: ", Contador ," veces.";
FinAlgoritmo
```

## Ejercicio 17

17. Construir  un  algoritmo  que,  dada  una  secuencia  de  enteros  acabada  con  el  valor  cero, devuelva el mayor de ellos. Determinar cuántos números negativos han aparecido.

***revisar***

```
Algoritmo
    Definir Numero, Maximo, Contador Como Entero;

    Maximo <- 0;

    Repetir
        Leer Numero;

        Si (Numero > Maximo) Entonces
            Maximo <- Numero;
        FinSi
        Si (Numero < 0) Entonces
            Contador <- Contador + 1;
        FinSi
    Hasta Que (Numero = 0)

    Escribir "El maximo de los numeros ingresado es: ", Maximo;
    Escribir "La cantidad de numeros negativos: ", Contador;
FinAlgoritmo
```

**version 2**

```
Algoritmo
    Definir Numero, Maximo, Contador Como Entero;

    Contador <- 0;

    Leer Numero;
    Maximo <- Numero;
    Mientras (Numero <> 0) Hacer
        Si (Numero > Maximo) Entonces
            Maximo <- Numero;
        FinSi
        Si (Numero < 0) Entonces
            Contador <- Contador + 1;
        FinSi
        Leer Numero;
    FinMientras

    Escribir "El maximo de los numeros ingresado es: ", Maximo;
    Escribir "La cantidad de numeros negativos: ", Contador;
FinAlgoritmo 
```

## Ejercicio 18 

18. Dada una secuencia de caracteres acabada en punto, obtener un algoritmo que determine cuantas veces aparece un determinado carácter, el cual será leído previamente. 

```
Algoritmo
    Definir Letra, Ocurrencia Como Cadena;
    Definir Contador Como Entero;

    Contador <- 0;
    
    Escribir "Ingrese el caracter que desea que se cuente: ";
    Leer Ocurrencia;

    Repetir 
        Escribir "Ingrese una letra: ";
        Leer Letra;
        Si (Letra = Ocurrencia) Entonces
            Contador <- Contador + 1;
        FinSi
    Hasta Que (Letra = '.')

    Escribir "El caracter ", Ocurrencia , " se repitio ", Contador ," veces.";
FinAlgoritmo
```

## Ejercicio 19

19. Contar la cantidad de Números negativos de una lista que finaliza con el Nº 0.

```
Algoritmo
    Definir Indice, Numero Como Entero;

    Leer Numero;
    Para Indice <- Numero Hasta 0 Hacer
        Escribir " > ", Indice;
    FinPara
FinAlgoritmo
```

## Ejercicio 20

20. Escribir  un  algoritmo  que  permita  leer  una  serie  de  enteros.  Contar  el  Nº  de  valores  introducidos y su suma. 

```
Algoritmo
    Definir Numero, Suma, Contador Como Entero;

    Suma <- 0;
    Contador <- 0;

    Escribir "Ingrese una serie de numeros (termina el ciclo con -1): ";

    Repetir
        Leer Numero;
        Suma <- Suma + Numero;
        Contador <- Contador + 1;
    Hasta Que (Numero = -1)

    Escribir "Cantidad de numeros introducidos: ", Contador;
    Escribir "Suma de los numeros introducidos: ", Suma;
FinAlgoritmo
```

## Ejercicio 21

21. Dada la siguiente situación: se dispone de un mazo de cartas españolas. Se debe sacar la primera carta y separarla. Luego sacar de a una carta por vez hasta encontrar una del mismo palo y número mayor a la primera. El problema planteado es determinar cuántas cartas fue necesario extraer del mazo.

**version 1** _(ciclo Repetir..Hasta que)_
```
Algoritmo
    Definir Numero, AuxNumero, Indice Como Entero;
    Definir Palo, AuxPalo Como Cadena;
	
    Indice <- 0;
	
    Repetir 
        Escribir "Ingrese una carta. ";
        Leer Numero, Palo;
		
        Si (Indice = 0) Entonces
			Escribir "Se separo del mazo el ", Numero ," de ", Palo ,".";
            AuxPalo <- Palo;
            AuxNumero <- Numero + 1;
        FinSi
		Indice <- Indice + 1;
    Hasta Que ((AuxPalo = Palo) y (AuxNumero = Numero))
	
    Escribir "Fueron necesario sacar ", Indice - 1," cartas del mazo.";
FinAlgoritmo
```

## Ejercicio 22

22. Dada una lista de valores numéricos, hallar su rango, es decir la diferencia entre su valor máximo y su valor mínimo. 

```
Algoritmo
    Definir Numero, Maximo, Minimo, Indice Como Entero;
    Definir Control Como Logico;

    Control <- Falso;
    Indice <- 0;
    Maximo <- 0;
    Minimo <- 0;

    Repetir
        Leer Numero;

        Si (Control = Falso) Entonces
            Minimo <- Numero;
            Control <- Verdadero;
        FinSi

        Si (Numero > Maximo) Entonces
            Maximo <- Maximo;
        SiNo
            (Numero < Minimo) Entonces
            Minimo <- Numero;
        FinSi
    Hasta Que (Numero = 0)
    
    Escribir "Maximo: ", Maximo ," Minimo: ", Minimo;
FinAlgoritmo
```

## Ejercicio 23

23. Dada una lista de valores enteros positivos, hallar cuántos valores mayores que 1.000 hay. Si la cantidad es menor que 20 calcular su factorial.

**version 1** _(Repetir..Hasta que)_

```
Algoritmo
    Definir Numero, Indice, Maximo, Contador, Factorial Como Entero;
	
    Factorial <- 1;
    Contador <- 0;
	
    Repetir
		Escribir "Ingrese un numero: ";
        Leer Numero;
		
        Si (Numero > 0) Entonces
            Si Numero > 1000 Entonces
                Contador <- Contador + 1;
			FinSi
		FinSi
	Hasta Que (Numero = 0)
		
	Si (Contador < 20) Entonces
		Para Indice <- 1 Hasta Contador Hacer
			Factorial <- Factorial * Indice;         
		FinPara    
	FinSi
	
	Escribir "Hay ", Contador ," valores mayores a 1000.";
	Si (Contador < 20) Entonces
		Escribir "El factorial de ", Contador , " es ", Factorial ,".";
	FinSi
FinAlgoritmo
```

## Ejercicio 24

24. Se dispone de un conjunto de tarjetas rojas y azules, las cuales están numeradas en forma correlativa. El lote de tarjetas termina con una tarjeta blanca. El problema es determinar de  las  tarjetas  del  lote:  cuántas  son  azules  y  con  número  par;  cuántas  son  rojas  y  con número impar, y cuántas son las restantes (excepto la blanca). 

```
Algoritmo
    Definir Indice, Par, Impar, Contador Como Entero;
    Definir Tarjeta Como Cadena;
	
    Contador <- 0;
    Indice <- 0;
    Par <- 0;
    Impar <- 0;
	
	Escribir "Ingrese el lote de Cartas Rojas y Azules, (Blanca para terminar el ciclo).";
    Repetir
        Indice <- Indice + 1;
        Escribir "(", Indice ,") Ingresar el color de la tarjeta (roja/azul): ";
        Leer Tarjeta;
		
        Si (Tarjeta = 'Roja') o (Tarjeta = 'roja') Entonces
            Si ((Indice mod 2) = 0) Entonces
                Par <- Par + 1;
            FinSi
        SiNo
            Si (Tarjeta = 'Azul') o (Tarjeta = 'azul') Entonces
				Si ((Indice mod 2) <> 0) Entonces
					Impar <- Impar + 1;
				FinSi
			SiNo
				Si (Tarjeta = 'Blanca') o (Tarjeta = 'blanca') Entonces
					Indice <- Indice - 1;
				SiNo
					Escribir "Dato Invalido";
					Indice <- Indice - 1;
				FinSi
			FinSi
			
		FinSi
	Hasta Que ((Tarjeta = 'Blanca') o (Tarjeta = 'blanca'))
		
    Escribir "El Nº de Tarjetas Rojas y Pares: ", Par;
    Escribir "El Nº de Tarjetas Azules e Impares: ", Impar;
    Escribir "El resto de tarjetas: ", (Indice - (Par + Impar));
FinAlgoritmo
```

## Ejercicio 25

25. Dada  una  lista  de  precios  de  productos,  la  cual  termina  con  un  precio  igual  a  cero.  Se desea saber el monto total a pagar y la cantidad de artículos comprados. 

```
Algoritmo
    Definir Indice Como Entero;
    Definir Monto, MontoTotal Como Real;
	
    Indice <- 0;
	
    Escribir "Ingrese la lista de precios.";
	
	Repetir
		Indice <- Indice + 1;
		Escribir "Monto del poducto (", Indice ,"): ";
		Leer Monto;
		MontoTotal <- MontoTotal + Monto;
	Hasta Que (Monto = 0)

    Escribir "Cantidad de productos: ", Indice ,".";
    Escribir "Monto Total a pagar: $", MontoTotal ,".";
FinAlgoritmo
```

## Ejercicio 26

26. Tenemos una empresa que necesita incorporar a su plantilla varios empleados en diversos departamentos.  Se  reciben  multitud  de  Currículum  Vitae  y  se  intenta  introducir  en  una pequeña  aplicación  para  realizar  una  primera  selección  y  en  base  a  su  resultado, comprobaremos si es apto o no apto para optar al cargo.  
    **Necesita la empresa:** 
    - Un administrativo. 
    - Un transportista. 
    - Dos operarios. 
    - Tres guardias de seguridad. 
        - *Para todos los puestos tienen que tener 18 años.*
        - Para **Administrativo** y **Transportista** pueden tener hasta 55 años. 
        - Para **Operarios** no pueden superar los 50 años. 
        - Para **Guardia de Seguridad** no pueden superar los 45 años. 
        - Para **Administrativo** se requiere el Ciclo superior en Administración y Finanzas. 
        - Para los demás puestos el titulo secundario. 
 
Una vez haya superado los requerimientos anteriores, introduciremos el nombre, 
apellidos, dirección y número de DNI.

**version 1**
```
Algoritmo
    Definir Administrativo, Transportista, Operario, Guardia Como Entero;
    Definir Indice, Edad Como Entero;
    Definir Opcion, Titulo, Nombre, Apellido, Direccion, DNI Como Cadena;
    Definir Condicion Como Logico;

    Administrativo <- 0;
    Transportis <- 0;
    Operario <- 0;
    Guardia <- 0;
    Condicion <- Verdadero;

    Repetir 
        Escribir "Seleccione el rol que desea evaluar: ";
        Escribir "  > Administrativo (1). ";
        Escribir "  > Transportista  (2). ";
        Escribir "  > Operario       (3). ";
        Escribir "  > Guaria de Seg. (4). ";
        Escribir "  > SALIR          (0). "; 
        Leer Opcion;

        Si ((Administrativo < 1) y (Opcion = 1)) Entonces
            Escribir "Ingrese la edad: ";
            Leer Edad;
            Si ((Edad >= 18) y (Edad <= 55)) Entonces
                Escribir "Titulo: Secundario (s/n): ";
                Leer Titulo;
                Si (Titulo = 's') Entonces
                    Escribir "Titulo: Ciclo Superior en Administracion y Finanzas (s/n):";
                    Leer Titulo;
                    Si (Titulo = 's') Entonces
                        Escribir "Se superaron los requisitos. Usted esta capacitado para ejercer la profesión de Administrativo.";
                        Condicion <- Verdadero;
                        Administrativo <- Administrativo + 1;
                    SiNo
                        Esribir "No posee el Titulo: Administracion y Finanzas.";
                    FinSi
                SiNo
                    Condicion <- Falso;
                    Escribir "No posee Titulo: Secundario.";    
                FinSi
            SiNo
                Condicion <- Falso;
                Escribir "No esta en el rango de edad."
            FinSi
        SiNo
            Escribir "El Puesto de Administrativo esta ocupado";
        FinSi

        Si ((Transportista < 1)y (Opcion = 2)) Entonces
            Escribir "Ingrese la edad: ";
            Leer Edad;
            Si ((Edad >= 18) y (Edad <= 55)) Entonces
                Escribir "Titulo: Secundario (s/n): ";
                Leer Titulo;
                Si (Titulo = 's') Entonces     
                    Escribir "Se superaron los Requisitos. Esta capacitado para ejercer la profesión de Transportista.";
                    Condicion <- Verdadero;
                    Transportista <- Transportista + 1;
                SiNo
                    Condicion <- Falso;
                    Escribir "No posee Titulo: Secundario.";    
                FinSi
            SiNo
                Condicion <- Falso;
                Escribir "No esta en el rango de edad."
            FinSi
        SiNo
            Escribir "El Puesto de Transportista esta ocupado";
        FinSi

        Si ((Operario < 2) y (Opcion = 3)) Entonces
            Escribir "Ingrese la edad: ";
            Leer Edad;
            Si ((Edad >= 18) y (Edad <= 50)) Entonces
                Escribir "Titulo: Secundario (s/n): ";
                Leer Titulo;
                Si (Titulo = 's') Entonces     
                    Escribir "Se superaron los Requisitos. Esta capacitado para ejercer la profesión de Operario.";
                    Condicion <- Verdadero;
                    Operario <- Operario + 1;
                SiNo
                    Condicion <- Falso;
                    Escribir "No posee Titulo: Secundario.";    
                FinSi
            SiNo
                Condicion <- Falso;
                Escribir "No esta en el rango de edad."
            FinSi
        SiNo
            Escribir "El Puesto de Operario esta ocupado";
        FinSi

        Si ((Guardia < 3) y (Opcion = 4)) Entonces
            Escribir "Ingrese la edad: ";
            Leer Edad;
            Si ((Edad >= 18) y (Edad <= 50)) Entonces
                Escribir "Titulo: Secundario (s/n): ";
                Leer Titulo;
                Si (Titulo = 's') Entonces     
                    Escribir "Se superaron los Requisitos. Esta capacitado para ejercer la profesión de Guardia de Seguridad.";
                    Condicion <- Verdadero;
                    Guardia <- Guardia + 1;
                SiNo
                    Condicion <- Falso;
                    Escribir "No posee Titulo: Secundario.";    
                FinSi
            SiNo
                Condicion <- Falso;
                Escribir "No esta en el rango de edad."
            FinSi
        SiNo
            Escribir "El Puesto de Operario esta ocupado";
        FinSi

        Si (Condicion = Verdadero) Entonces
            Escribir "Ingrese el Nombre: ";
            Leer Nombre;
            Escribir "Ingrese el apellido: ";
            Leer Apellido;
            Escribir "Ingrese la Direccion: ";
            Leer Direccion;
            Escribir "Ingrese el DNI: ";
            Leer DNI;
        SiNo
            Escribir "No supero los requisitos.";
        FinSi
        Condicion <- Falso;
    Hasta Que (Indice)
FinAlgoritmo
```

**version 2**
```
Algoritmo
    Definir Administrativo, Transportista, Operario, Guardia Como Entero;
    Definir Edad Como Entero;
    Definir Opcion, TituloSecundario, TituloTerciario, Nombre, Apellido, Direccion, DNI Como Cadena;
    Definir Condicion Como Logico;

    Administrativo <- 0;
    Transportista <- 0;
    Operario <- 0;
    Guardia <- 0;

    Repetir

        Leer Opcion;

        Leer Edad;
        Leer TituloSecundario;

        Si (Opcion = 1) Entonces
            Leer TituloTerciario;
        FinSi
        
        Si (Edad >= 18) Entonces
            Si (TituloSecundario = 's') Entonces
                Si (Edad <= 55) Entonces
                    Si (Opcion = 1) y (TituloTerciario = 's') y (Administrativo < 1) Entonces
                        Administrativo = Administartivo + 1;
                        Condicion <- Verdadero;
                    SiNo
                        Si (Opcion = 2) y (Transportista < 1) Entonces
                            Transportista <- Transportista + 1;
                            Condicion <- Verdadero;
                        SiNo
                            Si (Opcion = 3) y (Operario < 2) y (Edad <= 50) Entonces
                                Operario <- Operario + 1;
                                Condicion <- Verdadero;
                            SiNo
                                Si (Opcion = 4) y (Guardia < 3) y (Edad <= 45) Entonces
                                    Guardia <- Guardia + 1;
                                    Condicion <- Verdadero;
                                FinSi
                            FinSi
                        FinSi
                    FinSi    
                FinSi
            FinSi
        FinSi

        Si (Condicion = Verdadero) Entonces
            Leer Nombre;
            Leer Apellido;
            Leer Direccion;
            Leer DNI;
        FinSi
        Condicion <- Falso;
    Hasta Que (Opcion = 0)
FinAlgoritmo
```

*version 3*

```
Algoritmo
    Definir Administrativo, Transportista, Operario, Guardia Como Entero;
    Definir Edad Como Entero;
    Definir Opcion, TituloSecundario, TituloTerciario, Nombre, Apellido, Direccion, DNI Como Cadena;
    Definir Condicion Como Logico;

    Administrativo <- 0;
    Transportista <- 0;
    Operario <- 0;
    Guardia <- 0;

    Repetir
        Escribir "Seleccione el rol que desea evaluar: ";
        Escribir "  > Administrativo (1). ";
        Escribir "  > Transportista  (2). ";
        Escribir "  > Operario       (3). ";
        Escribir "  > Guaria de Seg. (4). ";
        Escribir "  > SALIR          (0). "; 
        Leer Opcion;

        Si (Opcion > 0) y (Opcion < 5) Entonces
            Escribir "Ingerse la Edad: ";
            Leer Edad;
            Escribir "Ingrese si posee el Titulo: Secundario (s/n): "
            Leer TituloSecundario;

            Si (Opcion = 1) Entonces
                Escribir "Ingrese si posee el Titulo: Administración y Finanzas (s/n): "
                Leer TituloTerciario;
            FinSi
            
            Si (Edad >= 18) y (Edad <= 55) Entonces
                Si (TituloSecundario = 's') Entonces            
                    Si (Opcion = 1) y (TituloTerciario = 's') y (Administrativo < 1) Entonces
                        Administrativo = Administartivo + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Administrativo.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si (Opcion = 2) y (Transportista < 1) Entonces
                        Transportista <- Transportista + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Transportista.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si (Opcion = 3) y (Operario < 2) y (Edad <= 50) Entonces
                        Operario <- Operario + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Operario."
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si (Opcion = 4) y (Guardia < 3) y (Edad <= 45) Entonces
                        Guardia <- Guardia + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Guardia de seguridad.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi               
                FinSi
            FinSi

            Si (Condicion = Verdadero) Entonces
                Escribir "Ingrese el nombre: ";
                Leer Nombre;
                Escribir "Ingrese el apellido: ";
                Leer Apellido;
                Escribir "Ingrese la direccion: ";
                Leer Direccion;
                Escribir "Ingrese el DNI: ";
                Leer DNI;
            FinSi
            Condicion <- Falso;
        SiNo
            Si (Opcion > 4) Entonces
                Escribir "Opcion incorrecta.":
            FinSi
        FinSi
    Hasta Que (Opcion = 0)   
FinAlgoritmo
```