// Se conocen las compras realizadas por una universidad (N), de cada una
// se procesa cantidad, descripción, total abonado y rubro al que pertenece
// la compra (librería, producto de limpieza o equipamiento). Se supone que
// por cada factura se compra un solo tipo de artículo. Se pide:
//	   a. Total abonado por rubro y en total.
//	   b. Determinar si se compraron resmas de hojas, si es así mostrar la
//		   cantidad total y los montos abonados en conceptos de este ítem,
//		   además en que rubro se clasificó.
//	   c. Suponer que debe buscar una factura de compra que se realizó de
//		   punteros láser para anularla, indicar si hay una factura o más, si es
//		   así mostrar cuantas facturas se emitieron por este concepto y
//		   cantidad de punteros comprados en ambos casos.

Algoritmo ejercicio2
	Definir Indice, Cantidad, CantidadResma, CantidadPunteros, ContadorFactura, NumeroCompras Como Entero;
	Definir Descripcion, Rubro, RubroResmas Como Cadena;
	Definir TotalAbonado, TotalAbonadoResmas Como Real;
	
	TotalAbonadoResmas <- 0;
	RubroResmas <- '';
	CantidadResma <- 0;
	ContadorFactura <- 0;
	CantidadPunteros <- 0;
	
	Escribir "Ingrese la cantidad de compras realizadas por la universidad.";
	Leer NumeroCompras;
	Si NumeroCompras > 0 Entonces
		Para Indice <- 1 Hasta NumeroCompras Hacer
			Escribir ">> Compra Numero [",Indice,"] <<";
			Escribir "Ingrese la descripcion del articulo: ";
			Leer Descripcion;
			Escribir "Ingrese la cantidad del articulo: ";
			Leer Cantidad;
			Escribir "Ingrese el rubro al que pertenece la compra: ";
			Leer Rubro;
			Escribir "Ingrese el total abonado: ";
			Leer TotalAbonado;
			
			Si (Descripcion = 'Resmas') Entonces
				RubroResmas <- Rubro;
				CantidadResma <- Cantidad;
				TotalAbonadoResmas <- TotalAbonado;
			FinSi
			
			Si (Descripcion = 'Puntero laser') Entonces
				ContadorFactura <- ContadorFactura + 1;
				CantidadPunteros <- CantidadPunteros + Cantidad;
			FinSi
		FinPara	
	FinSi
	
	Si (CantidadResma <> 0) Entonces
		Escribir "Se compraron ",CantidadResma," resmas de hojas en el rubro: ", RubroResmas ," y se abono un total de $",TotalAbonadoResmas,".";
	FinSi
	
	Escribir "Ingrese la descripcion de un producto:  ";
	Leer Descripcion;
	
	Si ((Descripcion = 'Puntero laser') o (Descripcion = 'puntero laser')) y (ContadorFactura > 0) Entonces
		Escribir "Se encontraron ", ContadorFactura ," facturas de punteros lasers.";
		Escribir "Se compraron en total ", CantidadPunteros ," punteros lasers.";
	SiNo
		Escribir "No existen facturas de ", Descripcion ,"."; 
	FinSi	
FinAlgoritmo
