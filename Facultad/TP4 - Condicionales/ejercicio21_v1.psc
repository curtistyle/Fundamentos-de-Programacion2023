Algoritmo ejercicio21
    Definir Kilometros, Tarifa, Auxiliar_Kilometros Como Real;
	
	Escribir "Ingrese la cantidad de kilometros recorridos: ";
    Leer Kilometros;
	
    Si (Kilometros <= 30) Entonces
        Tarifa <- Kilometro * 20;
        Escribir "Kilometros Recorridos: ", Kilometros ,"Km, el monto a pagar es: ", Tarifa ," euros.";
    SiNo
        Si (Kilometros > 30) y (Kilometros <= 100) Entonces
            Auxiliar_Kilometros <- Kilometros - 30;
            Tarifa <- (30 * 20) + Auxiliar_Kilometros;
            Escribir "Kilometros Recorridos: ", Kilometros ,"Km, el monto a pagar es: ", Tarifa ," euros.";
        SiNo
            Si (Kilometros > 100) Entonces
                Auxiliar_Kilometros <- Kilometros - 100;
                Tarifa <- (30 * 20) + 70 + (Auxiliar_Kilometros * 0.50);
                Escribir "Kilometros Recorridos: ", Kilometros ,"Km, el monto a pagar es: ", Tarifa ," euros.";
            FinSi
        FinSi
    FinSi
FinAlgoritmo