somaPar = 0
somaImpar = 0
qtdPares = 0
qtdImpares = 0
inputLoop = True

while inputLoop == True:
    Flag = int(input())

    if Flag == 0:
        inputLoop = False
    else:
        if Flag % 2 == 0:
            somaPar += Flag
            qtdPares += 1
        else:
            somaImpar += Flag
            qtdImpares += 1

if qtdPares == 0:
    qtdPares = 1
if qtdImpares == 0:
    qtdImpares = 1
    
print(round((somaPar/qtdPares),2))
print(round((somaImpar/qtdImpares),2))
