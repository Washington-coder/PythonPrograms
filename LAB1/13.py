numero = int(input())
i = 1
fatorial = 1

if(numero > 0):
    while i <= numero:
        fatorial *= i
        i += 1
    print("Fatorial de",numero,"eh",fatorial)
    
elif(numero < 0):
    print("Numero Negativo")
    
else:
    print("Fatorial de 0 eh 1")
