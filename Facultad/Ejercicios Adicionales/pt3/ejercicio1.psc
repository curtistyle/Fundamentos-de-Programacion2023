// 1. Se tienen los 10 cobradores de un club de barrio, de cada uno se lee apellido y nombre, total
//    cobrado y cantidad de socios asignados. Se pide:
//	    a. Cargar los datos y asignarle un premio a cada cobrador de acuerdo al monto
//	       recaudado, si este es mayor a $100000, el premio será del 10%, caso contrario del
//		   5%. Aquellos cobradores que recauden más de $200000, recibirán un premio extra
//		   del 8%. Mostrar premio total que percibirá cada cobrador.
//		b. Mostrar la cantidad de clientes que posee el club.
//		c. Calcular total recaudado por el club.
//		d. Mostrar cual cobrador recaudó más dinero.
//		e. Indicar si Mora Ballay es cobradora del club, si es así mostrar sus datos.

Algoritmo ejercicio1
	Definir Cobradores, Cantidad_Socios, Socios, Mayor_Recaudador, Aux_Socios Como Entero;
	Definir Nombre, Apellido Como Cadena;
	Definir Total_Cobrado, Premio, Total_Recaudad, Aux_Total_Cobrado Como Real;
	
	Cobradores <- 0;
	Cantidad_Socios <- 0;
	Total_Recaudado <- 0;
	Aux_Recaudado <- 0;
	Aux_Total_Cobrado <- 0;
	Aux_Socios <- 0;
	
	Para Cobradores <- 1 Hasta 10 Hacer
		Escribir "*** Cobrador Nº ",Cobradores,". ***";
		
		Escribir " > Nombre: ";
		Leer Nombre;
		Escribir " > Apellido: ";
		Leer Apellido;
		Escribir " > Total Cobrado: ";
		Leer Total_Cobrado;
		Escribir " > Cantidad de Socios Asignados: ";
		Leer Socios;
		
		Cantidad_Socios <- Cantidad_Socios + Socios;
		Total_Recaudado <- Total_Recaudado + Total_Cobrado;
		
		Si (Total_Cobrado > 200000) Entonces
			Premio <- ((Total_Cobrado * 18) / 100);
		SiNo
			Si (Total_Cobrado > 10000) Entonces
				Premio <- ((Total_Cobrado * 10) / 100);
			SiNo
				Premio <- ((Total_Cobrado * 5) / 100);
			FinSi
		FinSi
		
		Si (Total_Cobrado > Aux_Recaudado) Entonces
			Aux_Recaudado <- Total_Cobrado;
			Mayor_Recaudador <- Cobradores;
		FinSi
		
		Si (Nombre = 'Mora') y (Apellido = 'Ballay') Entonces
			Aux_Total_Cobrado <- Total_Cobrado;
			Aux_Socios <- Socios;
		FinSi
	FinPara
FinAlgoritmo
