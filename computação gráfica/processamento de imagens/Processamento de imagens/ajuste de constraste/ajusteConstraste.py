from PIL import Image

# Carregua a imagem desejada a partir de um diretório/
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Obtem os pixels da imagem
pixels = imagem.load()

# Ajusta do fator de contraste
fator_contraste = 1.5  # Valor maior que 1 para aumentar o contraste, valor entre 0 e 1 para diminuir o contraste

# Percorra todos os pixels da imagem
largura, altura = imagem.size
for x in range(largura):
    for y in range(altura):
        r, g, b = pixels[x, y]
        r = int((r - 128) * fator_contraste + 128)
        g = int((g - 128) * fator_contraste + 128)
        b = int((b - 128) * fator_contraste + 128)
        r = max(0, min(255, r))  # Certificar se o valor RGB esteja no intervalo válido (0-255)
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        pixels[x, y] = (r, g, b)

# Salve a imagem com o contraste ajustado
imagem.save("imagem_com_contraste.jpg")
