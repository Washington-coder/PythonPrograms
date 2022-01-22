import numpy as np

N = int(input())
M = int(input())

lista = []

for i in range(N):
    lista.append([])
    for j in range(M):
        lista[i].append(0)

b = np.array(lista)

print(b)
