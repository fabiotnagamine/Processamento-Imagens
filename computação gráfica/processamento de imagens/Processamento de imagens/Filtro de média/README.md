# Documentação - Aplicação do Filtro da Mediana em uma Imagem

O trecho de código fornecido demonstra como aplicar o filtro da mediana em uma imagem usando Python. Ele utiliza a função `median_filter` do módulo `scipy.ndimage`, a biblioteca `PIL` para processamento de imagens e a biblioteca `numpy` para manipulação de arrays.

## Função: `apply_median_filter(image_path, size)`

Esta função aplica o filtro da mediana em uma imagem, dada a localização do arquivo da imagem e o tamanho da janela do filtro.

### Argumentos

- `image_path` (str): O caminho para o arquivo de imagem de entrada.
- `size` (int ou tuple): O tamanho da janela do filtro da mediana. Pode ser um número inteiro representando uma janela quadrada ou uma tupla de dois inteiros representando um tamanho de janela retangular (largura, altura).

### Retorna

Nenhum. A imagem filtrada é salva em disco.

### Passos

1. Abrir a imagem usando `Image.open(image_path)` da biblioteca `PIL`.
2. Converter a imagem para tons de cinza usando o método `convert('L')`. Isso garante que a imagem tenha um único canal (tons de cinza) para a operação do filtro da mediana.
3. Converter a imagem em tons de cinza para um array NumPy usando `np.array(img)`. Isso permite aplicar o filtro da mediana usando a função `median_filter` do módulo `scipy.ndimage`.
4. Aplicar o filtro da mediana ao array da imagem usando `median_filter(img_array, size=size)`. Isso substitui o valor de cada pixel pela mediana dos valores dos pixels na vizinhança definida pelo tamanho da janela do filtro.
5. Converter o array filtrado de volta para uma imagem usando `Image.fromarray(filtered_array)`.
6. Salvar a imagem resultante em disco usando o método `save` do objeto `Image`, especificando o caminho do arquivo de saída.
7. Imprimir uma mensagem de confirmação indicando que a imagem com o filtro da mediana aplicado foi salva.

## Exemplo de Uso

O código também inclui um exemplo de uso que demonstra como chamar a função `apply_median_filter`.

1. Definir a variável `image_path`, especificando o caminho para o arquivo de imagem de entrada desejado.
2. Definir a variável `filter_size`, indicando o tamanho da janela do filtro da mediana (por exemplo, 3 representa uma janela 3x3).
3. Chamar a função `apply_median_filter` com os argumentos `image_path` e `filter_size`.

Certifique-se de substituir `'image.jpg'` pelo caminho para o arquivo de imagem de entrada desejado. A imagem resultante com o filtro da mediana aplicado será salva como `'output.png'`.