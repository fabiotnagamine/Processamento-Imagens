from PIL import Image

def convert_to_black_and_white(image_path, threshold):
    # Abrir a imagem em tons de cinza
    img = Image.open(image_path).convert('L')

    # Obter os pixels da imagem
    pixels = img.load()

    # Converter pixels para preto e branco usando o limiar
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixels[x, y] < threshold:
                pixels[x, y] = 0  # Preto
            else:
                pixels[x, y] = 255  # Branco

    # Salvar a imagem resultante
    output_path = 'output.png'
    img.save(output_path)
    print(f"A imagem em preto e branco foi salva em {output_path}.")

# Exemplo de uso
image_path = '/home/fabio/Documentos/computação gráfica/Processamento de placas/Computação_grafica_reconhecimento_placa/imagens/R.png'
threshold = 128  # Limiar para a binarização
convert_to_black_and_white(image_path, threshold)
