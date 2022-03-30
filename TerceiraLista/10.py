inputLoop = True
lista = []

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

for i in range(10):
    num = int(input())
    num = fatorial(num)

    lista.append(num)

for i in range(10):
    print(lista[i])