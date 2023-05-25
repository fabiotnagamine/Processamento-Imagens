# Rotação de Imagem utilizando a biblioteca Pillow

Este código em Python utiliza a biblioteca Pillow para realizar a rotação de uma imagem.

## Passo 1: Carregar a Imagem

A primeira etapa é carregar a imagem desejada utilizando a função `Image.open()` do módulo `PIL`. Substitua o caminho `/home/fabio/Documentos/computação gráfica/nature.jpg` pelo caminho e nome do arquivo da imagem que você deseja rotacionar.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```

## Passo 2: Rotacionar a Imagem

Utilizamos o método `transpose()` do objeto Image para realizar a rotação da imagem. No exemplo fornecido, a imagem é rotacionada em 90 graus no sentido anti-horário, utilizando a constante `Image.ROTATE_270`.

```python
imagem_rotacionada = imagem.transpose(Image.ROTATE_270)
```

Outras opções para a rotação são:

- Para rotacionar 90 graus no sentido horário: `Image.ROTATE_90`
- Para rotacionar 180 graus: `Image.ROTATE_180`
- Para rotacionar 270 graus no sentido horário: `Image.ROTATE_270`
- Para rotacionar 360 graus (sem alteração): `Image.ROTATE_360`

## Passo 3: Salvar a Imagem Rotacionada

Por fim, salvamos a imagem rotacionada em um novo arquivo. Substitua "imagem_rotacionada.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem rotacionada.

```python
imagem_rotacionada.save("imagem_rotacionada.jpg")
```

Certifique-se de ter a biblioteca Pillow instalada em seu ambiente Python para executar este código. Você pode instalá-la utilizando o comando `pip install pillow`.