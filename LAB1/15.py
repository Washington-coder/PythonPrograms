numero = int(input())
i = 0 
soma = 0
x1 = 0
x2 = 1

while(i < numero):
    
    print(x1)
    soma = x1 + x2
    x1 = x2
    x2 = soma
    i += 1
    
    