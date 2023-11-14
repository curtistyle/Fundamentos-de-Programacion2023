with open("Facultad\TP - Archivos\salarios.txt", "w", encoding="utf-8") as fichero:
    # ID, Nombre, Apellido, Sueldo, Horas trabajadas
    lineas = [
        "001 Francisco Sanchez 420200.50 80\n", 
        "002 Laura Perez 380000.50 78\n",
        "003 Jose Diaz 400500.50 79\n",
        "004 Raul Gonzales 420200.50 80\n"
        ]
    fichero.writelines( lineas )
