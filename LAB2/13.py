def potencia(b,n):
    if(n != 0):
        aux = b
        b *= b
        n -= 1
        potencia(aux,n)
    return b

b = int(input())
n = int(input())

print(potencia(b,n))