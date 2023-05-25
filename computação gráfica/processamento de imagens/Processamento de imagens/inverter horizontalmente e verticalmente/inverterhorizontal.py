from PIL import Image

# Carregue a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Inverter horizontalmente
imagem_invertida = imagem.transpose(Image.FLIP_LEFT_RIGHT)

# Salvar a imagem invertida horizontalmente
imagem_invertida.save("imagem_invertida_horizontal.jpg")
