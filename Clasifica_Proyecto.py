class clasifica_proyecto():
    def __init__(self):
        pass
    def clasifica(self,Tipo_proyecto, matriz_proyecto):
        clasificado = []
        for i in range(len(matriz_proyecto)):
            if Tipo_proyecto in matriz_proyecto[i][0]:
                clasificado.append(matriz_proyecto[i][:])
        return clasificado