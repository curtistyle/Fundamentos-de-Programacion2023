# TP1 - Entender el problema

## Ejercicio 1

 1. Dado el número matematico PI, se solicita al usuario que ingrese el valor del radio de una circunferencia y calcule y muestre por pantalla el área y el perimetro. (área = PI * radio^2 ; perimetro = 2 * PI * radio)

 - **Entrada:**
 > Radio : Real
 - **Proceso:**
 > Area = PI * (Radio^2) \
 > Perimetro = 2 * PI * Radio
 - **Salida:**
 > Area, Perimetro : Real

#### Pseudocodigo
```
Algoritmo
    Definir Radio, Area, Perimetro Como Real;

    Leer Radio;

    Area <- PI * (Radio^2);
    Perimetro <- 2 * PI * Radio;

    Escribir Area, Perimetro;
FinAlgoritmo
```



## Ejercicio 13

13. De los y las estudiantes de Fundamentos de Programacion se desea saber que porcentaje menores a 20 años se encuentran cursando la materia. El programa debe solicitar al usuario que ingrese la cantidad total de estudiantes menores a 20 años y el total.

 - **Entrada:**
 > Total_Estudiantes, Estudiantes_Menores : Real
 - **Proceso:**
 > Porcentaje = (Estudiantes_Menores * 100) - Total_Estudiantes
 - **Salida:**
 > Porcentaje : Real

#### Pseudocodigo
```
Algoritmo
    Definir Total_Estudiantes, Estudiantes_Menores, Porcentaje Como Real;

    Leer Total_Estudiantes, Estudiantes_Menores;

    Porcentaje <- (Estudiantes_Menores * 100) / Total_Estudiantes;

    Escribir Porcentaje;
FinAlgoritmo
```

## Ejercicio 2

2. Dadas las longitudes de dos catetos de un triangulo rectangulo, hallar la longitud de la hipotenusa.

 - **Entrada:**
 > Cateto1, Cateto2 : Real
 - **Proceso:**
 > Hipotenusa = Raiz_Cuadrada( (Cateto1^2) + (Cateto^2) )
 - **Salida:**
 > Hipotenusa : Real

#### Pseudocodigo
```
Algoritmo
    Definir Cateto1, Cateto2, Hipotenusa Como Real;

    Leer Cateto1, Cateto2;

    Hipotenusa <- sqrt((Cateto1^2)+(Cateto^2));

    Escribir Hipotenusa;
FinAlgoritmo
```

## Ejercicio 3

3. Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que sueldo percibe dicho operario.

 - **Entrada:**
 > Horas_Trabajadas, Horas_Valor : Real
 - **Proceso:**
 > Sueldo = Horas_Trabajadas * Horas_Valor
 - **Salida:**
 > Sueldo : Real

#### Pseudocodigo
```
Algoritmo
    Definir Horas_Trabajadas, Horas_Valor, Sueldo Como Real;

    Leer Horas_Trabajadas, Horas_Valor;

    Sueldo <- Horas_Trabajadas * Horas_Valor;

    Escribir Sueldo;
FinAlgoritmo
```

## Ejercicio 4

4. Ídem anterior, pero considerando que se le debe aplicar los descuentos correspondientes por ley, los mismos son del 20%. Mostrar el sueldo a cobrar.

 - **Entrada:**
 > Horas_Trabajadas, Horas_Valor : Real
 - **Proceso:**
 > Descuento = Horas_Trabajadas * Horas_Valor * 0.2 \
 > Sueldo = (Horas_Trabajadas * Horas_Valor) - Descuento
 - **Salida:**
 > Sueldo : Real

#### Pseudocodigo
```
Algoritmo
    Definir Horas_Trabajadas, Horas_Valor, Sueldo, Descuento Como Real;

    Leer Horas_Trabajadas, Horas_Valor;

    Descuento <- Horas_Trabajadas * Horas_Valor * 0.2;
    Sueldo <- (Horas_Trabajadas * Horas_Valor) - Descuento;

    Escribir Sueldo;
FinAlgoritmo
```

## Ejercicio 5

5. Dados dos valores A y B distintos, determinar cuál es el mayor.

 - **Entrada:**
 > A, B : Real
 - **Proceso:**
 > Resultado = ¿A es mayor que B?
 - **Salida:**
 > Resultado : Booleano

#### Pseudocodigo
```
Algoritmo
    Definir A, B Como Real;
    Definir Resultado Como Booleano;

    Leer A, B;

    Si (A > B) Entonces
        Resultado <- Verdadero;
    SiNo
        Resultado <- Falso;
    FinSi
    
    Escribir Resultado;
FinAlgoritmo
```

## Ejercicio 6

6. Determinar si una palabra cualquiera es un palindromo (capicua); por ejemplo: Neuquen.

 - **Entrada:**
 > Palabra, Palabra_Invertida : Cadena
 - **Proceso:**
 > Resultado = ¿Palabra es igual a Palabra_Invertida?
 - **Salida:**
 > Resultado : Booleano

