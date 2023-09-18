import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia Euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Función para generar datos aleatorios en una dimensión d
def generate_data(dimension, num_points):
    return np.random.rand(num_points, dimension)

# Función para crear un histograma de distancias Euclidianas
def create_histogram(distances, dimension):
    plt.hist(distances, bins=20, alpha=0.5, label=f'Dimensión {dimension}')
    plt.xlabel('Distancia Euclidiana')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.title(f'Histograma de Distancias (Dimensión {dimension})')

if __name__ == "__main__":
    dimensions = [10, 50, 100, 500, 1000, 2000, 5000]
    num_points = 100

    for dimension in dimensions:
        data = generate_data(dimension, num_points)
        distances = []

        # Calcular todas las distancias entre pares de puntos
        for i in range(num_points):
            for j in range(i + 1, num_points):
                distance = euclidean_distance(data[i], data[j])
                distances.append(distance)

        plt.figure(figsize=(10, 6))
        create_histogram(distances, dimension)
    
    plt.show()
