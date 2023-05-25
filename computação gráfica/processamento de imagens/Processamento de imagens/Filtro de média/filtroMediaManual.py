import numpy as np
from PIL import Image

# Carregue a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/processamento de imagens/Processamento de imagens/polinesiaFrancesa.png")

# Converta a imagem para um array NumPy
imagem_array = np.array(imagem)

# Obtenha as dimensões da imagem
altura, largura, canais = imagem_array.shape

# Crie uma matriz vazia para a imagem filtrada
imagem_filtrada = np.zeros_like(imagem_array)

# Defina o tamanho da janela do filtro de média
tamanho_janela = 3

# Calcule o deslocamento para o centro da janela
offset = tamanho_janela // 2

# Percorra os pixels da imagem
for i in range(offset, altura - offset):
    for j in range(offset, largura - offset):
        # Extraia a vizinhança do pixel atual
        vizinhanca = imagem_array[i - offset: i + offset + 1, j - offset: j + offset + 1, :]

        # Calcule a média para cada canal de cor
        for canal in range(canais):
            pixel = vizinhanca[:, :, canal]
            media = np.mean(pixel)
            imagem_filtrada[i, j, canal] = media

# Crie uma nova imagem a partir do array filtrado
imagem_filtrada = Image.fromarray(imagem_filtrada.astype(np.uint8))

# Salve a imagem filtrada
imagem_filtrada.save("filtro-media-manual.png")
