Calcula
la
temperatura
promedio
por
ciudad
a
partir
de
los
datos
de
varias
semanas.

Parámetros:
datos(dict): Un
diccionario
donde
la
clave
es
el
nombre
de
la
ciudad
y
el
valor
es
una
lista
con
las
temperaturas
semanales.

Retorna:
dict: Diccionario
con
el
promedio
de
temperaturas
por
ciudad.
"""
promedios = {}  # Diccionario donde guardaremos los resultados

for ciudad, temperaturas in datos.items():
    # Verificamos que la lista no esté vacía
    if len(temperaturas) > 0:
        promedio = sum(temperaturas) / len(temperaturas)
    else:
        promedio = 0  # Si no hay datos, devolvemos 0

    # Guardamos el resultado en el diccionario
    promedios[ciudad] = promedio

return promedios


# ------------------------------------------------
# Datos de ejemplo: 3 ciudades, 4 semanas
# ------------------------------------------------
temperaturas = {
"Quito": [20, 22, 19, 21],
"Guayaquil": [28, 30, 29, 27],
"Cuenca": [18, 17, 19, 16]
}

# ------------------------------------------------
# Prueba de la función
# ------------------------------------------------
resultados = calcular_promedio_temperaturas(temperaturas)

print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultados.items():
print(f"- {ciudad}: {promedio:.2f} °C")
