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

**version 1**
```
Algoritmo
    Definir Alumnos_Promocionados, Alumnos_Regularizados, Alumnos_Desaprobados, Alumnos_Libros, Total Como Entero;
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

**version 2**

| VARIABLE | DESCRIPCION |
| -------- | ----------- |
| A_P | Alumnos Promocionados |
| A_R | Alumnos Regularizados |
| A_D | Alumnos Desaprobados |
| A_L | Alumnos Libres |

