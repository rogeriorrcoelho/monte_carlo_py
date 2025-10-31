<p align="center">
  <img src="Estimativa por tamanho de amostra.png" alt="Imagem do Projeto" />
</p>

Monte Carlo puro

Passo 1: Círculo de raio r (no caso de exemplo r = 1), centrado na origem.

Passo 2: O círculo estará circunscrito por um quadrado de lado 2r.

Passo 3: Gerar N pontos aleatórios com coordenadas (x,y), onde x e y variam entre −r e +r.

Passo 4: Para cada ponto, verifique se está dentro do círculo: x**2 + y**2 ≤ r**2

Passo 5: Contar o número de pontos dentro do círculo (N circle).

Passo 6: Estimar a área do círculo: Área estimada = (N circle / N) * (2r)**2

Isso porque (2r)**2 é a área do quadrado, e a razão fornece a fração da área correspondente ao círculo.
