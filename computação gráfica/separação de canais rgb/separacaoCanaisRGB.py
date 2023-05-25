from PIL import Image


def separar_canais(imagem):
    # Abre a imagem
    img = Image.open(imagem)

    # Separa os canais R, G e B
    r, g, b = img.split()

    # Salva os canais separados como imagens individuais
    r.save('canal_r.jpg')
    g.save('canal_g.jpg')
    b.save('canal_b.jpg')

    print("Canais separados com sucesso!")


# Chamada da função
separar_canais('/home/fabio/Documentos/computação gráfica/nature.jpg')
