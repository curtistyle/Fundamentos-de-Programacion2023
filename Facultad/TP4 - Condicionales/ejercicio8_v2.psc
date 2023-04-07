Algoritmo ejercicio8
    Definir Numero1, Numero2, Numero3 Como Real;
	
	Escribir "Ingrese el primer numero: ";
	Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	Escribir "Ingrese el tercer numero: ";
    Leer Numero3;
	
    Si (Numero1 > 0) y (Numero2 > 0) y (Numero3 > 0) Entonces
        Si (Numero1 > Numero2) y (Numero1 > Numero3) Entonces 
            Escribir "El mayor es ", Numero1;
        SiNo
            Si (Numero2 > Numero3) y (Numero2 > Numero1) Entonces
                Escribir "El mayor es ", Numero2;
            SiNo
                Escribir "El mayor es ", Numero3;
            FinSi
        FinSi
    SiNo
        Escribir "Los numeros ingresados no son positivos.";
    FinSi
FinAlgoritmo