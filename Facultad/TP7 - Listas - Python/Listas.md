# Listas

Mas información sobre listas: [https://docs.python.org/es/3/tutorial/datastructures.html](https://docs.python.org/es/3/tutorial/datastructures.html) , [https://docs.python.org/es/3/library/stdtypes.html?highlight=list#list](https://docs.python.org/es/3/library/stdtypes.html?highlight=list#list)

# Métodos

Aquí tienes algunos de los métodos más comunes para manipular listas en Python. Estos métodos te permiten realizar diversas operaciones en las listas, como agregar, eliminar, ordenar y modificar elementos. Recuerda que esta no es una lista exhaustiva, pero abarca muchas de las operaciones básicas y útiles que puedes realizar con listas:

1. **`append(elemento)`**: Agrega un elemento al final de la lista.
2. **`extend(iterable)`**: Agrega los elementos de un iterable (lista, tupla, etc.) al final de la lista.
3. **`insert(indice, elemento)`**: Inserta un elemento en una posición específica.
4. **`remove(elemento)`**: Elimina la primera aparición del elemento de la lista.
5. **`pop([indice])`**: Elimina y devuelve el elemento en el índice especificado (o el último si no se especifica índice).
6. **`index(elemento, [inicio], [fin])`**: Devuelve el índice de la primera aparición del elemento (opcionalmente dentro del rango especificado).
7. **`count(elemento)`**: Cuenta cuántas veces aparece un elemento en la lista.
8. **`sort([key], [reverse])`**: Ordena la lista (opcionalmente utilizando una función clave y en orden inverso).
9. **`reverse()`**: Invierte el orden de los elementos en la lista.
10. **`copy()`**: Crea una copia superficial de la lista.
11. **`clear()`**: Elimina todos los elementos de la lista.
12. **`len(lista)`**: Devuelve la cantidad de elementos en la lista.
13. **`max(lista)`**: Devuelve el elemento más grande en la lista.
14. **`min(lista)`**: Devuelve el elemento más pequeño en la lista.
15. **`sum(lista)`**: Devuelve la suma de todos los elementos en la lista (si son números).
16. **`join(iterable)`**: Une los elementos de un iterable (lista, tupla, etc.) en una cadena usando la lista como separador.
17. **`index(elemento)`**: Devuelve el índice de la primera aparición del elemento en la lista.
18. **`copy()`**: Crea una copia superficial de la lista.
19. **`clear()`**: Elimina todos los elementos de la lista.
20. **`count(elemento)`**: Cuenta cuántas veces aparece un elemento en la lista.
21. **`copy()`**: Crea una copia superficial de la lista.
22. **`clear()`**: Elimina todos los elementos de la lista.

Estos son solo algunos de los métodos que puedes usar para manipular listas en Python. Hay otros métodos más avanzados y específicos que puedes explorar según tus necesidades. Puedes obtener más información sobre estos métodos y otros en la documentación oficial de Python: [Métodos de lista en Python](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

# Los métodos `list()` y `map()`

El método `list()` y la función `map()` son herramientas útiles en Python para trabajar con listas y transformar elementos en una colección. A continuación, te explico cómo funcionan cada uno:

1. **`list(iterable)`**:
El método `list()` se utiliza para crear una nueva lista a partir de un iterable, como una cadena, una tupla o un conjunto. Toma el iterable como argumento y devuelve una lista que contiene todos los elementos del iterable en el mismo orden.
    
    ```python
    tupla = (1, 2, 3)
    lista = list(tupla)  # [1, 2, 3]
    ```
    
    También se puede utilizar para crear una lista a partir de una cadena, donde cada carácter se convierte en un elemento individual de la lista.
    
    ```python
    cadena = "Hola"
    lista_caracteres = list(cadena)  # ['H', 'o', 'l', 'a']
    ```
    
2. **`map(función, iterable)`**:
La función `map()` se utiliza para aplicar una función a cada elemento de un iterable y devuelve un objeto map que se puede convertir en una lista u otra estructura de datos. La función se aplica a cada elemento en el iterable y se aplica de forma "mapeada".
    
    ```python
    def cuadrado(x):
        return x * x
    
    numeros = [1, 2, 3, 4, 5]
    cuadrados = map(cuadrado, numeros)
    lista_cuadrados = list(cuadrados)  # [1, 4, 9, 16, 25]
    ```
    
    También puedes usar una función lambda con `map()`:
    
    ```python
    numeros = [1, 2, 3, 4, 5]
    cuadrados = map(lambda x: x * x, numeros)
    lista_cuadrados = list(cuadrados)  # [1, 4, 9, 16, 25]
    ```
    
    Además, `map()` puede aceptar múltiples iterables y aplicar una función que acepte múltiples argumentos:
    
    ```python
    lista1 = [1, 2, 3]
    lista2 = [10, 20, 30]
    resultado = map(lambda x, y: x + y, lista1, lista2)
    lista_resultado = list(resultado)  # [11, 22, 33]
    ```
    

En resumen, `list()` se utiliza para convertir un iterable en una lista, mientras que `map()` se utiliza para aplicar una función a cada elemento de un iterable y obtener un objeto map que luego se puede convertir en otros tipos de datos, como una lista.

# Slice

La rebanada (**slice**) de secuencia es una característica poderosa en Python que te permite extraer una porción de una secuencia, como una lista, una cadena o una tupla. Aquí están algunas de las formas en que puedes usar la rebanada de secuencia (**sequence slicing**) con listas en Python:

1. **Rebanada Básica:**
Puedes obtener una porción de una lista especificando el índice de inicio y el índice de parada (sin incluirlo) separados por `:`.
    
    ```python
    lista = [1, 2, 3, 4, 5]
    sublista = lista[1:4]  # [2, 3, 4]
    ```
    
2. **Rebanada sin Índice de Inicio o Parada:**
Si omites el índice de inicio, se tomará desde el principio. Si omites el índice de parada, se tomará hasta el final.
    
    ```python
    sublista_inicio = lista[:3]  # [1, 2, 3]
    sublista_fin = lista[2:]     # [3, 4, 5]
    ```
    
3. **Rebanada con Incremento (Step):**
Puedes usar un tercer valor (incremento) para tomar elementos con un cierto intervalo.
    
    ```python
    sublista_incremento = lista[0:5:2]  # [1, 3, 5]
    ```
    
4. **Rebanada en Orden Inverso:**
Puedes usar incremento negativo para obtener elementos en orden inverso.
    
    ```python
    sublista_inversa = lista[::-1]  # [5, 4, 3, 2, 1]
    ```
    
5. **Asignación de Rebanada:**
Puedes utilizar una rebanada para asignar valores a una porción de la lista.
    
    ```python
    lista[1:4] = [6, 7, 8]  # [1, 6, 7, 8, 5]
    ```
    
6. **Rebanada con Variables:**
Puedes usar variables para definir los índices de inicio, parada e incremento.
    
    ```python
    inicio = 1
    parada = 4
    incremento = 1
    sublista_variables = lista[inicio:parada:incremento]  # [2, 3, 4]
    ```
    
7. **Rebanada con Rango de Índices:**
Puedes utilizar la función `range()` para generar un rango de índices.
    
    ```python
    sublista_rango = lista[range(1, 4)]  # [2, 3, 4]
    ```
    
8. **Rebanada con Índices Negativos:**
Los índices negativos cuentan desde el final de la lista.
    
    ```python
    sublista_negativos = lista[-3:-1]  # [3, 4]
    ```
    
9. **Rebanada con Índice Fuera de Límites:**
Los índices fuera de los límites no generan un error, simplemente se truncarán.
    
    ```python
    sublista_fuera_de_limites = lista[10:20]  # []
    ```
    

Recuerda que en Python, el índice de inicio es inclusivo y el índice de parada es exclusivo. Experimenta con estas formas de rebanada de secuencia para comprender mejor cómo funcionan.