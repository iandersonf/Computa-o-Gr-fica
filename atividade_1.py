import numpy as np
import matplotlib.pyplot as plt

# Definindo as variáveis
wJanela = 100.0  # largura da janela em metros
hJanela = 100.0  # altura da janela em metros
dJanela = 10.0  # distância da janela ao olho do pintor
rEsfera = 5  # raio da esfera em metros
esfColor = (255/255, 0/255, 0/255)  # cor da esfera (vermelho)
bgColor = (100/255, 100/255, 100/255)  # cor de fundo (cinza)

# Definindo o número de colunas e linhas
nCol = 50  # número de colunas
nLin = 50   # número de linhas

# Dimensões dos retângulos da tela de mosquito
Dx = wJanela / nCol
Dy = hJanela / nLin

# Inicializando a matriz de cores do Canvas
canvas = np.zeros((nLin, nCol, 3))  # 3 para RGB

# Posição do observador
observador = np.array([0, 0, 0])  # observador na origem

# Loop sobre as linhas e colunas
for linha in range(nLin):
  for coluna in range(nCol):
    # Calculando as coordenadas do centro do retângulo na tela de mosquito
    y = hJanela / 2 - Dy / 2 - linha * Dy
    x = -wJanela / 2 + Dx / 2 + coluna * Dx

    # Vetor direção do raio
    dir_ray = np.array([x, y, -dJanela])  # ponto na janela

    # Norma vetor
    norm_dir_ray = np.sqrt(np.sum(dir_ray**2))  # √(x² + y² + z²)

    dir_ray_normalized = dir_ray / norm_dir_ray  # normalizando o vetor

    # Centro da esfera
    esfera_center = np.array([0, 0, -(dJanela + rEsfera)])

    # Equação da esfera: (X - centerX)² + (Y - centerY)² + (Z - centerZ)² = rEsfera²
    # (Po + ti * dr - c)² = rEsfera²
    # v = Po - c
    # (v + ti * dr) . (v + ti * dr) = rEsfera²
    # v² + 2ti * (v . dr) + ti² * (dr . dr) = rEsfera²
    # (v . dr)² + 2ti * (v . dr) + ti² * (dr . dr) - rEsfera² = 0
    # (dr . dr) * ti² + 2ti * (v . dr) + v² - rEsfera² = 0

    a = np.dot(dir_ray_normalized, dir_ray_normalized)
    b = 2 * np.dot(dir_ray_normalized, (esfera_center - observador))
    c = np.dot(esfera_center, esfera_center) - rEsfera**2

    # Discriminante
    discriminant = b**2 - 4 * a * c

    # Verificando a interseção
    if discriminant < 0:
      # Não há interseção
      canvas[int(linha), int(coluna)] = bgColor  # cor de fundo

    else:
      ti_pos = (-b + np.sqrt(discriminant)) / (2 * a)  # raiz positiva
      ti_neg = (-b - np.sqrt(discriminant)) / (2 * a)  # raiz negativa

      # print(f"Valores encaixados linha: {y} e coluna: {x}")
      # print(f"Valores encaixados linha: {linha} e coluna: {coluna}")
      print(f"Valores encaixados linha: {int(x)} e coluna: {int(y)}")

      # Há interseção ou tangência
      canvas[int(linha), int(coluna)] = esfColor  # cor da esfera

# Verificando as dimensões do canvas antes de plotar
print(f"Dimensões do canvas: {canvas.shape}")  # Deve ser (nLin, nCol, 3)

# Plotando o canvas
plt.imshow(canvas, extent=(-wJanela/2, wJanela/2, -hJanela/2, hJanela/2))
plt.title('Visualização da Esfera no Canvas')
plt.xlabel('X (metros)')
plt.ylabel('Y (metros)')
plt.axis('on')
plt.show()
