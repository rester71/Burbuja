from burbuja import Burbuja

def main():
    Lista = [9,8,7,6,5,4]
    burbuja = Burbuja(Lista)
    print("Arreglo desordenado\t", Lista)
    Lista_ordenada = burbuja.ordenar()
    print("Arreglo ordenado\t",Lista_ordenada)

if __name__ == main():
    main()
