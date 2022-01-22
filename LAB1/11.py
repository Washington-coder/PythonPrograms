i = 1
par = 0
impar = 0

while i <= 10:
    numero = int(input())
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    i += 1
    
print(par)
print(impar)
