from PIL import Image

# Carregue a imagem desejada
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")

# Gire a imagem em 90 graus no sentido anti-horário
imagem_rotacionada = imagem.transpose(Image.ROTATE_270)

# Para rotacionar 90 graus ==> ROTATE_90
# Para rotacionar 180 graus ==> ROTATE_180
# Para rotacionar 270 graus ==> ROTATE_270
# Para rotacionar 360 graus ==> ROTATE_360


# Salva a imagem rotacionada
imagem_rotacionada.save("imagem_rotacionada.jpg")
