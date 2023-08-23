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


Otro uso basico del metodo `format()`

```python
    print("We are the {} who say '{}!'".format('knights','Ni'))

    # out: We are the knights who say 'Ni!'
``` 

Las llaves y caracteres dentro de las mismas (llamados campos de formato) son reemplazadas con los objetos pasados en el método `str.format()`. Un número en las llaves se refiere a la posición del objeto pasado en el método `str.format()`.

```python
    print("{0} and {1}".format('spam','eggs'))
    # spam and eggs

    print("{1} and {0}.".format('spam','eggs'))
    # eggs and spam
```

Si se usan argumentos nombrados en el método `str.format()`, sus valores se referencian usando el nombre del argumento

```python
    print("This {food} is {adjetive}.".format(food='spam', adjetive='absolutely horrible'))

    # out: This spam is absolutely horrible.
```

Si tiene una cadena de caracteres de formato realmente larga que no desea dividir, sería bueno si pudiera hacer referencia a las variables que se formatearán por nombre en lugar de por posición. Esto se puede hacer simplemente pasando el diccionario y usando corchetes `[]` para acceder a las claves.

```python
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcad': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoer]:d}; Dcab: {0[Dcab]:d}.'.format(table))

    # out: Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Esto se podría hacer, también, pasando el diccionario `table` como argumentos por palabra clave con la notación “**”.

```python
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
```

Esto es particularmente útil en combinación con la función integrada `vars()`, que retorna un diccionario conteniendo todas las variables locales.

Como ejemplo, las siguientes líneas producen un conjunto ordenado de columnas que dan enteros y sus cuadrados y cubos:

```python
    for x in range(1, 11)
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    # out: 
"""  1   1    1
     2   4    8
     3   9   27
     4  16   64
     5  25  125
     6  36  216
     7  49  343
     8  64  512
     9  81  729
    10 100 1000
"""
```


### Modificadores para convertir variables

Se pueden utilizar otros modificadores para convertir el valor antes de formateo. `!a` se aplica `ascii()`, `!s` se aplica `str()`, y `!r` se aplica `repr()`

```python
    animal = 'cat'

    print(f"My house is full of {animal}")
    # out: My house is full of cat

    print(f"My house is full of {animal!r}")
    # out: My house is full of 'cat'
```

El especificador `=` puede utilizarse para expandir una expresión al texto de la expresión, un signo igual y, a continuación, la representacion de la expresión evaluada.

```python
    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f"Debugging {bugs=} {count=} {area=}")
    # Debugging bugs='roaches' count=13 area='living room'
```



### Caracteres de escape 

En Python, los caracteres de escape son secuencias especiales que se utilizan en secuencia de texto para representar caracteres que de otra manera seria dificiles de insertar directamente en el codigo.

1. `\n`: Salto de línea. Insertar una nueva linea de cadena.
2. `\t`: Tabulacion. Insertar un carácter de tabulación en la cadena.
3. `\\`: Barra invertida. Inserta un carácter de barra invertida en la cadena.
4. `\'`: Comilla simple. Inserta una comilla simple en la cadena.
5. `\"`: Comilla doble. Inserta una comilla doble en la cadena.
6. `\r`: Retorno de carro. Se utiliza para realizar un retorno de carro (retorno al inicio de la linea) en algunas plataformas.
7. `\b`: Retroceso. Borra un carácter antes del cursor en la cadena.
8. `\f`: Avance de página. Insertar un caracter de avance de pagina.
9. `\v`: Tabulacion vertical. Inserta un carácter de tabulación vertical.
10. `\xhh` : Representacion hexadecimal. Inserta un caracter correspondiente al valor hexadecimal `hh`.

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


## Modulo `msvcrt`

### `getch()`
El metodo `getch()` del modulo `msvcrt` en Python se utiliza para capturar la entrada del teclado de manera sencilla y sin necesidad de presionar Enter. Este metodo es especialmente útil en aplicaciones donde se requiere una entrada de teclado inmediata y sin buffer.

Ejemplo:

```python
    print("Presiona una tecla: ")
    
    # in: s
    tecla_presionada = msvcrt.getch()
    
    print(f"Presionaste la tecla: {tecla_presionada.decode('utf-8')}")
    # out: s
```

otras variantes del metodo: 

#### `getwch()`

Variante de caracteres anchos de getch(), que devuelve un valor Unicode.

Ej. 

```python
    print("Presiona una tecla: ")

    # in: s
    tecla_presionada = msvcrt.getwch()

    print(f"Presionaste la tecla: {tecla_presioada}")
    # out: s
```


### Otra forma de formatear un `print()` 

