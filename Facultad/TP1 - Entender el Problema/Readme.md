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
    Definir Total_Estudiantes, Estudiantes_Menores, Porcentaje Como Real

    Leer Total_Estudiantes, Estudiantes_Menores

    Porcentaje <- (Estudiantes_Menores * 100) Total_Estudiantes

    Escribir Porcentaje
FinAlgoritmo
```


