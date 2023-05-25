from PIL import Image
import numpy as np
from scipy.ndimage import convolve

# Carrega a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Converte a imagem para um array numpy
imagem_array = np.array(imagem)

# Define o kernel do filtro de desfoque gaussiano
sigma = 1.0  # Valor do desvio padrão
size = int(2 * np.ceil(3 * sigma) + 1)  # Tamanho do kernel
kernel = np.fromfunction(lambda x, y: (1/(2 * np.pi * sigma**2)) * np.exp(-((x - size//2)**2 + (y - size//2)**2)/(2 * sigma**2)), (size, size))
kernel = kernel / np.sum(kernel)  # Normaliza o kernel para que a soma dos elementos seja igual a 1

# Aplica o filtro de defoque gaussiano na imagem usando o kernel
imagem_filtrada_array = np.zeros_like(imagem_array)  # Cria uma matriz de zeros com as mesmas dimensões da imagem
for i in range(3):  # Itera sobre os canais de cores (R, G, B)
    imagem_filtrada_array[:, :, i] = convolve(imagem_array[:, :, i], kernel)

# Converte a matriz de volta para uma imagem usando o Pillow
imagem_filtrada = Image.fromarray(imagem_filtrada_array.astype(np.uint8))

# Salva a imagem filtrada
imagem_filtrada.save("imagem_filtrada-Gauss.jpg")
