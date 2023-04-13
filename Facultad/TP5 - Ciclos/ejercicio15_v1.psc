Algoritmo ejercicio15
    Definir NumeroA, NumeroB, IndiceA, IndiceB, Producto Como Entero
	
    Escribir "Ingrese el rango para desarrollar la tabla.";
    Escribir "A: ";
    Leer NumeroA;
    Escribir "B: ";
    Leer NumeroB;
	
    Si (NumeroA < NumeroB) Entonces
        Para IndiceA <- NumeroA Hasta NumeroB Hacer
			Escribir ">Tabla de multiplicar del ", IndiceA ,".<"
            Para IndiceB <- 1 Hasta 10 Hacer
                Producto <- IndiceA * IndiceB;
                Escribir IndiceA ," por ", IndiceB ," es igual a ", Producto;
            FinPara
        FinPara
    FinSi
FinAlgoritmo