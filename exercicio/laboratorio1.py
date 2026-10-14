from pathlib import Path
import os

import cv2
import matplotlib.pyplot as plt


os.chdir(Path(__file__).resolve().parent)
imagem = cv2.imread("megan_fox.png")

if imagem is None:
    raise FileNotFoundError("Não foi possível carregar a imagem 'megan_fox.png'.")

print(imagem.shape)
altura, largura, canais = imagem.shape

lado = min(200, altura, largura)
y_inicial = (altura - lado) // 2
x_inicial = (largura - lado) // 2
recorte = imagem[y_inicial : y_inicial + lado, x_inicial : x_inicial + lado].copy()

recorte[:, :, 1] = 0
recorte[:, :, 2] = 0

if not cv2.imwrite("resultado_roi.png", recorte):
    raise OSError("Não foi possível salvar 'resultado_roi.png'.")

imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
recorte_rgb = cv2.cvtColor(recorte, cv2.COLOR_BGR2RGB)

fig, eixos = plt.subplots(1, 2, figsize=(10, 5))
eixos[0].imshow(imagem_rgb)
eixos[0].set_title("Imagem Original")
eixos[1].imshow(recorte_rgb)
eixos[1].set_title("ROI Azul")

for eixo in eixos:
    eixo.axis("off")

plt.tight_layout()
plt.show()
