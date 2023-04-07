Algoritmo ejercicio16
    Definir Mes Como Entero;
	
	Escribir "Ingrese el Mes: ";
    Leer Mes;
	
    Si (Mes = 4) o (Mes = 6) o (Mes = 9) o (Mes = 11) Entonces
        Escribir "Es Mes: ", Mes ," tiene 30 dias.";
    SiNo
        Si (Mes = 2) Entonces
            Escribir "Es Mes: ", Mes ," tiene 28 dias.";
        SiNo
            Escribir "Es Mes: ", Mes ," tiene 31 dias.";
        FinSi
    FinSi
FinAlgoritmo