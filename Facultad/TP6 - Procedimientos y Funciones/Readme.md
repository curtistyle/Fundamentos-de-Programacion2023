# Procedimientos y Funciones

### Ejercicio 1

1. Escribir un procedimiento Geometría tal que dado el alto y ancho de un rectángulo calcule
el área.

*Procedimiento*
```
Procedimiento Area(Alto, Ancho : Real ; VAR Resultado : Real)
	Resultado <- Alto * Ancho;
FinProcedimiento

Algoritmo 
	Definir Alto, Ancho, Resultado Como Real;
		
	Escribir "Ingrese la alura del rectangulo: ";
	Leer Alto;
	Escribir "Ingrese el ancho del rectangulo: ";
	Leer Ancho;
		
	Area(Alto, Ancho, Resultado);
		
	Escribir "El area del rectango es: ", Resultado;
FinAlgoritmo
```
*Funcion*
```
Funcion Area(Alto, Ancho : Real) : Real;
	Area <- Alto * Ancho;
FinFuncion

Algoritmo
	Definir Alto, Ancho Como Real;

	Escribir "Ingrese la altura del rectangulo: ";
	Leer Alto;
	Escribir "Ingrese el ancho del rectangulo: ";
	Leer Ancho;

	Escribir "El Area del rectangulo es: ", Area(Alto,Ancho);
FinAlgoritmo
```

### Ejercicio 2

1. Ídem para el perímetro.

*Procedimiento*
```
Procedimiento Perimetro(Alto, Ancho : Real ; VAR Resultado : Real)
	Resultado <- (Alto*2) + (Ancho*2);
FinProcedimiento

Algoritmo
	Definir Alto, Ancho, Resultado Como Real;

	Escribir "Ingrese el alto del rectangulo: ";
	Leer Alto;
	Escribir "Ingrese el ancho del rectangulo: ";
	Leer Ancho;

	Perimetro(Alto,Ancho,Resultado);

	Escribir "El perimetro del rectangulo es ", Resultado;
	
FinAlgoritmo
```
*Funcion*
```
Funcion Perimetro(Alto, Ancho : Real) : Real;
	Perimetro <- (Alto*2) + (Ancho*2);
FinFuncion

Algoritmo
	Definir Alto, Ancho Como Real;

	Escribir "Ingrese el alto del rectangulo: ";
	Leer Alto;
	Escribir "Ingrese el ancho del rectangulo: ";
	Leer Ancho;

	Escribir "El perimetro del rectangulo es ", Perimetro(Alto,Ancho);
FinAlgoritmo
```

### Ejercicio 8

1. Escribir  un  programa  que,  utilizando  procedimientos  con  parámetros,  lea  desde  el
teclado  las  unidades  y  el  precio  que  quiere  comprar,  y  en  función  de  las  unidades
introducidas le haga un descuento o no.

*Procedimiento*
```
Procedimiento Generar_Descuento(Total, Descuento : Real ; VAR Resultado : Real)
	Definir Aux Como Real;

	Aux <- (Total * Descuento) / 100;
	Resultado <- Total - Aux;
FinProcedimiento

Algoritmo ejercicio8
	Definir Cantidad Como Entero;
	Definir Monto, Total, Descuento, Resultado Como Real;
	Definir Opcion Como Caracter;

	Escribir "Ingrese la cantidad de items que desea comprar: ";
	Leer Cantidad;
	Escribir "Ingrese el monto de cada item.";
	Leer Monto;
	Escribir "Quiere hacer un descuento (s/n): "
	Leer Opcion;

	Total <- Monto * Cantidad;

	Si (Opcion = 's') o (Opcion = 'S') Entonces
		Escribir "Ingrese el descuento (%): ";
		Leer Descuento;
		Generar_Descuento(Total, Descuento, Resultado);
		Escribir "Usted debe pagar $", Resultado;
	SiNo
		Escribir "Usted debe pagar $", Total;
	FinSi
FinAlgoritmo
```

