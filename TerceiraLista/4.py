N = int(input())
soma = 1
divisor = 1

for i in range(N-1):
    divisor += 1
    soma = soma + (1/divisor)

print(soma)