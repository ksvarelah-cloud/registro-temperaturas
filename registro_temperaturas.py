
import random

# Registro automático de temperaturas diarias en varias ciudades
# Dimensiones: ciudades x días de la semana x semanas

# Configuración
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Crear matriz 3D con temperaturas aleatorias (15-35 °C)
temperaturas = [
    [ [random.randint(15, 35) for semana in range(num_semanas)] for dia in range(len(dias_semana)) ]
    for ciudad in ciudades
]

# Mostrar matriz completa
print("Matriz de temperaturas (Ciudad x Día x Semana):\n")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}:")
    for dia_idx, dia in enumerate(dias_semana):
        print(f"  {dia}: {temperaturas[i][dia_idx]}")
    print()

# Calcular y mostrar promedio de temperaturas por ciudad y semana
print("Promedios de temperaturas por ciudad y semana:\n")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}:")
    for semana in range(num_semanas):
        suma = sum(temperaturas[i][dia][semana] for dia in range(len(dias_semana)))
        promedio = suma / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")