*Funcion*
```
Funcion Generar_Descuento(Total, Descuento : Real) : Real;
Definir Aux Como Real;

Aux <- (Total * Descuento) / 100;
Generar_Descuento <- Aux - Total;
FinFuncion

Algoritmo ejercicio8
	Definir Cantidad Como Entero;
	Definir Monto, Total, Descuento Como Real;
	Definir Opcion Como Caracter;

	Escribir "Ingrese la cantidad de items que desea comprar: ";
	Leer Cantidad;
	Escribir "Ingrese el monto de cada item.";
	Leer Monto;
	Escribir "Quiere hacer un descuento (s/n): "
	Leer Opcion;

	Total <- Monto * Cantidad;

	Si (Opcion = 's') o (Opcion = 'S') Entonces
		Escribir "Ingrese el descuento (%): ";
		Leer Descuento;
		Escribir "Usted debe pagar $", Generar_Descuento(Total, Descuento);
	SiNo
		Escribir "Usted debe pagar $", Total;
	FinSi
FinAlgoritmo
```
### Ejercicio 9

1. Escribir una función par tal que indique si un número es par o impar.

*Procedimiento*
```
Procedimiento Determinar_Paridad(Numero : Entero, VAR Paridad : Entero)
	Paridad <- Numero mod 2;
FinProcedimiento

Algoritmo
	Definir Numero, Paridad Como Entero;

	Escribir "Ingrese un numero: ";
	Leer Numero;

	Mientras (Numero <> 0) Hacer
		Determinar_Paridad(Numero,Paridad);

		Si (Paridad = 0) Entonces
			Escribir "El numero es Par.";
		SiNo
			Escribir "El numero es impar.";	
		FinSi	

		Escribir "Ingrese un numero: ";
		Leer Numero;
	FinMientras
FinAlgoritmo
```
*Funcion*
```
Funcion Determinar_Paridad(Numero : Entero) : Entero;
	Determinar_Paridad <- Numero mod 2;
FinFuncion

Algoritmo
	Definir Numero Como Entero;

	Escribir "Ingrese un numero: ";
	Leer Numero;

	Mientras (Numero <> 0) Hacer		

		Si (Determinar_Paridad(Numero) = 0) Entonces
			Escribir "El numero es Par.";
		SiNo
			Escribir "El numero es impar.";	
		FinSi	

		Escribir "Ingrese un numero: ";
		Leer Numero;

	FinMientras
FinAlgoritmo
```

### Ejercicio 10

1. Escribir una función que tenga un parámetro de tipo entero y que devuelva la letra P si el Nº es positivo y N si es negativo o cero.

*Procedimiento*
```
Procedimiento Determinar_Signo(Numero : Entero ; VAR Signo : Caracter)
	Si (Numero >= 0) Entonces
		Signo <- 'P';
	SiNo
		Signo <- 'N';
	FinSi
FinProcedimiento

Algoritmo ejercicio10
	Definir Numero Como Entero;
	Definir Signo Como Caracter;

	Escribir "Ingrese un numero: ";
	Leer Numero;
	
	Determinar_Signo(Numero, Signo);

	Escribir "El numero es: ", Signo;
FinAlgoritmo
```

*Funcion*

```
Funcion Determinar_Signo(Numero : Entero) : Caracter;
	Si (Numero >= 0) Entonces
		Determinar_Signo <- 'P';
	SiNO
		Determinar_Signo <- 'N';
	FinSi
FinFuncion

Algoritmo ejercicio10
	Definir Numero Como Entero;
	Definir Signo Como Caracter;

	Escribir "Ingrese un numero: ";
	Leer Numero;
	
	Escribir "El signo del numero es: ", Determinar_Signo(Numero);;
FinAlgoritmo
```

### Ejercicio 11

1. Escribir una función lógica de dos parámetros enteros que devuelva True si uno divide al
otro y False en caso contrario.

