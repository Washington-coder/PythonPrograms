import numpy as np

numeros = eval(input())
lista = np.zeros(37, dtype=int)

for i in range(len(numeros)):
    for j in range(len(lista)):
        if(numeros[i] == j):
            lista[j] += 1

print(lista)