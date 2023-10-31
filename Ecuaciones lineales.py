import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 3], [-7, 4]])
B = np.array([-1, 47])

det_A = np.linalg.det(A)
det_x = np.linalg.det(np.column_stack((B, A[:, 1])))
det_y = np.linalg.det(np.column_stack((A[:, 0], B)))

x = det_x / det_A
y = det_y / det_A

print("Soluciones para el sistema 2x2:")
print("x =", x)
print("y =", y)

A_3x3 = np.array([[2, 1, 1], [3, -2, -3], [8, 2, 5]])
B_3x3 = np.array([6, 5, 11])

det_A_3x3 = np.linalg.det(A_3x3)
det_x_3x3 = np.linalg.det(np.column_stack((B_3x3, A_3x3[:, 1:])))
det_y_3x3 = np.linalg.det(np.column_stack((A_3x3[:, [0, 2]], B_3x3)))
det_z_3x3 = np.linalg.det(np.column_stack((A_3x3[:, :-1], B_3x3)))

x_3x3 = det_x_3x3 / det_A_3x3
y_3x3 = det_y_3x3 / det_A_3x3
z_3x3 = det_z_3x3 / det_A_3x3

print("\nSoluciones para el sistema 3x3:")
print("x =", x_3x3)
print("y =", y_3x3)
print("z =", z_3x3)

x_values_2x2 = np.linspace(-10, 10, 400)
y1_values_2x2 = (-A[0, 0] * x_values_2x2 - B[0]) / A[0, 1]
y2_values_2x2 = (-A[1, 0] * x_values_2x2 - B[1]) / A[1, 1]

plt.figure(figsize=(8, 6))
plt.gca().set_facecolor('black')
plt.scatter(x, y, color='red', marker='x', label='Solución (x, y)')
plt.xlabel('x', color='blue')
plt.ylabel('y', color='blue')
plt.suptitle('Proyecto Algebra Lineal', color='purple')
plt.title('Gráfica de las Ecuaciones 2x2', color='blue')
plt.plot(x_values_2x2, y1_values_2x2, label='2x + 3y = -1')
plt.plot(x_values_2x2, y2_values_2x2, label='-7x + 4y = 47')
plt.legend()
plt.grid(True, color='red', linestyle='--', linewidth=0.5)


x_values_3x3 = np.linspace(-10, 10, 400)
z1_3x3 = (-A_3x3[0, 0] * x_values_3x3 - A_3x3[0, 1] * y_3x3 - B_3x3[0]) / A_3x3[0, 2]
z2_3x3 = (-A_3x3[1, 0] * x_values_3x3 - A_3x3[1, 1] * y_3x3 - B_3x3[1]) / A_3x3[1, 2]
z3_3x3 = (-A_3x3[2, 0] * x_values_3x3 - A_3x3[2, 1] * y_3x3 - B_3x3[2]) / A_3x3[2, 2]

plt.figure(figsize=(8, 6))
plt.gca().set_facecolor('black')
plt.plot(x_values_3x3, z1_3x3, label='2x + y + z = 6', color='pink')
plt.plot(x_values_3x3, z2_3x3, label='3x - 2y - 3z = 5', color='yellow')
plt.plot(x_values_3x3, z3_3x3, label='8x + 2y + 5z = 11')
plt.xlabel('x', color='blue')
plt.ylabel('z', color='blue')
plt.legend()
plt.suptitle('Proyecto Algebra Lineal', color='purple')
plt.title('Gráfica de las Ecuaciones 3x3 x y z', color='blue')
plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.subplots_adjust(bottom=0.01) 

plt.scatter(x_3x3, z_3x3, color='green', marker='x')

plt.show()
