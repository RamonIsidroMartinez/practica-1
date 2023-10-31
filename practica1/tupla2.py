palabras = ('manzana', 'pera', 'platano', 'naranja', 'uva')
total_a = 0
for palabra in palabras:
    total_a += palabra.count('a')
print(f"El número total de letras 'a' en todas las palabras es {total_a}.")