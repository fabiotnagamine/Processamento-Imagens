from PIL import Image

# Carrega a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Obtem os pixels da imagem
pixels = imagem.load()

# Ajusta o fator de brilho da imagem
fator_brilho = 1.5  # Valor maior que 1 para aumentar o brilho, valor entre 0 e 1 para diminuir o brilho

# Percorre todos os pixels da imagem
largura, altura = imagem.size
for x in range(largura):
    for y in range(altura):
        r, g, b = pixels[x, y]
        r = int(r * fator_brilho)
        g = int(g * fator_brilho)
        b = int(b * fator_brilho)
        pixels[x, y] = (r, g, b)

# Salva a imagem com o brilho ajustado
imagem.save("caminho/para/imagem_com_brilho.jpg")
