import numpy as np
grupos = eval(input())
grupoLength = 0

for i in range(len(grupos)):
    if(grupos[i] % 2 == 1):
        grupoLength += 1

grupo2 = np.zeros(grupoLength, dtype=int)

for i in range(len(grupos)):
    if(grupos[i] % 2 == 1):
    

print(grupo2)
