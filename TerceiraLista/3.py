N = int(input())
lista = [1]
numAtual = 1
diferenca = 2

for i in range(N-1):
    numAtual += diferenca
    diferenca += 1
    lista.append(numAtual)

print(lista)
