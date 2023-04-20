Algoritmo ejercicio23
    Definir Administrativo, Transportista, Operario, Guardia Como Entero;
    Definir Edad Como Entero;
    Definir Opcion, TituloSecundario, TituloTerciario, Nombre, Apellido, Direccion, DNI Como Cadena;
    Definir Condicion Como Logico;
	
    Administrativo <- 0;
    Transportista <- 0;
    Operario <- 0;
    Guardia <- 0;
	
    Repetir
        Escribir "Seleccione el rol que desea evaluar: ";
        Escribir "  > Administrativo (1). ";
        Escribir "  > Transportista  (2). ";
        Escribir "  > Operario       (3). ";
        Escribir "  > Guaria de Seg. (4). ";
        Escribir "  > SALIR          (0). "; 
        Leer Opcion;
		
        Si ((Opcion > '0') y (Opcion < '5')) Entonces
            Escribir "Ingerse la Edad: ";
            Leer Edad;
            Escribir "Ingrese si posee el Titulo: Secundario (s/n): ";
            Leer TituloSecundario;
			
            Si (Opcion = '1') Entonces
                Escribir "Ingrese si posee el Titulo: Administración y Finanzas (s/n): ";
                Leer TituloTerciario;
            FinSi
            
            Si (Edad >= 18) y (Edad <= 55) Entonces
                Si (TituloSecundario = 's') Entonces            
                    Si (Opcion = '1') y (TituloTerciario = 's') y (Administrativo < 1) Entonces
                        Administrativo <- Administrativo + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Administrativo.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si ((Opcion = '2') y (Transportista < 1)) Entonces
                        Transportista <- Transportista + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Transportista.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si ((Opcion = '3') y (Operario < 2) y (Edad <= 50)) Entonces
                        Operario <- Operario + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Operario.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi
                    Si ((Opcion = '4') y (Guardia < 3) y (Edad <= 45)) Entonces
                        Guardia <- Guardia + 1;
                        Condicion <- Verdadero;
                        Escribir "Cumple con los requisitos para ser Guardia de seguridad.";
                    SiNo
                        Escribir "No cumple con los requisitoso o bien el puesto esta ocupado.";
                    FinSi               
                FinSi
            FinSi
			
            Si (Condicion = Verdadero) Entonces
                Escribir "Ingrese el nombre: ";
                Leer Nombre;
                Escribir "Ingrese el apellido: ";
                Leer Apellido;
                Escribir "Ingrese la direccion: ";
                Leer Direccion;
                Escribir "Ingrese el DNI: ";
                Leer DNI;
            FinSi
            Condicion <- Falso;
        SiNo
            Si (Opcion > '4') Entonces
			Escribir "Opcion incorrecta.";
            FinSi
        FinSi
    Hasta Que (Opcion = '0')   
FinAlgoritmo