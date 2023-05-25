# Filtro de Desfoque Gaussiano utilizando o Pillow e NumPy

Este código em Python utiliza as bibliotecas Pillow e NumPy para aplicar um filtro de desfoque gaussiano em uma imagem.

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

## Passo 3: Definir o Kernel do Filtro de Desfoque Gaussiano

O próximo passo é definir o kernel do filtro de desfoque gaussiano. O kernel é uma matriz que descreve a distribuição do desfoque gaussiano. No código, usamos a fórmula do desfoque gaussiano para gerar o kernel.

```python
sigma = 1.0  # Valor do desvio padrão
size = int(2 * np.ceil(3 * sigma) + 1)  # Tamanho do kernel
kernel = np.fromfunction(lambda x, y: (1/(2 * np.pi * sigma**2)) * np.exp(-((x - size//2)**2 + (y - size//2)**2)/(2 * sigma**2)), (size, size))
kernel = kernel / np.sum(kernel)  # Normaliza o kernel para que a soma dos elementos seja igual a 1
```

## Passo 4: Aplicar o Filtro de Desfoque Gaussiano na Imagem

Utilizamos o método `convolve` do módulo `scipy.ndimage` para aplicar o filtro de desfoque gaussiano na imagem. Iteramos sobre os canais de cores (R, G, B) e aplicamos o filtro em cada canal separadamente.

```python
imagem_filtrada_array = np.zeros_like(imagem_array)  # Cria uma matriz de zeros com as mesmas dimensões da imagem
for i in range(3):  # Itera sobre os canais de cores (R, G, B)
    imagem_filtrada_array[:, :, i] = convolve(imagem_array[:, :, i], kernel)
```

## Passo 5: Converter a Matriz de Volta para uma Imagem usando o Pillow

Após aplicar o filtro de desfoque gaussiano, convertemos a matriz resultante de volta para uma imagem utilizando a função `Image.fromarray()`. Garantimos que os valores da matriz estejam no tipo de dados `uint8` antes de converter.

```python
imagem_filtrada = Image.fromarray(imagem_filtrada_array.astype(np.uint8))
```

## Passo 6: Salvar a Imagem Filtrada

Por fim, salvamos a imagem filtrada em um novo arquivo. Substitua "imagem_filtrada-Gauss.jpg" pelo caminho e nome do arquivo no qual você deseja salvar a imagem filtrada.

```python
imagem_filtrada.save("imagem_filtrada-Gauss.jpg")
```

Certifique-se

 de ter as bibliotecas Pillow e NumPy instaladas em seu ambiente Python para executar este código. Você pode instalá-las usando os comandos `pip install pillow` e `pip install numpy`.