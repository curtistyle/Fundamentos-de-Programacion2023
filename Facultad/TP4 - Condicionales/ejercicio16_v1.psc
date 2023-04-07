Algoritmo ejercicio16
    Definir Mes Como Entero;
	
	Escribir "Ingrese el Mes: ";
    Leer Mes;
	
    Si (Mes = 1) o (Mes = 3) o (Mes = 5) o (Mes = 7) o (Mes = 8) o (Mes = 10) o (Mes = 12) Entonces
        Escribir "El Mes ", Mes ,"tiene 31 Dias.";
    SiNo
        Si (Mes = 2) Entonces
            Escribir "El Mes ", Mes ,"tiene 28 Dias.";
        SiNo
            Escribir "El Mes ", Mes ,"tiene 30 Dias.";
        FinSi
    FinSi
FinAlgoritmo