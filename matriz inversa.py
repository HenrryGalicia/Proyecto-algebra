import numpy as np
import matplotlib.pyplot as plt

matriz = np.array([[3, 5], [2, 6]])

try:
    matriz_inversa = np.linalg.inv(matriz)
    print("Inversa de la matriz:")
    for row in matriz_inversa:
        print(" ".join("{:.2f}".format(val) for val in row))

    plt.scatter(matriz_inversa[0, 0], matriz_inversa[1, 0], color='green', marker='x', label='Resultado Matriz inversa')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_facecolor('black')
    plt.xlabel('x', color='blue')
    plt.ylabel('y', color='green')
    plt.axhline(0, color='red', linewidth=0.10)
    plt.axvline(0, color='red', linewidth=0.10)
    plt.grid(color='red', linestyle='-', linewidth=0.25)
    plt.legend()
    plt.show()

except np.linalg.LinAlgError:
    print("La matriz no tiene inversa")

