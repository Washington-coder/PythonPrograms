inputLoop = True
lista = []

def tamanhoLista(lista):
    contador = 0
    for i in lista:
        contador += 1
    
    return contador

num = 1 
while num != -1:
    num = int(input())
    lista.append(num)

listaRepetidos = []

for i in range(tamanhoLista(lista)):
    for j in range(i+1, tamanhoLista(lista)):
        if lista[i] == lista[j]:
            if listaRepetidos == []:
                listaRepetidos.append(lista[i])
            else:    
                contador = 0
                for c in range(tamanhoLista(listaRepetidos)):
                    if lista[i] != listaRepetidos[c]:
                        contador += 1
                if contador == tamanhoLista(listaRepetidos):
                    listaRepetidos.append(lista[i])

print(listaRepetidos)
