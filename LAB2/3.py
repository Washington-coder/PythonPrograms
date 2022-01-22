data = int(input())

ano = data%10000
mes = int(((data%1000000)-ano)/10000)
dia = int(data/1000000)

if(ano<=0 or mes>12 or mes<1 or dia<1 or dia>31):
    print(dia,"de",mes,"de",ano,"nao eh uma data valida")

elif(ano == 1582 and dia>=5 and dia <= 14 and mes == 10):
    print(dia,"de",mes,"de",ano,"nao eh uma data valida")

elif(mes==2):
    if(dia>29):
        print(dia,"de",mes,"de",ano,"nao eh uma data valida")
    elif(ano % 4 == 0 and dia<=29):
        print(dia,"de",mes,"de",ano,"eh uma data valida")
    elif(ano % 4 != 0 and dia == 29):
        print(dia,"de",mes,"de",ano,"nao eh uma data valida")
    else:
        print(dia,"de",mes,"de",ano,"eh uma data valida")

elif(mes == 8 and dia <= 31):
    print(dia,"de",mes,"de",ano,"eh uma data valida")

elif(mes % 2 == 1 and dia <= 31):
    print(dia,"de",mes,"de",ano,"eh uma data valida")
elif(mes % 2 == 0 and dia <= 30):
    print(dia,"de",mes,"de",ano,"eh uma data valida")
else:
    print(dia,"de",mes,"de",ano,"nao eh uma data valida")