*Procedimiento*
```
Procedimiento Determinar_Divisibilidad(Numero1, Numero2 : Entero ; VAR Divisible : Logico)
	Definir Aux Como Entero;
	Aux <- Numero1 mod Numero2;
	Si (Aux = 0) Entonces
		Divisible <- Verdadero;
	SiNo
		Divisible <- Falso;
	FinSi
FinProcedimiento

Algoritmo ejercicio11
	Definir Numero1, Numero2 Como Entero;
	Definir Divisible Como Logico;
	
	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2; 
	
	Determinar_Divisibilidad(Numero1, Numero2, Divisible);
	
	Si (Divisible = Verdadero) Entonces
		Escribir "El ", Numero1 , " es divisible por el numero ", Numero2; 
	SiNo
		Escribir "El ", Numero1 , " no es divisible por el numero ", Numero2; 
	FinSi
FinAlgoritmo
```
*Funcion*
```
Procedimiento Determinar_Divisibilidad(Numero1, Numero2 : Entero) : Logico;
	Definir Aux Como Entero;
	Aux <- Numero1 mod Numero2;
	Si (Aux = 0) Entonces
		Determinar_Divisibilidad <- Verdadero;
	SiNo
		Determinar_Divisibilidad <- Falso;
	FinSi
FinProcedimiento

Algoritmo ejercicio11
	Definir Numero1, Numero2 Como Entero;
	Definir Divisible Como Logico;
	
	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2; 
	
	Divisible <- Determinar_Divisibilidad(Numero1, Numero2);
	
	Si (Divisible = Verdadero) Entonces
		Escribir "El ", Numero1 , " es divisible por el numero ", Numero2; 
	SiNo
		Escribir "El ", Numero1 , " no es divisible por el numero ", Numero2; 
	FinSi
FinAlgoritmo
```

### Ejercicio 12

1. Escribir un procedimiento digito, que determine si un carácter es uno de los dígitos de 0 a 9.

*Procedimiento*

```
Procedimiento Determinar_Digito(Numero : Caracter ; VAR Resultado : Logico)
	Si (Numero >= 0) y (Numero <= 9) Hacer
		Resultado <- Verdadero;
	SiNo
		Resultado <- Falso;
	FinSi
FinProcedimiento

Algoritmo ejercicio19
	Definir Numero Como Caracter;
	Definir Resultado Como Logico;

	Escribir "Ingrese un numero: ";
	Leer Numero;

	Determinar_Digito(Numero, Resultado);

	Si (Resultado = Verdadero) Entonces
		Escribir "El numero que ingreso esta en el rango de 0 a 9.";
	SiNo
		Escribir "El numero que ingreso no esta en el rango de 0 a 9.";
	FinSi
FinAlgoritmo
```

*Funcione*

```
Funcion Determinar_Digito(Numero : Entero) : Logico;
	Si (Numero >= 0) y (Numero <= 9) Hacer
		Determinar_Digito <- Verdadero;
	SiNo
		Determinar_Digito <- Faldo;
	FinSi
FinFuncion

Algoritmo ejercicio19
	Definir Numero Como Entero;
	Definir Resultado Como Logico;

	Escribir "Ingrese un numero: ";
	Leer Numero;

	Resultado <- Determinar_Digito(Numero);

	Si (Resultado = Verdadero) Entonces
		Escribir "El numero que ingreso esta en el rango de 0 a 9.";
	SiNo
		Escribir "El numero que ingreso no esta en el rango de 0 a 9.";
	FinSi
FinAlgoritmo
```

### Ejercicio 13

1. Escribir una función lógica vocal que determine si un carácter es una vocal.

