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

# Formas de cargar una Lista

Aquí tienes algunas formas de crear una función o procedimiento en Python para cargar una lista con valores:

1. **Función con Parámetros:**
Puedes crear una función que acepte parámetros para cargar valores en la lista.
    
    ```python
    def cargar_lista(valores):
        lista = []
        for valor in valores:
            lista.append(valor)
        return lista
    
    valores = [1, 2, 3, 4, 5]
    lista_cargada = cargar_lista(valores)
    
    ```
    
2. **Función con Entrada de Usuario:**
Puedes crear una función que solicite al usuario ingresar valores.
    
    ```python
    def cargar_lista_usuario():
        lista = []
        n = int(input("Ingrese la cantidad de valores: "))
        for _ in range(n):
            valor = int(input("Ingrese un valor: "))
            lista.append(valor)
        return lista
    
    lista_cargada = cargar_lista_usuario()
    ```
    
3. **Función con Range:**
Puedes utilizar una función que genere valores utilizando `range()`.
    
    ```python
    def cargar_lista_rango(n):
        lista = list(range(1, n + 1))
        return lista
    
    cantidad = 5
    lista_cargada = cargar_lista_rango(cantidad)
    ```
    
4. **Función con List Comprehension:**
Puedes utilizar una list comprehension para cargar valores en la lista.
    
    ```python
    def cargar_lista_comprehension(n):
        lista = [x for x in range(1, n + 1)]
        return lista
    
    cantidad = 5
    lista_cargada = cargar_lista_comprehension(cantidad)
    ```
    
5. **Función con Valores Fijos:**
Puedes crear una función que cargue valores específicos en la lista.
    
    ```python
    def cargar_lista_fija():
        lista = [1, 2, 3, 4, 5]
        return lista
    
    lista_cargada = cargar_lista_fija()
    ```
    
6. *Función con args:*
Puedes crear una función que acepte una cantidad variable de argumentos.
    
    ```python
    def cargar_lista_args(*args):
        lista = list(args)
        return lista
    
    lista_cargada = cargar_lista_args(1, 2, 3, 4, 5)
    ```
    
7. **Función con Archivo Externo:**
Puedes crear una función que lea valores desde un archivo y los cargue en la lista.
    
    ```python
    def cargar_lista_desde_archivo(nombre_archivo):
        lista = []
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                valor = int(linea.strip())
                lista.append(valor)
        return lista
    
    archivo = "datos.txt"
    lista_cargada = cargar_lista_desde_archivo(archivo)
    ```
    

Estas son algunas formas de crear funciones o procedimientos en Python para cargar valores en una lista. Puedes adaptar estas ideas según tus necesidades específicas y el tipo de valores que deseas cargar en la lista.

# Como funciona el asterisco * con las Listas.

En Python, el asterisco (`*`) se utiliza en varias formas con las listas para realizar operaciones como empaquetar y desempaquetar elementos, expandir secuencias y más. Aquí están algunas de las formas más comunes en las que se utiliza el asterisco con las listas:

1. **Desempaquetar Listas:**
El asterisco se utiliza para desempaquetar elementos de una lista y pasarlos como argumentos individuales a una función.
    
    ```python
    def suma(a, b, c):
        return a + b + c
    
    numeros = [1, 2, 3]
    resultado = suma(*numeros)  # Equivalente a suma(1, 2, 3)
    ```
    
2. **Empaquetar Valores:**
El asterisco también se utiliza para empaquetar varios valores en una lista.
    
    ```python
    valores = *numeros, 4, 5  # Equivalente a [1, 2, 3, 4, 5]
    ```
    
3. **Expandir Secuencias:**
Puedes usar el asterisco para expandir una secuencia en elementos individuales.
    
    ```python
    secuencia = [6, 7]
    nueva_lista = [*numeros, *secuencia]  # Equivalente a [1, 2, 3, 6, 7
    ```
    
4. **Desempaquetar para Asignación:**
Puedes desempaquetar elementos de una lista en variables individuales.
    
    ```python
    a, *resto, b = [1, 2, 3, 4, 5]
    # a = 1, resto = [2, 3, 4], b = 5
    ```
    
5. **Desempaquetar para Iteración:**
Puedes desempaquetar elementos de una lista para iterar sobre ellos.
    
    ```python
    for elemento in [1, 2, 3]:
        print(elemento)
    ```
    
6. **Unir Listas:**
Puedes utilizar el asterisco para unir dos listas en una nueva.
    
    ```python
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista_unida = [*lista1, *lista2]  # [1, 2, 3, 4, 5, 6]
    ```
    
7. **Argumentos Variables en Funciones:**
En la definición de una función, el asterisco se usa para indicar argumentos variables.
    
    ```python
    def mi_funcion(*args):
        for arg in args:
            print(arg)
    
    mi_funcion(1, 2, 3)  # Imprime 1, 2, 3
    ```
    
