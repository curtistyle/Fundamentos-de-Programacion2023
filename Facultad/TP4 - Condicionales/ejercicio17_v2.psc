Algoritmo ejercicio17
	Definir Operador Como Caracter;
	Definir Numero1, Numero2, Resultado Como Real;
	
	Escribir "Ingrese el primer numero: ";
	Leer Numero1;
	Escribir "Ingrese el operador: ";
	Leer Operador;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Segun Operador Hacer
        "+" : 
            Resultado <- Numero1 + Numero2;
            Escribir "Resultado: ", Resultado;
        "-" :
            Resultado <- Numero1 - Numero2;
            Escribir "Resultado: ", Resultado;
        "*" :
            Resultado <- Numero1 * Numero2;
            Escribir "Resultado: ", Resultado;
        "/" :
            Si (Numero2 <> 0) Entonces
                Resultado <- Numero1 / Numero2;
                Escribir "Resultado: ", Resultado;
            SiNo
                Escribir "No se puede dividir por 0";
            FinSi
		De otro modo:
			Escribir "Operador invalido";
    FinSegun 
FinAlgoritmo
