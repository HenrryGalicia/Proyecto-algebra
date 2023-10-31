import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


A = np.array([[2, 3], [-7, 4]])
B = np.array([-1, 47])

det_A = np.linalg.det(A)
det_x = np.linalg.det(np.column_stack((B, A[:, 1])))
det_y = np.linalg.det(np.column_stack((A[:, 0], B)))

x = det_x / det_A
y = det_y / det_A

x_values_2x2 = np.linspace(-10, 10, 400)
y1_values_2x2 = (-A[0, 0] * x_values_2x2 - B[0]) / A[0, 1]
y2_values_2x2 = (-A[1, 0] * x_values_2x2 - B[1]) / A[1, 1]

A_3x3 = np.array([[2, 1, 1], [3, -2, -3], [8, 2, 5]])
B_3x3 = np.array([6, 5, 11])

det_A_3x3 = np.linalg.det(A_3x3)
det_x_3x3 = np.linalg.det(np.column_stack((B_3x3, A_3x3[:, 1:])))
det_y_3x3 = np.linalg.det(np.column_stack((A_3x3[:, [0, 2]], B_3x3)))
det_z_3x3 = np.linalg.det(np.column_stack((A_3x3[:, :-1], B_3x3)))

x_3x3 = det_x_3x3 / det_A_3x3
y_3x3 = det_y_3x3 / det_A_3x3
z_3x3 = det_z_3x3 / det_A_3x3

x_values_3x3 = np.linspace(-10, 10, 400)
z1_3x3 = (-A_3x3[0, 0] * x_values_3x3 - A_3x3[0, 1] * y_3x3 - B_3x3[0]) / A_3x3[0, 2]
z2_3x3 = (-A_3x3[1, 0] * x_values_3x3 - A_3x3[1, 1] * y_3x3 - B_3x3[1]) / A_3x3[1, 2]
z3_3x3 = (-A_3x3[2, 0] * x_values_3x3 - A_3x3[2, 1] * y_3x3 - B_3x3[2]) / A_3x3[2, 2]

matriz1 = np.array([[4, -1]])
matriz2 = np.array([[3, 0]])

resultado = matriz1 * matriz2

matriz = np.array([[3, 5], [2, 6]])

try:
    matriz_inversa = np.linalg.inv(matriz)
except np.linalg.LinAlgError:
    matriz_inversa = None

gs = gridspec.GridSpec(2, 2)

ax1 = plt.subplot(gs[0, 0])
ax1.set_facecolor('black')  
ax1.scatter(x, y, color='red', marker='x', label='Solución (x, y)')
ax1.set_xlabel('x', color='blue')
ax1.set_ylabel('y', color='blue')
ax1.set_title('Gráfica de las Ecuaciones 2x2', color='blue')
ax1.plot(x_values_2x2, y1_values_2x2, label='2x + 3y = -1')
ax1.plot(x_values_2x2, y2_values_2x2, label='-7x + 4y = 47')
ax1.grid(True, color='red', linestyle='--', linewidth=0.5)
ax1.legend()

ax2 = plt.subplot(gs[0, 1])
ax2.set_facecolor('black') 
ax2.plot(x_values_3x3, z1_3x3, label='2x + y + z = 6', color='pink')
ax2.plot(x_values_3x3, z2_3x3, label='3x - 2y - 3z = 5', color='yellow')
ax2.plot(x_values_3x3, z3_3x3, label='8x + 2y + 5z = 11')
ax2.set_xlabel('x', color='blue')
ax2.set_ylabel('z', color='blue')
ax2.set_title('Gráfica de las Ecuaciones 3x3 x y z', color='blue')
ax2.grid(color='red', linestyle='--', linewidth=0.5)
ax2.legend()

ax3 = plt.subplot(gs[1, 0])
ax3.set_facecolor('black') 
ax3.plot([0, resultado[0, 0]], [0, resultado[0, 1]], linestyle='--', color='red', label='Resultado')
ax3.set_xlim(-15, 15)
ax3.set_ylim(-15, 15)
ax3.set_xlabel('x', color='blue')
ax3.set_ylabel('y', color='green')
ax3.axhline(0, color='pink', linewidth=0.75)
ax3.axvline(0, color='orange', linewidth=0.75)
ax3.set_title('Gráfica de Multiplicación de Matrices', color='blue')
ax3.legend()

ax4 = plt.subplot(gs[1, 1])
ax4.set_facecolor('black') 
if matriz_inversa is not None:
    ax4.scatter(matriz_inversa[0, 0], matriz_inversa[1, 0], color='green', marker='x', label='Resultado Matriz inversa')
    ax4.set_xlim(-10, 10)
    ax4.set_ylim(-10, 10)
    ax4.set_xlabel('x', color='blue')
    ax4.set_ylabel('y', color='green')
    ax4.axhline(0, color='red', linewidth=0.10)
    ax4.axvline(0, color='red', linewidth=0.10)
    ax4.grid(color='red', linestyle='-', linewidth=0.25)
    ax4.set_title('Gráfica de la Inversa de la Matriz', color='blue')
    ax4.legend()
else:
    ax4.text(0.5, 0.5, 'La matriz no tiene inversa', fontsize=12, color='red', ha='center')

plt.tight_layout()

plt.suptitle('Portafolio de Gráficas', color='purple')
plt.show()
