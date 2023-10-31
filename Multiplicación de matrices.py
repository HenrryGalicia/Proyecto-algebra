import numpy as np
import matplotlib.pyplot as plt

matriz1 = np.array([[4, -1]])
matriz2 = np.array([[3, 0]])

resultado = matriz1 * matriz2

print("Resultado de la multiplicación:")
print(resultado)

plt.figure(figsize=(7, 6))
plt.gca().set_facecolor('black')

plt.plot(matriz1[0, 0], matriz1[0, 1], marker='x', markersize=10, color='yellow', label='Matriz 1', linestyle='None')

plt.plot(matriz2[0, 0], matriz2[0, 1], marker='x', markersize=10, color='blue', label='Matriz 2', linestyle='None')

plt.plot([0, resultado[0, 0]], [0, resultado[0, 1]], linestyle='--', color='red', label='Resultado')

xlabel='Resultado'
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.xlabel('x', color='blue')
plt.ylabel('y', color='green')
plt.axhline(0, color='pink', linewidth=0.75)
plt.axvline(0, color='orange', linewidth=0.75)
plt.grid(color='white', linestyle='--', linewidth=0.60)
plt.suptitle('Proyecto Algebra Lineal', color='purple')
plt.title('Gráfica de Multiplicación de Matrices', color='blue')
plt.legend()
plt.show()