*Procedimiento*
```
Procedimiento Determinar_Vocal(Letra : Caracter ; VAR Resultado : Logico)
	Segun Letra Hacer
		'a' : Resultado <- Verdadero;
		'e' : Resultado <- Verdadero;
		'i' : Resultado <- Verdadero;
		'o' : Resultado <- Verdadero;
		'u' : Resultado <- Verdadero;
	De Otro Modo:
		Resultado <- Falso;
	FinSegun
FinProcedimiento

Algoritmo ejercicio13
	Definir Letra Como Caracter;
	Definir Resultado Como Logico;

	Escribir "Ingrese una letra: ";
	Leer Letra;
	
	Determinar_Vocal(Letra, Resultado);
	
	Si (Resultado = Verdadero) Entonces
		Escribir "La letra que ingreso esta entre las vocales.";
	SiNo
		Escribir "La letra que ingreso no esta entre las vocales.";
	FinSi
FinAlgoritmo
```
*Funcion*
```
Procedimiento Determinar_Vocal(Letra : Caracter) : Logico;
	Segun Letra Hacer
		'a' : Resultado <- Verdadero;
		'e' : Resultado <- Verdadero;
		'i' : Resultado <- Verdadero;
		'o' : Resultado <- Verdadero;
		'u' : Resultado <- Verdadero;
	De Otro Modo:
		Resultado <- Falso;
	FinSegun
FinProcedimiento

Algoritmo ejercicio13
	Definir Letra Como Caracter;
	Definir Resultado Como Logico;

	Escribir "Ingrese una letra: ";
	Leer Letra;
	
	Resultado <- Determinar_Vocal(Letra);
	
	Si (Resultado = Verdadero) Entonces
		Escribir "La letra que ingreso esta entre las vocales.";
	SiNo
		Escribir "La letra que ingreso no esta entre las vocales.";
	FinSi
FinAlgoritmo
```

### Ejercicio 14

1. Escribir un procedimiento que permita calcular la suma 1+2+3+ ... + n.

*Procedimiento*
```
Procedimiento Calcular_Suma(Limite : Entero ; VAR Resultado : Entero)
Definir Indice Como Entero;	
Resultado <- 0;
	Para Indice <- 1 Hasta Limite Hacer
		Resultado  <- Resultado + Indice;
	FinPara
FinProcedimiento

Algoritmo ejercicio14
	Definir Limite, Resultado Como Entero;

	Escribir "Ingrese el limite de la sucecion: ";
	Leer Limite;
	
	Calcular_Suma(Limite, Resultado);

	Escribir "La Sucesion da como resultado: ", Resultado;
FinAlgoritmo
```
*Funcion*
```
Funcion Calcular_Suma(Limite : Entero) : Entero;
Definir Indice Como Entero;	
Resultado <- 0;
	Para Indice <- 1 Hasta Limite Hacer
		Resultado  <- Resultado + Indice;
	FinPara
FinFuncion

Algoritmo ejercicio14
	Definir Limite Como Entero;

	Escribir "Ingrese el limite de la sucecion: ";
	Leer Limite;
	
	Calcular_Suma(Limite);

	Escribir "La Sucesion da como resultado: ", Calcular_Suma(Limite);
FinAlgoritmo
```

### Ejercicio 15

1. Escribir un procedimiento tipo calculadora donde se le da como entrada dos números y el
tipo de operación y esta devuelve el resultado.

