# Inverter uma Imagem Horizontalmente e Verticalmente utilizando a biblioteca Pillow

Este código em Python utiliza a biblioteca Pillow para inverter uma imagem horizontalmente e verticalmente.

## Inverter Horizontalmente

### Passo 1: Carregar a Imagem

A primeira etapa é carregar a imagem desejada utilizando a função `Image.open()` do módulo `PIL`. Substitua o caminho `/home/fabio/Documentos/computação gráfica/nature.jpg` pelo caminho e nome do arquivo da imagem que você deseja inverter.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```

### Passo 2: Inverter Horizontalmente

Utilizamos o método `transpose()` do objeto Image para inverter a imagem horizontalmente, utilizando a constante `Image.FLIP_LEFT_RIGHT`.

```python
imagem_invertida = imagem.transpose(Image.FLIP_LEFT_RIGHT)
```

### Passo 3: Salvar a Imagem Invertida Horizontalmente

Por fim, salvamos a imagem invertida horizontalmente em um novo arquivo. Substitua "imagem_invertida_horizontal.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem invertida.

```python
imagem_invertida.save("imagem_invertida_horizontal.jpg")
```

## Inverter Verticalmente

### Passo 1: Carregar a Imagem

Carregue a imagem desejada utilizando a função `Image.open()` do módulo `PIL`. Substitua o caminho `/home/fabio/Documentos/computação gráfica/nature.jpg` pelo caminho e nome do arquivo da imagem que você deseja inverter.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```

### Passo 2: Inverter Verticalmente

Utilizamos o método `transpose()` do objeto Image para inverter a imagem verticalmente, utilizando a constante `Image.FLIP_TOP_BOTTOM`.

```python
imagem_invertida = imagem.transpose(Image.FLIP_TOP_BOTTOM)
```

### Passo 3: Salvar a Imagem Invertida Verticalmente

Por fim, salvamos a imagem invertida verticalmente em um novo arquivo. Substitua "imagem_invertida_vertical.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem invertida.

```python
imagem_invertida.save("imagem_invertida_vertical.jpg")
```

Certifique-se de ter a biblioteca Pillow instalada em seu ambiente Python para executar este código. Você pode instalá-la utilizando o comando `pip install pillow`.