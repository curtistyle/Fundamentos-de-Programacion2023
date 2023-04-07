Algoritmo ejercicio17
    Definir Numero1, Numero2, Resultado Como Real;
    Definir Operador Como Cadena;
	
	Escribir "Calculadora.";
	Escribir "Ingrese el primer numero: ";
	Leer Numero1;
	Escribir "Ingrese el operador: ";
	Leer Operador;
	Escribir "Ingrese el segundo numero: ";
    Leer Numero2;
	
    Si (Operador = '+') Entonces
        Resultado <- Numero1 + Numero2;
        Escribir Resultado;
    SiNo
        Si (Operador = '-') Entonces
            Resultado <- Numero1 - Numero2;
            Escribir Resultado;
        SiNo
            Si (Operador = '*') Entonces
                Resultado <- Numero1 * Numero2;
                Escribir Resultado;
            SiNo
                Si (Operador = '/') y (Numero2 <> 0) Entonces   
                    Resultado <- Numero1 / Numero2;
                    Escribir Resultado;
                SiNo
                    Escribir "¡Operador incorrecto!";
                FinSi
            FinSI
        FinSi
    FinSi
FinAlgoritmo