```
Procedimiento Calculadora(Numero1, Numero2 : Real ; Operador : Caracter ; VAR Resultado : Real)
	Segun Operador Hacer
		'+' : Resultado <- Numero1 + Numero2;
		'-' : Resultado <- Numero1 - Numero2;
		'*' : Resultado <- Numero1 * Numero2;
		'/' : Resultado <- Numero1 / Numero2;
	De Otro Modo:
		Resultado <- 0;
	FinSegun
FinProcedimiento
	
Algoritmo ejercicio15
	Definir Numero1, Numero2, Resultado Como Real;
	Definir Operador Como Caracter;

	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2;
	Escribir "Ingrese la operacion que desea hacer (+,-,*,/): ";
	Leer Operador;

	Si (Numero2 = 0) y (Operador = '/') Entonces
		Escribir "No se puede dividir por 0";
	SiNo
		Calculadora(Numero1, Numero2, Operador, Resultado);
		Escribir "Resultado: ", Resultado;
	FinSi
FinAlgoritmo
```
*Funcion*
```
Funcion Calculadora(Numero1, Numero2 : Real ; Operador : Caracter) : Real;
	Segun Operador Hacer
		'+' : Resultado <- Numero1 + Numero2;
		'-' : Resultado <- Numero1 - Numero2;
		'*' : Resultado <- Numero1 * Numero2;
		'/' : Resultado <- Numero1 / Numero2;
	De Otro Modo:
		Resultado <- 0;
	FinSegun
FinFuncion
	
Algoritmo ejercicio15
	Definir Numero1, Numero2 Como Real;
	Definir Operador Como Caracter;

	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2;
	Escribir "Ingrese la operacion que desea hacer (+,-,*,/): ";
	Leer Operador;

	Si (Numero2 = 0) y (Operador = '/') Entonces
		Escribir "No se puede dividir por 0";
	SiNo
		Escribir "Resultado: ", Calculadora(Numero1, Numero2, Operador);
	FinSi
FinAlgoritmo
```
*Funcion y Procedimiento*
```
Funcion Sumar(Numero1, Numero2 : Real) : Real;
	Suma <- Numero1 + Numero2;
FinFuncion

Funcion Restar(Numero1, Numero2 : Real) : Real;
	Resta <- Numero1 - Numero2;
FinFuncion

Funcion Multiplicar(Numero1, Numero2 : Real) : Real;
	Resta <- Numero1 * Numero2;
FinFuncion

Funcion Dividir(Numero1, Numero2 : Real) : Real;
	Dividir <- Numero1 div Numero2;
FinFuncion

Procedimiento Calculador(Numero1, Numero2 : Real ; Operador : Caracter ; VAR Resultado : Real)
	Segun (Operador) Hacer
		'+' : Resultado <- Suma(Numero1, Numero2);
		'-' : Resultado <- Resta(Numero1, Numero2);
		'*' : Resultado <- Multiplicar(Numero1, Numero2);
		'/' : Resultado <- Dividir(Numero1, Numero2);
	De Otro Modo: 
		Resultado <- 0;
	FinSegun
FinProcedimiento

Algoritmo ejercicio15
	Definir Numero1, Numero2, Resultado Como Real;
	Definir Operador Como Caracter;

	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2;
	Escribir "Ingrese la operacion que desea hacer (+,-,*,/): ";
	Leer Operador;

	Si (Operador = '/') y (Numero = 0) Entonces
		Escribir "No se puede dividor por 0."; 
	SiNo
		Calculadora(Numero1, Numero2, Operador, Resultado);
		Escribir "Resultado: ",Resultado;
	FinSi
FinAlgoritmo
```
### Ejercicio 16

16. Escribir una función que dados 2 números, calcule el porcentaje que el primero representa
respecto del segundo.

*Procedimiento*
```
Procedimiento Determinar_Porcentaje(Numero1, Numero2 : Entero ; VAR Resultado : Real)
	Resultado <- (Numero1 / Numero2) * 100;
FinProcedimiento

Algoritmo ejercicio16
	Definir Numero1, Numero2 Como Entero;
	Definir Resultado Como Real;

	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2;

	Si (Numero2 = 0) Entonces
		Escribir "El segundo numero no puede ser 0.";
	SiNo
		Determinar_Porcentaje(Numero1, Numero2, Resultado);
		Escribir "El porcentaje que el primer numero (",Numero1,") representa respecto del segundo (", Numero2,") es: ", Respuesta,"%.";
	FinSi
FinAlgoritmo
```
*Funcion*
```
Procedimiento Determinar_Porcentaje(Numero1, Numero2 : Entero) : Real;
	Determinar_Porcentaje <- (Numero1 / Numero2) * 100;
FinProcedimiento

Algoritmo ejercicio16
	Definir Numero1, Numero2 Como Entero;

	Escribir "Ingrese un numero: ";
	Leer Numero1;
	Escribir "Ingrese otro numero: ";
	Leer Numero2;

	Si (Numero2 = 0) Entonces
		Escribir "El segundo numero no puede ser 0.";
	SiNo
		
		Escribir "El porcentaje que el primer numero (",Numero1,") representa respecto del segundo (", Numero2,") es: ", Determinar_Porcentaje(Numero1, Numero2),"%.";
	FinSi
FinAlgoritmo
```