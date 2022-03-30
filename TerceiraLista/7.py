inputLoop = True
somaTotal = 0

while inputLoop:
    num = int(input())
    if num == -1:
        inputLoop = False
    else:
        somaTotal += num

print("Soma Total: "+str(somaTotal))