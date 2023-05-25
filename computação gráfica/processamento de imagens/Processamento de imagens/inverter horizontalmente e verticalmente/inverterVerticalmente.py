from PIL import Image

# Carrega a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Inverte verticalmente
imagem_invertida = imagem.transpose(Image.FLIP_TOP_BOTTOM)

# Salvar a imagem invertida verticalmente
imagem_invertida.save("imagem_invertida_vertical.jpg")
