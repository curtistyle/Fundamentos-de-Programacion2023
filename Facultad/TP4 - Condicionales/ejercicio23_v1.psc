Algoritmo ejercicio23
	Definir Total, Correctas Como Entero; 
	Definir Porcentaje Como Real;
	
	Escribir "Ingrese la cantidad total de proguntas: ";
    Leer Total;
	Escribir "Ingrese la cantidad de preguntas correctas: ";
	Leer Correctas;
	
    Porcentaje <- (Correctas * 100) / Total;
	
    Si (Porcentaje < 50) Entonces
        Escribir "Malo";
    SiNo
        Si (Porcentaje >= 50) y (Porcentaje < 70) Entonces
            Escribir "Regular";
        SiNo
            Si (Porcentaje >= 70) y (Porcentaje < 90) Entonces
                Escribir "Bueno";
            SiNo
                Escribir "Muy Bueno";
            FinSi
        FinSi
    FinSi
FinAlgoritmo