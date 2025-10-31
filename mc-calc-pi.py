# Cálculo e comparação da área estimada do círculo usando o método de Monte Carlo puro com diferentes tamanhos de amostra. 
# Os resultados são visualizados em um gráfico que mostra a média estimada e o desvio padrão para cada amostragem utilizada.

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
raio = 1.0
amostras_list = [10, 
                 25, 
                 50, 
                 100, 
                 150, 
                 300, 
                 500, 
                 1000, 
                 10000]
num_runs = 50

area_square = (2*raio)**2

def monte_carlo_area(n_points, radius):
    x = np.random.uniform(-radius, radius, n_points)
    y = np.random.uniform(-radius, radius, n_points)
    dentro = (x**2 + y**2) <= radius**2
    frac_dentro = np.sum(dentro) / n_points
    area_est = frac_dentro * area_square
    return area_est

areas_mean = []
areas_std = []
print("Valor real do Pi: ", np.pi)
for n_points in amostras_list:
    amostra = [monte_carlo_area(n_points, raio) for _ in range(num_runs)]
    areas_mean.append(np.mean(amostra))
    areas_std.append(np.std(amostra))
    print(n_points, "Valor calculado: ", np.mean(amostra) , "Desvio padrão: ", np.std(amostra))

plt.figure(figsize=(9,5))

# Plota a média
plt.plot(amostras_list, areas_mean, 'o-', label='Estimativa Monte Carlo')

# Preenche a região do desvio padrão
areas_upper = np.array(areas_mean) + np.array(areas_std)
areas_lower = np.array(areas_mean) - np.array(areas_std)
plt.fill_between(amostras_list, areas_lower, areas_upper, color='blue', alpha=0.25, label='Desvio padrão')

# Linha horizontal para área verdadeira
plt.axhline(np.pi * raio**2, color='red', linestyle='--', label='Área verdadeira')

# Eixo x logarítmico
plt.xscale('log')

plt.xlabel('Número de Pontos (escala logaritmica)')
plt.ylabel('Área estimada (valor de Pi)')
plt.title('Estimativa da Área do Círculo (valor de Pi dado que o raio = 1) por Monte Carlo')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