#### Pseudocodigo
```
Algoritmo
    Definir Palabra, Palabra_Invertida Como Cadena;
    Definir Resultado Como Booleano;

    Leer Palabra;

    Palabra_Invertida <- Invertir_Cadena(Palabra); 
    
    Si (Palabra = Palabra_Invertida) Entonces
        Resultado <- Verdadero;
    SiNo
        Resultado <- Falso;
    FinSi
    
    Escribir Resultado;
FinAlgoritmo
```

## Ejercicio 7

7. Dadas las calificaciones de 3 exámenes finales de un estudiante determinar el promedio.

 - **Entrada:**
 > Nota1, Nota2, Nota3 : Real
 - **Proceso:**
 > Promedio = (Nota1 + Nota2 + Nota3) / 3
 - **Salida:**
 > Promedio : Real

#### Pseudocodigo
```
Algoritmo
    Definir Nota1, Nota2, Nota3, Promedio Como Real;

    Leer Nota1, Nota2, Nota3;

    Promedio <- (Nota1 + Nota2 + Nota3) / 3;

    Escribir Promedio;
FinAlgoritmo
```

## Ejercicio 8

8. Dada una lista de 3 números determinar si el Nº 3 se encuentra en dicha lista.

 - **Entrada:**
 > 
 - **Proceso:**
 > Resultado = ¿El numero 3 esta en la Lista?
 - **Salida:**
 > Resultado : Booleano

#### Pseudocodigo
```
Algoritmo
    Definir Numero, Indice, Lista Como Entero;
    Definir Resultado Como Booleano;
    Dimension Lista[3];

    Numero <- 3
    Mientras (Indice <= 2) y (Resultado = Falso) Hacer
        Si (Numero = Lista[Indice]) Entonces
            Resultado <- Verdadero;
        SiNo 
            Resultado <- Falso;
        FinSi
        Indice <- Indice + 1;
    FinMientras

    Escribir Resultado;
FinAlgoritmo
```

## Ejercicio 9

9. Calcular el valor a cancelar de un producto de un monto ingresado, el programa debe mostrar cómo se presenta en una factura, subtotal
(cantidad por precio), IVA (del subtotal) y total a pagar (la suma
del subtotal + el IVA). IVA=21%.

 - **Entrada:**
 > Monto : Real ; Cantidad : Entero
 - **Proceso:**
 > Subtotal = Cantidad * Monto \
 > IVA = Subtotal * 0.21 \
 > Total = Subtotal + IVA 
 - **Salida:**
 > Subtotal, IVA, Total : Real

 #### Pseudocodigo
```
Algoritmo
    Definir Monto, Subtotal, IVA, Total Como Real;
    Definir Cantidad Como Entero;

    Leer Monto, Cantidad;

    Subtotal <- Cantidad * Monto;
    IVA <- Subtotal * 0.21;
    Total <- Subtotal + IVA;
    
    Escribir Subtotal, IVA, Total;
FinAlgoritmo
```

## Ejercicio 10

10. Escribir un programa que calcule el volumen de un cilindro. Para ello se deberá solicitar al usuario que ingrese el radio y la altura. Mostrar el resultado por pantalla. volumen = π * radio^2 * altura.

 - **Entrada:**
 > Radio, Altura : Real
 - **Proceso:**
 > Volumen = PI * (Radio^2) * Altura
 - **Salida:**
 > Volumen : Real

 #### Pseudocodigo
```
Algoritmo
    Definir Radio, Altura, Volumen Como Real;

    Leer Radio, Altura;

    Volumen <- PI * (Radio^2) * Altura;

    Escribir Volumen;
FinAlgoritmo
```

## Ejercicio 11

11. Escriba un programa que permita el ingreso de un número de tres dígitos y determine si es un número Armstrong (ej. 153, 371). Como el número que se ingresa posee 3 dígitos, la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número.

 - **Entrada:**
 > Numero : Real
 - **Proceso:**
 > _(El 'div' divide y nos devuelve la parte entera del resultado)_ \
 > Digito1 = Numero div 100  \
 > Digito2 = (Numero - (Digito1 * 100)) div 10  \
 > Digito3 = (Numero - ((Digito1 * 100) + (Digito2 * 10)))  \
 > Suma = (Digito^3) + (Digito^3) + (Digito^3) \
 > Resultado = ¿Suma es igual a Numero?
 - **Salida:**
 > Resultado : Booleano

 #### Pseudocodigo
```
Algoritmo
    Definir Numero, Digito1, Digito2, Digito3 Como Entero;
    Definir Resultado Como Booleano;

    Leer Numero;

    Digito1 <- Numero div 100;
    Digito2 <- (Numero - (Digito1 * 100)) div 10;
    Digito3 <- (Numero - ((Digito1 * 100) + (Digito2 * 10)));

    Suma <- (Digito1^3) + (Digito^3) + (Digito3^3);

    Si (Suma = Numero) Entonces
        Resultado <- Verdadero;
    FinSi
        Resultado <- Falso;

    Escribir Resultado;
FinAlgoritmo
```
