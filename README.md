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