# TP3 - Secuencia

## Ejercicio 1

1. Leer tres números de a una por vez, calcular su suma y su producto

```
Algoritmo
    Definir Numero1, Numero2, Numero3, Suma, Producto Como Real;

    Leer Numero1, Numero2, Numero3;

    Suma <- Numero1 + Numero2 + Numero3;
    Producto <- Numero1 * Numero2 * Numero3;

    Escribir Suma, Producto;
FinAlgoritmo
```

## Ejercicio 2

2. Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa.

```
Algoritmo
    Definir Cateto1, Cateto2, Hipotenusa Como Real;

    Leer Cateto1, Cateto2;

    Hipotenusa <- sqrt((Cateto1^2)+(Cateto2^2));

    Escribir Hipotenusa;
FinAlgoritmo
```

## Ejercicio 3

3. Dadas  las  horas  trabajadas  por  un  operario  y  el  valor  de  las  mismas,  determinar  que sueldo percibe dicho operario. Se solicita indicar cuanto cobraría si se aplican descuentos del 20%.

```
Algoritmo
    Definir Horas_Trabajadas, Horas_Valor, Sueldo, Descuento Como Real;

    Leer Horas_Trabajadas, Horas_Valor;

    Descuento <- Horas_Trabajadas * Horas_Valor * 0.2;
    Sueldo <- (Horas_Trabajadas * Horas_Valor) - Descuento;

    Escribir Descuento, Sueldo;
FinAlgoritmo
```

## Ejercicio 4

4. Hallar  el  área  de  un  cuadrado,  cuyos  lados  tienen  la  longitud  de  la  hipotenusa  de  un triángulo rectángulo y cuyos catetos son dados.

```
Algoritmo 
    Definir Cateto1, Cateto2, Area, Hipotenusa Como Real;

    Leer Cateto1, Cateto2;

    Hipotenusa <- sqrt((Cateto1^2) + (Cateto2^2));
    Area <- Hipotenusa^2;

    Escribir Area;
FinAlgoritmo
```

## Ejercicio 5

5. Dadas las calificaciones de 4 exámenes finales de un estudiante determinar el promedio

```
Algoritmo
    Definir Nota1, Nota2, Nota3, Nota4, Promedio Como Real;

    Leer Nota1, Nota2, Nota3, Nota4;

    Promedio <- (Nota1 + Nota2 + Nota3 + Nota4) / 4;

    Escribir Promedio;
FinAlgoritmo
```

## Ejercicio 6

6. Diseñe un algoritmo que determine el porcentaje de: Alumnos promocionados, Alumnos regularizados, Alumnos desaprobados y Alumnos libres, teniendo como datos cantidad de alumnos que cumplen con cada condición.

**version 1** _(sobrescribiendo variables)_
```
Algoritmo
    Definir Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libres, Total Como Entero;
    Definir Porcentaje Como Real;

    Leer Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libres;

    Total <- Alumnos_Promocionados + Alumnos_Regularizados + Alumnos_Desaprobados + Alumnos_Libres;

    Porcentaje <- (Alumnos_Promocionados * 100) / Total;
    Escribir Porcentaje;

    Porcentaje <- (Alumnos_Regularizados * 100) / Total;
    Escribir Porcentaje;

    Porcentaje <- (Alumnos_Desaprobados * 100) / Total;
    Escribir Porcentaje;

    Porcentaje <- (Alumnos_Libres * 100) / Total;
    Escribir Porcentaje;
FinAlgoritmo
```

**version 2** _(sobrescribiendo variables)_
```
Algoritmo
    Definir Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libres, Porcentaje, Total Como Real;

    Leer Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libres;

    Total <- Alumnos_Promocionados + Alumnos_Regularizados + Alumnos_Desaprobados + Alumnos_Libres;

    Alumnos_Promocionados <- (Alumnos_Promocionados * 100) / Total;
    Alumnos_Regularizados <- (Alumnos_Regularizados * 100) / Total;
    Alumnos_Desaprobados <- (Alumnos_Desaprobados * 100) / Total;
    Alumnos_Libres <- (Alumnos_Libres * 100) / Total;

    Escribir Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libres;
FinAlgoritmo
```


**version 3**

| VARIABLE | DESCRIPCION |
| -------- | ----------- |
| A_P | Alumnos Promocionados |
| A_R | Alumnos Regularizados |
| A_D | Alumnos Desaprobados  |
| A_L |     Alumnos Libres    |
|     |                       |
| P_P | Porcentaje Alumnos Promocionados |
| P_R | Porcentaje Alumnos Regularizados |
| P_D |  Porcentaje Alumnos Desaprobados |
| P_L |     Porcentaje Alumnos Libres    |

