from PIL import Image


def converter_para_tons_de_cinza(imagem):
    # Abre a imagem
    img = Image.open(imagem)

    # Converte para tons de cinza
    img_gray = img.convert('L')

    # Salva a imagem em tons de cinza
    img_gray.save('imagem_cinza.jpg')

    print("Imagem convertida para tons de cinza com sucesso!")


# Chamada da função
converter_para_tons_de_cinza(r'C:\\Users\\nagam\\OneDrive\\Documentos\\Processamento de imagens\\polinesiaFrancesa.png')
