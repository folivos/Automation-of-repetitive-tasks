class Ordena_informe():
    def __init__(self):
        pass
    def vector(self,aux1, aux2):
        self.aux_vector = []
        for j in range(len(aux2) - 1):
            if aux2[j] != aux2[j + 1]:
                self.aux_vector.append(aux1[j])
                if j + 1 == len(aux2) - 1 and aux2[j + 1] != aux2[len(aux2) - 1]:
                    self.aux_vector.append(aux1[len(aux1) - 1])
            if j + 1 == len(aux2) - 1 and aux2[j + 1] == aux2[len(aux2) - 1]:
                self.aux_vector.append(aux1[len(aux1) - 1])
        return self.aux_vector


    def vectores(self, proyectos, areas, datos):
        return self.vector(proyectos, proyectos), self.vector(areas, areas), self.vector(datos, areas)