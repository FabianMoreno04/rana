import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator

#obtiene la ruta del archivo txt con los datos
ruta_absoluta = "C:\\rana\\datos.txt"

# Leer los números del archivo txt
with open(ruta_absoluta, 'r') as file:
    steps = [float(line.strip()) for line in file]

# Inicializar contadores y series para almacenar las coordenadas
count = 0
x_coords = [0]
y_coords = [0]

n=1/2
i=0
# Realiza el recorrido en 1D de la rana
for step in steps:
    if step <= n:
        count += 1
    else:
        count -= 1

    # Registrar las coordenadas en la serie
    i += 1    
    x_coords.append(i)
    y_coords.append(count)

# Crear el gráfico 1D
plt.plot(x_coords, y_coords, marker='o')

# Etiquetas de ejes
plt.xlabel('Pasos')
plt.ylabel('Posicion en el eje X')

# Alinear los marcadores de los ejes y asegurarse de que sean numeros enteros
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Mostrar el gráfico
plt.show()
