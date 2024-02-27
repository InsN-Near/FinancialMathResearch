import matplotlib.pyplot as plt
import numpy as np

#Definindo a função
def minha_funcao(x):
    return 12.85 * x - 15.78 * x**2 + 5.2e-7

#Coeficientes da função quadrática
a = -15.78
b = 12.85
c = 5.2e-7

#Coordenada x do vértice
x_v = -b / (2 * a)

#Gerando valores de x em torno do vértice
x_values = np.linspace(0, 3, 200)  # Intervalo menor de x

#Calculando os valores de y correspondentes
y_values = minha_funcao(x_values)

#Plotando o gráfico da função quadrática
plt.plot(x_values, y_values, label='y = 12.85x - 15.78x² + 5.2E-07')

#Definindo limites dos eixos
plt.xlim(0, 1.0)  # Limites menores em x
plt.ylim(0, 3)  # Limites menores em y

#Configurações do gráfico
plt.title('Gráfico da Curva de Laffer')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

#Determinando os pontos de interseção
x_intersect_red = 0.4073
x_intersect_green = 0.3456
y_intersect_red = minha_funcao(x_intersect_red)
y_intersect_green = minha_funcao(x_intersect_green)

#Pontos de interseção
plt.plot([x_intersect_red, x_intersect_red], [0, y_intersect_red], color='red', linestyle='--', label='Ponto de máximo (40,73%)')
plt.plot([x_intersect_green, x_intersect_green], [0, y_intersect_green], color='green', linestyle='--', label='Taxa observada (34,56%)')

plt.legend()
plt.show()