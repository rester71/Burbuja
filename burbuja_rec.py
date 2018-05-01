class Burbuja(object):
    lista = None
    tam_lista = 0
    def __init__(self, lista):
        self.lista = lista
        self.tam_lista = len(lista)

    def ordenar(self,tam_lista):
        if tam_lista >= self.tam_lista:
            return self.lista
        else:
            for j in range(self.tam_lista-1):
                if self.lista[j] > self.lista[j+1]:
                    Ordenado = False
                    tmp = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = tmp
                    #print("Lista",self.lista)
            return self.ordenar(tam_lista+1)
