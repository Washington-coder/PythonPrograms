
def SomaLista(lista):
    soma = 0
    if(len(lista) == 0):
        print("Lista vazia")
    for i in lista:
        soma += i
    return soma

lista = eval(input())

print(SomaLista(lista))