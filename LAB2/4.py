import numpy as np

notas = eval(input())

for i in range(len(notas)):
    if(notas[i] < 2.0):
        notas[i] = 0.0
    elif(notas[i] > 8.0):
        notas[i] = 10

notas = np.array(notas)

print(notas)