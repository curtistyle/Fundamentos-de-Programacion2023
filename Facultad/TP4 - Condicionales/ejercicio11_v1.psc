Algoritmo ejercicio11
    Definir Numero1, Numero2, Producto, Suma Como Entero;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Si (Numero1 < Numero2) Entonces
        Suma <- Numero1 + Numero2;
        Escribir "Como el primero es menor que el segundo, la suma de ambos es: ", Suma;
    SiNo
        Producto <- Numero1 * Numero2;
        Escribir "Como el primero es mayor que el segundo, el producto de ambos es: ", Producto;
    FinSi
FinAlgoritmo