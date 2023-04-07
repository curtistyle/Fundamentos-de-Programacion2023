Algoritmo ejercicio22
    Definir Numero1, Numero2, Numero3 Como Real;
	
    Escribir "Ingrese el primer numero: ";
	Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	Escribir "Ingrese el tercer numero: ";
	Leer Numero3;
	
    Si (Numero1 > Numero2) y (Numero2 > Numero3) Entonces
        Escribir Numero1, " > " ,Numero2, " > " ,Numero3;
    SiNo
        Si (Numero1 > Numero3) y (Numero3 > Numero2) Entonces
            Escribir Numero1, " > " ,Numero3, " > " ,Numero2;
        SiNo
            Si (Numero2 > Numero1) y (Numero1 > Numero3) Entonces
                Escribir Numero2, " > " ,Numero1, " > " ,Numero3;
            SiNo
                Si (Numero2 > Numero3) y (Numero3 > Numero1) Entonces
                    Escribir Numero2, " > " ,Numero3, " > " ,Numero1;
                SiNo
                    Si (Numero3 > Numero1) y (Numero1 > Numero2) Entonces
                        Escribir Numero3, " > " ,Numero1, " > " ,Numero2;
                    SiNo
                        Escribir Numero3, " > " ,Numero2, " > " ,Numero1;
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo