# Filtro de Mediana Manual utilizando NumPy e Pillow

Este código em Python utiliza as bibliotecas NumPy e Pillow para aplicar um filtro de mediana em uma imagem.

## Passo 1: Carregar a Imagem

A primeira etapa é carregar a imagem desejada utilizando a função `Image.open()` do módulo `PIL`. Substitua o caminho `/home/fabio/Documentos/computação gráfica/nature.jpg` pelo caminho e nome do arquivo da imagem que você deseja filtrar.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```

## Passo 2: Converter a Imagem para um Array NumPy

Em seguida, convertemos a imagem para um array NumPy usando a função `np.array()`. Isso nos permite manipular os pixels da imagem como uma matriz multidimensional.

```python
imagem_array = np.array(imagem)
```

## Passo 3: Obter as Dimensões da Imagem

Utilizamos a propriedade `shape` do array para obter as dimensões da imagem: altura, largura e número de canais de cor.

```python
altura, largura, canais = imagem_array.shape
```

## Passo 4: Criar uma Matriz Vazia para a Imagem Filtrada

Criamos uma matriz vazia com as mesmas dimensões da imagem original para armazenar a imagem filtrada.

```python
imagem_filtrada = np.zeros_like(imagem_array)
```

## Passo 5: Definir o Tamanho da Janela do Filtro de Mediana

Definimos o tamanho da janela do filtro de mediana. Esse valor determina a vizinhança dos pixels que serão considerados para o cálculo da mediana.

```python
tamanho_janela = 3
```

## Passo 6: Calcular o Deslocamento para o Centro da Janela

Calculamos o deslocamento necessário para posicionar corretamente a janela de filtro no centro dos pixels. Isso é feito dividindo o tamanho da janela por 2.

```python
offset = tamanho_janela // 2
```

## Passo 7: Percorrer os Pixels da Imagem

Utilizamos dois loops `for` para percorrer todos os pixels da imagem. Começamos do `offset` e percorremos até a altura - `offset` e largura - `offset`, para evitar que a janela de filtro ultrapasse as bordas da imagem.

```python
for i in range(offset, altura - offset):
    for j in range(offset, largura - offset):
```

## Passo 8: Extrair a Vizinhança do Pixel Atual

Dentro dos loops, extraímos a vizinhança do pixel atual utilizando as técnicas de indexação do NumPy. Isso nos permite obter uma submatriz correspondente à janela de filtro em torno do pixel.

```python
vizinhanca = imagem_array[i - offset: i + offset + 1, j - offset: j + offset + 1, :]
```

## Passo 9: Calcular a Mediana para Cada Canal de Cor

Para cada canal de cor (R, G, B), calculamos a mediana dos valores dos pixels na vizinhança utilizando a função `np.median()`. A mediana representa o valor central da distribuição dos pixels.

```python
for canal in

 range(canais):
    pixel = vizinhanca[:, :, canal]
    mediana = np.median(pixel)
    imagem_filtrada[i, j, canal] = mediana
```

## Passo 10: Criar uma Nova Imagem a partir do Array Filtrado

Utilizamos a função `Image.fromarray()` do módulo `PIL` para criar uma nova imagem a partir do array NumPy filtrado. É importante converter o tipo de dados para `np.uint8` para garantir que esteja no formato adequado para imagens.

```python
imagem_filtrada = Image.fromarray(imagem_filtrada.astype(np.uint8))
```

## Passo 11: Salvar a Imagem Filtrada

Por fim, salvamos a imagem filtrada em um novo arquivo. Substitua "imagem_filtrada-manual.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem filtrada.

```python
imagem_filtrada.save("imagem_filtrada-manual.jpg")
```

Certifique-se de ter as bibliotecas NumPy e Pillow instaladas em seu ambiente Python para executar este código. Você pode instalá-las usando os comandos `pip install numpy` e `pip install pillow`.