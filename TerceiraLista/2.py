N = int(input())
lista = []

for i in range(N):
    lista.append(int(input()))

for i in range(N):
    for j in range(N):
        if(lista[i] < lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)
