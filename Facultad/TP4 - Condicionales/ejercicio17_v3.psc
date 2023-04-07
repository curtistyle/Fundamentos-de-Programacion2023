Algoritmo ejercicio17
	Definir Operador Como Caracter;
	Definir Numero1, Numero2 Como Real;
	
	Escribir "Ingrese el primer numero: ";
	Leer Numero1;
	Escribir "Ingrese el operador: ";
	Leer Operador;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
    Segun Operador Hacer
        "+" : 
            Escribir "Resultado: ", Numero1 + Numero2;
        "-" :
            Escribir "Resultado: ", Numero1 - Numero2;
        "*" :
            Escribir "Resultado: ", Numero1 * Numero2;
        "/" :
            Si (Numero2 <> 0) Entonces
                Escribir "Resultado: ", Numero1 / Numero2;
            SiNo
                Escribir "No se puede dividir por 0";
            FinSi
		De otro modo:
			Escribir "Operador invalido";
    FinSegun 
FinAlgoritmo