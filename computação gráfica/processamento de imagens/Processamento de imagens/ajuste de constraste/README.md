## Ajuste de Contraste Manualmente

Este código em Python utiliza a biblioteca Pillow para ajustar manualmente o contraste de uma imagem. O contraste determina a diferença entre os tons claros e escuros em uma imagem, e este código permite aumentar ou diminuir esse contraste de acordo com um fator definido.

## Passo 1: Carregar a Imagem

A primeira etapa é carregar a imagem desejada utilizando a função `Image.open()` do módulo `PIL`. Neste exemplo, a imagem é carregada a partir do diretório `/home/fabio/Documentos/computação gráfica/nature.jpg`. Certifique-se de substituir esse caminho pelo caminho e nome do arquivo da imagem que você deseja ajustar o contraste.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```

## Passo 2: Obter os Pixels da Imagem

Utilizamos o método `load()` do objeto `imagem` para obter os pixels da imagem. Isso nos permite acessar e modificar os valores de cor de cada pixel.

```python
pixels = imagem.load()
```

## Passo 3: Ajustar o Fator de Contraste

Definimos o `fator_contraste`, que determina o quanto o contraste será ajustado. Se o valor for maior que 1, o contraste será aumentado. Se for um valor entre 0 e 1, o contraste será diminuído.

```python
fator_contraste = 1.5

# Valor maior que 1 para aumentar o contraste, valor entre 0 e 1 para diminuir o contraste

```

## Passo 4: Percorrer Todos os Pixels e Ajustar o Contraste

Utilizando dois loops `for`, percorremos todos os pixels da imagem. Para cada pixel, realizamos o ajuste do contraste aplicando a seguinte fórmula para cada componente de cor (vermelho, verde, azul):

```python
r = int((r - 128) * fator_contraste + 128)
g = int((g - 128) * fator_contraste + 128)
b = int((b - 128) * fator_contraste + 128)
```

Nessa fórmula, subtraímos 128 do valor original do componente de cor, multiplicamos pelo fator de contraste e adicionamos 128 novamente. Isso garante que o valor resultante permaneça dentro do intervalo válido de 0 a 255.

## Passo 5: Verificar os Valores de Cor

Após o ajuste do contraste, verificamos se os valores de cor de cada pixel estão dentro do intervalo válido (0-255). Utilizamos as funções `max()` e `min()` para garantir que os valores não ultrapassem esses limites:

```python
r = max(0, min(255, r))
g = max(0, min(255, g))
b = max(0, min(255, b))
```

## Passo 6: Atualizar os Pixels da Imagem

Por fim, atualizamos os valores dos pixels da imagem com os novos valores de cor ajustados:

```python
pixels[x, y] = (r, g, b)
```

## Passo 7: Salvar a Imagem com o Contraste Ajustado

A imagem com o contraste ajustado é salva

 em um novo arquivo utilizando o método `save()` do objeto `imagem`. Substitua "imagem_com_contraste.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem com o contraste ajustado.

```python
imagem.save("imagem_com_contraste.jpg")
```

Certifique-se de ter a biblioteca Pillow instalada em seu ambiente Python para executar este código. Você pode instalá-la usando o comando `pip install pillow`.