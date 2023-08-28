persons = [
    {"name" : "L. Messi", "year" : 36, "dorsal" : 10},
    {"name" : "A. Di Maria", "year" : 35, "dorsal" : 11},
    {"name" : "A. Varela", "year" : 22, "dorsal" : 22},
    {"name" : "C. Medina", "year" : 21, "dorsal" : 36}
]

print(f'{"Nombre":<15}{"Edad":<14}{"Dorsal":<10}')
for person in persons:
    print(f"{person['name']:<15}{person['year']:<14}{person['dorsal']:<10}")