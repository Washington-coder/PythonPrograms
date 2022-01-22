
def fatorial(N):
    fatorial = 1
    i = 1
    while (i!=N):
        fatorial *= i + 1 
        i += 1
    return fatorial    

N = int(input())

print(fatorial(N))