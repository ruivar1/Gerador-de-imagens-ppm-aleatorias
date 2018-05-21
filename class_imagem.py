from class_cor_rgb import CorRGB

class imagem:
    def __init__(self, numero_linhas, numero_culunas):
        self.numero_linhas   = max(numero_linhas,1)
        self.numero_culunas  = max(numero_culunas,1)
        self.grelha=[]
        for x in range(self.numero_linhas):
            self.grelha.append([])
            for y in range(self.numero_culunas):
                self.grelha[x].append(CorRGB(0,0,0))

    def __repr__(self):
        strgrelha = "P3\n"+str(self.numero_linhas) + " "
        strgrelha = strgrelha + str(self.numero_culunas)+"\n"
        strgrelha = strgrelha + "255\n"

        for x in range(self.numero_linhas):
            for y in range(self.numero_culunas):
                strgrelha = strgrelha + str(self.grelha[x][y])+ "  "
            strgrelha = strgrelha + "\n"
        return strgrelha
    
    def set_cor(self, linha, culuna, cor_rgb):
        self.grelha[linha][culuna] = cor_rgb

    def guardar_como_ppm(self, nome_ficheiro):
        img = open(nome_ficheiro, 'w')
        img.write(str(self))
        img.close()
        
