import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator
import os

#Inicializar contenedores de coordenadas
verticalCounter = 0
horizontalCounter = 0
depthCounter = 0

ruta_absoluta = "C:\\rana\\datos.txt"

# Leer los números del archivo txt
with open(ruta_absoluta, 'r') as file:
    steps = [float(line.strip()) for line in file]

def random_walk():
    global verticalCounter, horizontalCounter, depthCounter

    # Listas para almacenar las coordenadas
    x_coords = [horizontalCounter]
    y_coords = [verticalCounter]
    z_coords = [depthCounter]

    n = 1/6
    
    # Realiza salto de la rana
    for step in steps:
        if 0 < step <= n:
            verticalCounter += 1
        elif n < step <= 2 * n:
            verticalCounter -= 1
        elif 2 * n < step <= 3 * n:
            horizontalCounter += 1
        elif 3 * n < step <= 4 * n:
            horizontalCounter -= 1
        elif 4 * n < step <= 5 * n:
            depthCounter += 1
        else:
            depthCounter -= 1

        # Registrar las coordenadas en la serie    
        x_coords.append(horizontalCounter)
        y_coords.append(verticalCounter)
        z_coords.append(depthCounter)
    
    # crea una figuar 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # graficar el recorrido de la rana
    ax.plot(x_coords, y_coords, z_coords, marker='o')

    # etiqueta los ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z') 

    # Mostrar el grafico
    plt.show()   

# llama la funcion ramdon walk para ejecutarla
    
random_walk()