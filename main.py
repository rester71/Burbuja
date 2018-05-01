from burbuja import Burbuja
from burbuja_rec import Burbuja as br
import mergesort
import random
import time

def main():
    start_time = time.time()
    Lista = []
    Lista.extend(range(10000,-1,-1))
    #burbuja = Burbuja(Lista)
    #burbuja_rec = br(Lista)

    print("Arreglo desordenado\t", Lista)
    Lista_ordenada = mergesort.mergesort(Lista)
    #Lista_ordenada = burbuja.ordenar()
    #Lista_ordenada = burbuja_rec.ordenar(0)
    print("Arreglo ordenado\t",Lista_ordenada)
    print("--- %s seconds ---" % round(time.time() - start_time, 2))

if __name__ == main():
    main()
