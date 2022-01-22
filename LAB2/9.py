numeros = eval(input())

maior = numeros[0]

print(len(numeros))
for i in range(len(numeros)):
    print(maior)
    #print(i)
    if(i == len(numeros)):
        print(maior)
    else:
        if(maior > numeros[i+1]):
            maior = numeros[i]
        else:
            maior = numeros[i+1]

