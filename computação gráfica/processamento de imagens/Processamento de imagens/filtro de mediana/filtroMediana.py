from PIL import Image
from PIL import ImageFilter
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
imagem_filtrada = imagem.filter(ImageFilter.MedianFilter(size=3))
imagem_filtrada.save("imagem_filtrada.jpg")

