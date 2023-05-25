## Separação de Canais de uma Imagem

O código a seguir demonstra como separar os canais de cor de uma imagem RGB (vermelho, verde e azul) em imagens individuais usando a biblioteca Python PIL (Pillow).

```python
from PIL import Image


def separar_canais(imagem):
    """
    Separa os canais de cor de uma imagem RGB em imagens individuais.

    Args:
        imagem (str): O caminho para a imagem de entrada.

    Returns:
        None. Os canais separados são salvos como imagens individuais.

    """

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
separar_canais(r'C:\\Users\\nagam\\OneDrive\\Documentos\\Processamento de imagens\\polinesiaFrancesa.png')
```

### Função `separar_canais`

Esta função separa os canais de cor de uma imagem RGB em imagens individuais. O parâmetro da função é o seguinte:

- `imagem` (str): O caminho para a imagem de entrada que terá seus canais separados.

A função opera da seguinte maneira:

1. A imagem é aberta utilizando o método `Image.open` da biblioteca PIL.
2. Em seguida, os canais de cor R, G e B são separados utilizando o método `split()` do objeto de imagem. Cada canal é armazenado em uma variável separada.
3. Cada canal separado é salvo como uma imagem individual usando o método `save()`. Os canais R, G e B são salvos como 'canal_r.jpg', 'canal_g.jpg' e 'canal_b.jpg', respectivamente.
4. Uma mensagem é exibida no console indicando que os canais foram separados com sucesso.

### Chamada da Função

A função `separar_canais` é chamada no exemplo com o caminho da imagem de entrada como argumento. Certifique-se de substituir o caminho da imagem `imagem` pelo caminho correto da imagem que deseja separar os canais.

```python
separar_canais(r'C:\\Users\\nagam\\OneDrive\\Documentos\\Processamento de imagens\\polinesiaFrancesa.png')
```

Após a execução do código, os canais separados serão salvos como imagens individuais com os nomes 'canal_r.jpg', 'canal_g.jpg' e 'canal_b.jpg' no diretório atual.