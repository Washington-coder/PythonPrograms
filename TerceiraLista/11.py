N = int(input())
lista = []

for i in range(N):
    lista.append(int(input()))

maior = lista[0]
menor = lista[0]

for i in range(N):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print(menor, maior)
