from PIL import Image, ImageFilter

def apply_average_filter(image_path, radius):
    # Abrir a imagem
    img = Image.open(image_path)

    # Aplicar o filtro de média
    filtered_img = img.filter(ImageFilter.BoxBlur(radius))

    # Salvar a imagem resultante
    output_path = 'output.png'
    filtered_img.save(output_path)
    print(f"A imagem com o filtro de média foi salva em {output_path}.")

# Exemplo de uso
image_path = '/home/fabio/Documentos/computação gráfica/processamento de imagens/Processamento de imagens/polinesiaFrancesa.png'
radius = 80  # Raio do filtro de média
apply_average_filter(image_path, radius)
