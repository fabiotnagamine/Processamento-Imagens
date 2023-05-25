# Conversão de Imagem para Tons de Cinza

O código a seguir ilustra como converter uma imagem colorida para tons de cinza usando a biblioteca Python PIL (Pillow).

```python
from PIL import Image


def converter_para_tons_de_cinza(imagem):
    """
    Converte uma imagem colorida para tons de cinza.

    Args:
        imagem (str): O caminho para a imagem de entrada.

    Returns:
        None. A imagem convertida é salva como 'imagem_cinza.jpg'.

    """

    # Abre a imagem
    img = Image.open(imagem)

    # Converte para tons de cinza
    img_gray = img.convert('L')

    # Salva a imagem em tons de cinza
    img_gray.save('imagem_cinza.jpg')

    print("Imagem convertida para tons de cinza com sucesso!")


# Chamada da função
converter_para_tons_de_cinza(r'C:\\Users\\nagam\\OneDrive\\Documentos\\Processamento de imagens\\polinesiaFrancesa.png')
```

## Função `converter_para_tons_de_cinza`

Esta função converte uma imagem colorida em tons de cinza. O parâmetro da função é o seguinte:

- `imagem` (str): O caminho para a imagem de entrada que será convertida para tons de cinza.

A função opera da seguinte maneira:

1. A imagem é aberta utilizando o método `Image.open` da biblioteca PIL.
2. Em seguida, a imagem é convertida para tons de cinza utilizando o método `convert('L')`. O resultado é uma nova imagem em tons de cinza.
3. A imagem em tons de cinza é salva como 'imagem_cinza.jpg' utilizando o método `save()`.
4. Uma mensagem é exibida no console indicando que a imagem foi convertida com sucesso.

## Chamada da Função

A função `converter_para_tons_de_cinza` é chamada no exemplo com o caminho da imagem de entrada como argumento. Certifique-se de substituir o caminho da imagem `imagem` pelo caminho correto da imagem que deseja converter para tons de cinza.

```python
converter_para_tons_de_cinza(r'C:\\Users\\nagam\\OneDrive\\Documentos\\Processamento de imagens\\polinesiaFrancesa.png')
```

Após a execução do código, a imagem convertida para tons de cinza será salva como 'imagem_cinza.jpg' no diretório atual.