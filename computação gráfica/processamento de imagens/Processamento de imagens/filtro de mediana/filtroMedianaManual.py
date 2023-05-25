import numpy as np
from PIL import Image

# Carrega a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Converte a imagem para um array NumPy
imagem_array = np.array(imagem)

# Obtem as dimensões da imagem
altura, largura, canais = imagem_array.shape

# Cria uma matriz vazia para a imagem filtrada
imagem_filtrada = np.zeros_like(imagem_array)

# Definir o tamanho da janela do filtro de mediana
tamanho_janela = 3

# Calcular o deslocamento para o centro da janela
offset = tamanho_janela // 2

# Percorra os pixels da imagem
for i in range(offset, altura - offset):
    for j in range(offset, largura - offset):
        # Extraia a vizinhança do pixel atual
        vizinhanca = imagem_array[i - offset: i + offset + 1, j - offset: j + offset + 1, :]

        # Calcule a mediana para cada canal de cor
        for canal in range(canais):
            pixel = vizinhanca[:, :, canal]
            mediana = np.median(pixel)
            imagem_filtrada[i, j, canal] = mediana

# Crie uma nova imagem a partir do array filtrado
imagem_filtrada = Image.fromarray(imagem_filtrada.astype(np.uint8))

# Salve a imagem filtrada
imagem_filtrada.save("imagem_filtrada-manual.jpg")