```
Algoritmo
    Definir A_P, A_R, A_D, A_L, Total Como Entero;
    Definir P_P, P_R, P_D, P_L Como Real;

    Leer A_P, A_R, A_D, A_L;

    Total <- A_P + A_R + A_D + A_L;
    P_P <- (A_P * 100) / Total;
    P_R <- (A_R * 100) / Total;
    P_D <- (A_D * 100) / Total;
    P_L <- (A_L * 100) / Total;

    Ecribir P_P, P_R, P_D, P_L;
FinAlgoritmo
```

## Ejercicio 7

7. Dados  dos  números  a  y  b,  se  desea  intercambiar  sus  valores,  utilizando  una  variable auxiliar.

```
Algoritmo
    Definir A, B, Aux Como Real;

    Leer A, B;

    Aux <- B;
    B <- A;
    A <- Aux;

    Escribir A, B;
FinAlgoritmo
```

## Ejercicio 8

8. Escriba un programa que permita el ingreso de un número de tres dígitos y determine si es un número Armstrong (ej. 153, 371). Como el número que se ingresa posee 3 dígitos, la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número.

```
Algoritmo
    Definir Numero, Digito1, Digito2, Digito3, Suma Como Entero;
    
    Leer Numero;

    Digito1 <- Numero div 100;
    Digito2 <- (Numero - (Digito1 * 100)) div 10;
    Digito3 <- (Numero - (Digito1 * 100) + Digito2 * 10);

    Suma <- (Digito1^3)+(Digito2^3)(Digito3^3);

    Escribir Suma;
FinAlgoritmo
```

## Ejercicio 9

9. Escribir un programa que lea dos números enteros A y B, y obtenga los valores A div B, A mod B.


**version 1**
```
Algoritmo
    Definir A, B, Resultado Como Entero;

    Leer A, B;

    Resultado <- A div B;
    Escribir Resutaldo;

    Resultado <- A mod B;
    Escribir Resultado;
FinAlgoritmo
```

**version 2**
```
Algoritmo 
    Definir A, B, Modulo, Division_Entera Como Entero;

    Leer A, B;

    Modulo <- A mod B;
    Division_Entera <- A div B;

    Escribir Modulo, Division_Entera;
FinAlgoritmo
```

## Ejercicio 10

10. Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una circunferencia  y  calcule  y  muestre  por  pantalla  el  área  y  perímetro.  área  =  PI  *  radio2 || perímetro = 2 * PI * radio.

```
Algoritmo
    Definir Radio, Area, Perimetro Como Real;

    Leer Radio;

    Area <- PI * (Radio^2);
    Perimetro <- 2 * PI * Radio;

    Escribir Area, Perimetro;
FinAlgoritmo
```

## Ejercicio 11

11. Solicitar al usuario que ingrese el precio de un producto al inicio del año, y el precio del mismo producto transcurrido un determinado tiempo. El usuario debe mostrar cuál fue el porcentaje de aumento que tuvo ese producto en el año.

```
Algoritmo
    Definir Valor_Inicial, Valor_Final, Porcentaje Como Real;

    Leer Valor_Inicial, Valor_Final;

    Porcentaje <- ((Valor_Final - Valor_Inicial) / Valor_Inicial) * 100;

    Escribir Porcentaje;
FinAlgoritmo
```

## Ejercicio 12

12. De los y las estudiantes de Fundamentos de Programación se desea saber qué porcentaje  de personas  menores a  20  años  se  encuentran  cursando  la  materia.  El  programa  debe solicitar  al  usuario  que  ingrese  la cantidad  total  de  estudiantes  menores  a 20  años  y  el total.

```
Algoritmo
    Definir Total, Menores Como Entero;
    Definir Porcentaje Como Real;

    Leer Total, Menores;

    Porcentaje <- (Menores * 100) / Total;

    Escribir Porcentaje;
FinAlgoritmo
```

## Ejercicio 13

13. Un millonario excéntrico tenía tres hijos: Carlos,  José y Marta. Al morir dejó el siguiente legado: A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. A Marta le dejo la mitad de lo que le dejó a José. Preparar un algoritmo para darle la suma a repartir e imprima cuanto le tocó a cada uno.

**version 1**
```
Algoritmo 
    Definir Carlos, Jose, Marta, Legado Como Real;

    Carlos <- 1/3;
    Jose <- 4/3;
    Martina <- 1/2;

    Leer Legado;

    Carlos <- Legado * Carlos;
    Jose <- Carlos * Jose;
    Martina <- Jose * Martina;

    Escribir Carlos, Jose, Martina
FinAlgoritmo    
```

**version 2**
```
Algoritmo 
    Definir Carlos, Jose, Marta, Legado Como Real;

    Leer Legado;

    Carlos <- Legado * 1/3;
    Jose <- Carlos * 4/3;
    Martina <- Jose * 1/2;

    Escribir Carlos, Jose, Martina
FinAlgoritmo    
```