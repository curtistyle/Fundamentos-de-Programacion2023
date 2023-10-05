""" Escribir una declaración de tipo registro que almacene la sig. información sobre un disco de audio: 
título, autor, año de publicación y duración en segundos. """

# for key, item in disco.items():
#     print(key, item)

import math


tipo_disco = {
    "titulo"   : str(),
    "autor"    : str(),
    "año"      : int(),
    "duracion" : str()
}

def _min(segundos : int):
    minutos = segundos / 60
    str_minutos = str(f"{minutos:.2f}")
    minutos = str_minutos.replace(".", ":")
    return minutos

def cargar_registro(registro : tipo_disco):
    registro["titulo"]   = input("Ingrese el titulo del disco: ")
    registro["autor"]    = input("Ingrese el autor de disco: ")
    registro["año"]      = int(input("Ingrese el año del disco: "))
    registro["duracion"] = _min(int(input("Ingrese la duracion del disco: ")))




if __name__ == "__main__":

    disco = tipo_disco
    
    cargar_registro(disco)
    
    print(f"Titulo: {disco['titulo']}")
    print(f"autor: {disco['autor']}")
    print(f"Año: {disco['año']}")
    print(f"Duracion: {disco['duracion']}")
