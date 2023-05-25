# Conversão de Imagem para Preto e Branco

O código a seguir demonstra como converter uma imagem colorida em uma imagem em preto e branco usando um limiar especificado. A conversão é realizada utilizando a biblioteca Python PIL (Pillow).

```python
from PIL import Image

def convert_to_black_and_white(image_path, threshold):
    """
    Converte uma imagem colorida para preto e branco usando um limiar especificado.

    Args:
        image_path (str): O caminho para a imagem de entrada.
        threshold (int): O valor do limiar para a binarização. Pixels abaixo do limiar serão convertidos para preto,
                         e pixels acima ou igual ao limiar serão convertidos para branco.

    Returns:
        None. A imagem resultante é salva em disco.

    """

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
image_path = '/home/fabio/Documentos/computação gráfica/processamento de imagens/Processamento de imagens/polinesiaFrancesa.png'
threshold = 128  # Limiar para a binarização
convert_to_black_and_white(image_path, threshold)
```

## Função `convert_to_black_and_white`

Esta função converte uma imagem colorida para uma imagem em preto e branco, utilizando um limiar especificado para a binarização. Os parâmetros da função são os seguintes:

- `image_path` (str): O caminho para a imagem de entrada que será convertida.
- `threshold` (int): O valor do limiar para a binarização. Pixels abaixo do limiar serão convertidos para preto (valor 0),
  e pixels acima ou igual ao limiar serão convertidos para branco (valor 255).

A função opera da seguinte maneira:

1. A imagem é aberta utilizando o método `Image.open` da biblioteca PIL e em seguida é convertida para tons de cinza usando o método `convert('L')`. Isso resulta em uma imagem em escala de cinza.
2. Os pixels da imagem são obtidos através do objeto `load()` da imagem.
3. Em seguida, é realizado um loop pelos pixels da imagem. Para cada pixel, se o valor for menor que o limiar especificado, o pixel é convertido para preto (valor 0). Caso contrário, o pixel é convertido para branco (valor 255).
4. A imagem resultante é salva no disco usando o método `save`. O caminho de saída é definido como 'output.png'.
5. Uma mensagem é exibida no console indicando o caminho onde a imagem foi salva.

## Exemplo de Uso

Um exemplo de uso da função é fornecido no código abaixo:

```python
image_path = '/home/fabio/Documentos/computação

 gráfica/processamento de imagens/Processamento de imagens/polinesiaFrancesa.png'
threshold = 128  # Limiar para a binarização
convert_to_black_and_white(image_path, threshold)
```

Neste exemplo, é fornecido o caminho para a imagem de entrada e um limiar de 128. A função `convert_to_black_and_white` é chamada com esses argumentos, resultando na conversão da imagem para preto e branco. A imagem resultante é salva no disco com o nome 'output.png'.

Certifique-se de substituir o caminho da imagem `image_path` pelo caminho correto da imagem que deseja converter.