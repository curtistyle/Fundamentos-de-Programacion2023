import json


with open( "Facultad\TP - Archivos\main.txt", "r", encoding="utf-8" ) as item:
    for texto in item.readlines():
        print(texto, end="")
    

with open( "Facultad\TP - Archivos\main.txt", "a", encoding="utf-8" ) as item:
    item.write("\n")
    item.write("Nueva lieaa 1 \n")
    item.write("Nueva lieaa 2 \n")
    item.write("Nueva lieaa 3")
    
print(end="\n\n")

f = open( "Facultad\TP - Archivos\dyct.json", "r", encoding="utf-8" )
print( type(f) )

var = json.load(f)
print(var)

