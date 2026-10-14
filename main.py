import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Image

print(f"OpenCV version: {cv2.__version__}")
#Imagem
#https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg
# %matplotlib inline
# plt.rcParams['figure.figsize'] = (10, 10)

imagem = cv2.imread('lena.jpg')
altura, largura, canais = imagem.shape
print (f"Altura: {altura}, Largura: {largura}, Canais: {canais}")
print(f"Tipo da imagem: {imagem.dtype}")
print(f"Tamanho total em memória: {imagem.nbytes/1024:.2f} KB")

r = imagem[:,:,0] # Canal Vermelho
g = imagem[:,:,1] # Canal Verde
b = imagem[:,:,2] # Canal Azul
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Imagem em tons de cinza
original = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB) # Imagem original em RGB

fig, axs = plt.subplots(1, 5, figsize=(20, 5))
axs[0].imshow(r, cmap='Reds')
axs[0].set_title('Canal Vermelho')
axs[1].imshow(g, cmap='Greens')
axs[1].set_title('Canal Verde')
axs[2].imshow(b, cmap='Blues')
axs[2].set_title('Canal Azul')
axs[3].imshow(cinza, cmap='gray')
axs[3].set_title('Imagem em Tons de Cinza')
axs[4].imshow(original)
axs[4].set_title('Imagem Original')
for ax in axs:
    ax.axis('off')
plt.show()