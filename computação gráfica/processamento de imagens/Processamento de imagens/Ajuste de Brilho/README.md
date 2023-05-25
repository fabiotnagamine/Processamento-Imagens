# Ajuste de Brilho de uma Imagem 

Para essa parte do processamento de imagens podemos fazer o ajuste de brilho de uma imagem, com ajuda da biblioteca Pillow do Python.

## Passo 1: Carregar a imagem

A primeira etapa é carregar a imagem desejada utilizando a função `Image.open()` do Pillow. Substitua o caminho `/home/fabio/Documentos/computação gráfica/nature.jpg` pelo caminho e nome do arquivo da imagem que você deseja ajustar o brilho.

```python
imagem = Image.open("/home/fabio/Documentos/computação gráfica/nature.jpg")
```
## Passo 2: Obter os pixels da imagem
Em seguida, obtemos os pixels da imagem utilizando o método load() do objeto Image. Isso nos permite acessar e modificar os valores de cor de cada pixel.

```python
pixels = imagem.load()
```

## Passo 3: Ajustar o fator de brilho

O próximo passo é ajustar o fator de brilho da imagem. O valor fator_brilho controla a intensidade do brilho. Se for um valor maior que 1, o brilho será aumentado. Se for um valor entre 0 e 1, o brilho será diminuído.

```python
fator_brilho = 1.5
```
Para valores maiores que 1 o brilho vai aumentar, para valores entre 0 e 1 o brilho irá diminuir

## Passo 4: Percorrer os pixels e ajustar o brilho
Agora percorremos todos os pixels da imagem usando dois loops for. Para cada pixel, multiplicamos os valores RGB pelo fator de brilho para ajustar o brilho. Em seguida, atualizamos os valores dos pixels com os novos valores de brilho.

```python
largura, altura = imagem.size
for x in range(largura):
    for y in range(altura):
        r, g, b = pixels[x, y]
        r = int(r * fator_brilho)
        g = int(g * fator_brilho)
        b = int(b * fator_brilho)
        pixels[x, y] = (r, g, b)
```
## Passo 5: Salvar a imagem com o brilho ajustado
Por fim, salvamos a imagem com o brilho ajustado em um novo arquivo. Substitua "caminho/para/imagem_com_brilho.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem com o brilho ajustado.

```python
imagem.save("imagem_com_brilho.jpg")
``` 
Certifique-se de ter a biblioteca Pillow instalada em seu ambiente Python para executar este código. Você pode instalá-la usando o comando `pip install pillow`.