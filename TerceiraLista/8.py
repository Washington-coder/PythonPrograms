inputLoop = True
lista = []

while inputLoop == True:
    num = int(input())
    if num == 0:
        inputLoop = False
    else:
        lista.append(num)

i = (len(lista)-1)

while i >= 0:
    print(lista[i])
    i -= 1

