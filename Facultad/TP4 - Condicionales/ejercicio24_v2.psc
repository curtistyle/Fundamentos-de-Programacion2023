Algoritmo ejercicio24
    Definir Producto1, Producto2, Producto3 Como Cadena;
    Definir Porcentaje1, Porcentaje2, Porcentaje3 Como Real;
	
	Escribir "Ingrese el nombre del primer producto: ";
	Leer Producto1;
	
	Escribir "Ingrese su porcentaje: ";
	Leer Porcentaje1;
	
	Escribir "Ingrese el nombre del segundo producto: ";
	Leer Producto2;
	
	Escribir "Ingrese su porcentaje: ";
	Leer Porcentaje2;
	
	Escribir "Ingrese el nombre del tercer producto: ";
	Leer Producto3;
	
	Escribir "Ingrese su porcentaje: ";
	Leer Porcentaje3;
	
    Si (Porcentaje1 >= 0) y (Porcentaje2 >= 0) y (Porcentaje3 >= 0) Entonces
        Si (Porcentaje1 < Porcentaje2) y (Porcentaje2 < Porcentaje3) Entonces
            Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
            Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
        SiNo
            Si (Porcentaje1 < Porcentaje3) y (Porcentaje3 < Porcentaje2) Entonces
                Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";   
                Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%."; 
            SiNo
                Si (Porcentaje2 < Porcentaje1) y (Porcentaje1 < Porcentaje3) Entonces
                    Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                    Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
                SiNo
                    Si (Porcentaje2 < Porcentaje3) y (Porcentaje3 < Porcentaje1) Entonces
                        Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";   
                        Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                    SiNo
                        Si (Porcentaje3 < Porcentaje1) y (Porcentaje1 < Porcentaje2) Entonces
                            Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                            Escribir "El producto: ", Producto2, " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";
                        SiNo
                            Si (Porcentaje3 < Porcentaje2) y (Porcentaje2 < Porcentaje1) Entonces
                                Escribir "El producto: ", Producto3, " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";   
                                Escribir "El producto: ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
                            SiNo
                                Si (Porcentaje1 = Porcentaje2) y (Porcentaje2 < Porcentaje3) Entonces
                                    Escribir "Los productos ", Producto1 ," y ", Producto2 , " tienen un porcentaje de aceptacion de ", Porcentaje1 ,"%";
                                    Escribir "El producto ", Producto3 , " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
                                SiNo
                                    Si (Porcentaje1 = Porcentaje3) y (Porcentaje3 < Porcentaje2) Entonces
                                        Escribir "Los productos ", Producto1 ," y ", Producto3 , " tienen un porcentaje de aceptacion de ", Porcentaje1 ,"%";
                                        Escribir "El producto ", Producto2 , " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";
                                    SiNo
										Si (Porcentaje2 = Porcentaje3) y (Porcentaje3 < Porcentaje1) Entonces
											Escribir "Los productos ", Producto2 ," y ", Producto3 , " tienen un porcentaje de aceptacion de ", Porcentaje2 ,"%";
											Escribir "El producto ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
										SiNo
											Si (Porcentaje1 = Porcentaje2) y (Porcentaje2 > Porcentaje3) Entonces
												Escribir "El producto ", Producto3 , " tiene un porcentaje de aceptacion de ", Porcentaje3 ,"%.";
												Escribir "Los productos ", Producto1 ," y ", Producto2 , " tienen un porcentaje de aceptacion de ", Porcentaje1 ,"%";
											SiNo
												Si (Porcentaje1 = Porcentaje3) y (Porcentaje3 > Porcentaje2) Entonces
													Escribir "El producto ", Producto2 , " tiene un porcentaje de aceptacion de ", Porcentaje2 ,"%.";
													Escribir "Los productos ", Producto1 ," y ", Producto3 , " tienen un porcentaje de aceptacion de ", Porcentaje1 ,"%";
												SiNo
													Escribir "El producto ", Producto1, " tiene un porcentaje de aceptacion de ", Porcentaje1 ,"%.";
													Escribir "Los productos ", Producto2 ," y ", Producto3 , " tienen un porcentaje de aceptacion de ", Porcentaje2 ,"%";
												FinSi
											FinSi
										FinSi
                                    FinSi
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    SiNo
        Escribir "Los valores ingresado son incorrectos";
    FinSi
FinAlgoritmo