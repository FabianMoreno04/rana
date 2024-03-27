import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator

ruta_absoluta = "C:\\rana\\datos.txt"

# Leer los números del archivo txt
with open(ruta_absoluta, 'r') as file:
    steps = [float(line.strip()) for line in file]

# Inicializar contadores y series para almacenar las coordenadas
horizontalCounter = 0
verticalCunter = 0

#Listas para almacenar las coordenadas
x_coords = [horizontalCounter]
y_coords = [verticalCunter]

n=1/4
# Realizar el recorrido de la rana en 2D
for step in (steps):
    if 0 < step <= n:
        verticalCunter += 1
    elif n < step <= 2 * n:
        verticalCunter -= 1
    elif 2 * n < step <= 3 * n:
        horizontalCounter += 1
    elif 3 * n< step <= 4:
        horizontalCounter -= 1

    # Registrar las coordenadas en la serie
    x_coords.append(horizontalCounter)
    y_coords.append(verticalCunter)

# Crear el gráfico 1D
plt.plot(x_coords[:-1], y_coords[:-1], marker='o')
plt.plot(x_coords[-1], y_coords[-1], marker='o')

# Etiquetas de ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()