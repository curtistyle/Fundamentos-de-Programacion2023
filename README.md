# Python

## output

### **Imprimir con formato** *float*, *decimales*

En python un especificador de formato para imprimir un número con una cantida especificada de decimales se representa con la siguiente sintaxis:

```python
{:.nf}
```

Donde 'n' es el numero de decimales que desea mostrar.

Ejemplo: 

```python
# Utilizando cadenas de formato
numero = 123.456789
print("{:.2f}".format(numero)) # imprimirá el numero con dos decimales: 123.45

# Utilizando f-strings
print(f"{numero:.2f}") # tambien imprimirá el numero con dos decimales 123.45
```

Si deseas mostrar un número con un número de variable de decimales, puedes utilizar una variable para especificar la cantidad de decimales:

```python
numero = 123.456789
decimales = 4

print("{:.{}f}".format(numero,decimales)) # imprimira el numero con cuatro decimales 123.4567

# Utilizando f-strings
print(f"{numero:.{decumales}f}") # tambien imprimira el numero con cuatro decimales
```

Al usar `{:.{}f}`, el primer corchete representa el numero a formatear y el segundo corchete con `{}` representa la variable que contiene la cantidad de decimales que desea mostrar.

## Math

### `math.floor()`

El metodo `math.floor()` se utiliza para redondear un numero hacia abajo al entero mas cercano o igual al numero original. 

Su sintaxis es: 
```python
    import math 

    resultado = math.floor(numero)
```

Donde `numero` es el valor numerico al cual deseas aplicar el redondeo hacia abajo.

ejemplo: 

```python
    import math

    numero = 7.6
    resultado = math.floor(numero)

    print(resultado) # out: 8
```

## Errores

### `int too large convert to float`

El error *int too large to convert to float* en Python ocurre cuando intentas convertir un entero demasiado grande en un valor de punto flotante (`float`), y el entero excede la cantidad de formato `float` para representar números enteros con precisión completa.
El formato `float` tiene una capacidad finita para representar números grandes y pequeños con precisión limitada.

Si estas trabajando con números enteros muy grandes y necesitas mantener la presicisión, puedes considerar mantener la presicion utilizando el metodo `Decimal()` del modulo `decimal` que proporciona representación decimal de alta precision. Ejemplo:

```python
    from decimal  import Decimal

    entero_grande = 1234567890123456789012345678901234567890
    decimal_entero = Decimal(entero_grande)
    print(decimal_grande) # Output: 1234567890123456789012345678901234567890
```

Si no necesitas una alta precisión y solo deseas imprimir o mostrar el número grande, puedes utilizar el formato de cadena sin convertirlo a `float`:

```python
    entero_grande = 123456789012345678901234567890
    print(str(entero_grande)) # Output: 123456789012345678901234567890
```

En este caso, simplemente convertimos el número grande a una cadena y lo imprimimos directamente. Esto evitará el problema de convertir el entero grande en un `float`.