Algoritmo ejercicio13
    Definir Dia, Mes, Anio, siguienteDia, SiguienteMes, siguienteAnio Como Entero;
	
    siguienteDia <- 0;
    siguienteMes <- 0;
    siguienteAnio <- 0;
	
	Escribir "Ingrese el Dia: ";
    Leer Dia;
	Escribir "Ingrese el Mes: ";
	Leer Mes;
	Escribir "Ingrese el Año: ";
	Leer Anio;
    Si (Mes = 2) Entonces
        Si ((Anio mod 4) = 0) y (((anio mod 100) <> 0) o ((anio mod 400) = 0)) Entonces
            Si (Dia = 29) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDias <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        SiNo
            Si (Dia = 28) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        FinSi
    SiNo
        Si (Mes = 4) o (Mes = 6) o (Mes = 9) o (Mes = 11) Entonces
            Si (Dia = 30) Entonces
                siguienteDia <- 1;
                siguienteMes <- Mes + 1;
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        SiNo
            Si (Dia = 31) Entonces
                Si (Mes = 12) Entonces
                    siguienteDia <- 1;
                    siguienteMes <- 1;
                    siguienteAnio <- Anio + 1;
                SiNo
                    siguienteDia <- Dia + 1;
                    siguienteMes <- Mes;
                FinSi
            SiNo
                siguienteDia <- Dia + 1;
                siguienteMes <- Mes;
            FinSi
        FinSi
    FinSi
	
    Si (siguienteAnio <> 0) Entonces
        Escribir 'El dia siguiente es: ', siguienteDia ,'/', siguienteMes ,'/', siguienteAnio;
    SiNo
        Escribir 'El dia siguiente es: ', siguienteDia ,'/', siguienteMes, '/', Anio;
    FinSi
FinAlgoritmo