8. **Desempaquetar para Crear Listas:**
Puedes desempaquetar elementos de una lista para crear una nueva lista.
    
    ```python
    lista_original = [1, 2, 3]
    nueva_lista = [*lista_original, 4, 5]  # [1, 2, 3, 4, 5]
    ```
    

El uso del asterisco con las listas brinda flexibilidad y conveniencia en varios contextos, permitiéndote realizar operaciones como empaquetar y desempaquetar elementos, expandir secuencias y más.

# Otras formas…

Existen varias formas de cargar una lista en Python, dependiendo de tus necesidades y los datos que desees ingresar. Aquí tienes algunas de las formas más comunes de cargar una lista:

1. **Creación Manual:**
Puedes crear una lista manualmente ingresando los elementos uno por uno.
    
    ```python
    lista = [1, 2, 3, 4, 5]
    
    ```
    
2. **Utilizando `range()`:**
Puedes generar una lista de números utilizando la función `range()`.
    
    ```python
    lista = list(range(1, 6))  # [1, 2, 3, 4, 5]
    ```
    
3. **Usando List Comprehensions:**
Las list comprehensions son una forma concisa de crear listas basadas en una expresión.
    
    ```python
    cuadrados = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
    ```
    
4. **Entrada de Usuario:**
Puedes solicitar al usuario que ingrese elementos para cargar en la lista.
    
    ```python
    elementos = input("Ingrese elementos separados por comas: ")
    lista = elementos.split(",")
    ```
    
5. **Lectura desde Archivo:**
Puedes leer datos desde un archivo y cargarlos en una lista.
    
    ```python
    with open("datos.txt") as archivo:
        lineas = archivo.readlines()
    lista = [linea.strip() for linea in lineas]
    ```
    
6. **Mediante Iterables:**
Puedes cargar elementos de otro iterable, como una tupla o un conjunto.
    
    ```python
    tupla = (1, 2, 3, 4, 5)
    lista = list(tupla)
    ```
    
7. **Carga con Método `extend()`:**
Puedes agregar elementos de otro iterable a una lista existente utilizando el método `extend()`.
    
    ```python
    lista_existente = [1, 2, 3]
    nuevos_elementos = [4, 5, 6]
    lista_existente.extend(nuevos_elementos)
    ```
    
8. **Carga con Método `append()`:**
Puedes agregar elementos uno por uno al final de la lista utilizando el método `append()`.
    
    ```python
    lista = []
    lista.append(1)
    lista.append(2)
    ```
    
9. **Utilizando Funciones Generadoras:**
Puedes cargar elementos utilizando funciones generadoras como `map()` o `filter()`.
    
    ```python
    def doble(x):
        return x * 2
    
    numeros = [1, 2, 3, 4, 5]
    lista_dobles = list(map(doble, numeros))
    ```
    

Estas son solo algunas de las formas más comunes de cargar una lista en Python. La elección de la forma adecuada depende de los datos que tengas y de cómo quieras estructurar tu código.

Método `random`

El módulo `random` en Python te permite generar números pseudoaleatorios. Para utilizar este módulo y generar números aleatorios, debes seguir estos pasos:

1. **Importar el módulo random:**
Primero, debes importar el módulo `random` en tu programa. Puedes hacerlo de la siguiente manera:
    
    ```python
    import random
    
    ```
    
2. **Generar Números Aleatorios:**
Una vez que hayas importado el módulo `random`, puedes utilizar sus funciones para generar números aleatorios. Aquí hay algunas de las funciones más comunes que puedes utilizar:
    - **`random()`**: Genera un número decimal aleatorio entre 0 y 1.
    
    ```python
    numero_aleatorio = random.random()
    ```
    
    - **`randint(a, b)`**: Genera un número entero aleatorio entre `a` y `b` (inclusive).
    
    ```python
    numero_entero_aleatorio = random.randint(1, 10)
    ```
    
    - **`choice(lista)`**: Devuelve un elemento aleatorio de la lista.
    
    ```python
    opciones = ["manzana", "banana", "naranja"]
    eleccion_aleatoria = random.choice(opciones)
    ```
    
    - **`shuffle(lista)`**: Mezcla los elementos de la lista de forma aleatoria.
    
    ```python
    cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(cartas)
    ```
    
3. **Control de Semilla Aleatoria (Opcional):**
Si deseas reproducir los mismos números aleatorios en diferentes ejecuciones, puedes establecer una "semilla" aleatoria utilizando la función `seed()`.
    
    ```python
    random.seed(42)  # Establecer una semilla aleatoria
    numero_aleatorio = random.random()
    ```
    

Recuerda que los números generados por `random` son pseudoaleatorios, lo que significa que son deterministas y se basan en un valor inicial llamado semilla. Si no estableces la semilla manualmente, Python utiliza el reloj del sistema como semilla de manera predeterminada.