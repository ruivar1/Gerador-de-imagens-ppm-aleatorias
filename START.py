import  random
from PIL import Image
from class_cor_rgb import CorRGB
from class_imagem import imagem

lado = 16              #pixels

n_cores = 2   #color number 4 >= n_cores >= 1

matriz = []
for x in range(lado):
    linha = []
    for y in range(lado):
        if y <= (lado/2)-1: 
            linha.append(random.randrange(n_cores))
        else:
            linha.append(linha[lado-y-1])
            
    matriz.append(linha)

cor_1 = CorRGB(random.random(),random.random(),random.random())   
cor_2 = CorRGB(random.random(),random.random(),random.random())   
cor_3 = CorRGB(random.random(),random.random(),random.random())   
cor_4 = CorRGB(random.random(),random.random(),random.random())   
imagem_1 = imagem(lado*16,lado*16)


for x in range(lado*16):
    for y in range(lado*16):
        if (matriz[int(x/16)][int(y/16)] == 0): 
            imagem_1.set_cor(x,y,cor_1)             
        elif (matriz[int(x/16)][int(y/16)] == 1):     
            imagem_1.set_cor(x,y,cor_2)             
        elif (matriz[int(x/16)][int(y/16)] == 2):     
            imagem_1.set_cor(x,y,cor_3)             
        elif (matriz[int(x/16)][int(y/16)] == 3):     
            imagem_1.set_cor(x,y,cor_4)             


imagem_1.guardar_como_ppm("perfil_img.ppm")

print("Saved")














        
