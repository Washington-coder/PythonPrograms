# m = eval(input("Matriz: "))

# if(len(m) == len(m[0])):
#     for i in range(len(m)):
#         for j in range(len(m[0])):
#             if((len(m)-1) == i + j):
#                 print(m[i][j])
# else:
#     print("A matriz nao eh quadratica")

# notas = eval(input())
# medias = []
# soma = 0


# for i in range(len(notas)):
#     medias.append((sum(notas[i])/len(notas[0])))

# print(medias)

# print("Maior: ", max(medias))
# print("Menor: ", min(medias))

# matrizExibir = [[" " , " " , " " , "|" , " " , " " , " " , "|" , " " , " " , " "],
#                 ["-" , "-" , "-" , "+" , "-" , "-" , "-" , "+" , " " , " " , " "],
#                 [" " , " " , " " , "|" , " " , " " , " " , "|" , " " , " " , " "],
#                 ["-" , "-" , "-" , "+" , "-" , "-" , "-" , "+" , " " , " " , " "],
#                 [" " , " " , " " , "|" , " " , " " , " " , "|" , " " , " " , " "]]

# print(matrizExibir)

# import numpy as np

# a = np.array([[1,2,3],[3,4,5],[7,8,9]])

# for line in a:
#     print ('  '.join(map(str, line)))

# notas = [["   |   |   "],
#          ["---+---+---"],
#          ["   |   |   "],
#          ["---+---+---"],
#          ["   |   |   "]]

# for i in range(len(notas)):
#     for j in range(len(notas[0])):
#         print(notas[i][j], end = " ")
#     print("")

# s = "Naze"
# l = list(s)
# l[2] = 'm'
# s = "".join(l)
# print(s)

linha0 = "   |   |   "
linha1 = "   |   |   "
linha2 = "   |   |   "

rodada = 1

while(1):
    if (rodada == 1):
        linhaX = int(input("Linha de X: "))
        colunaX = int(input("Coluna de X: "))

        if(linhaX == 0):
            if(colunaX == 0):
                l = list(linha0)
                l[1] = 'X'
                linha0 = "".join(l)
            elif(colunaX == 1):
                l = list(linha0)
                l[5] = 'X'
                linha0 = "".join(l)
            elif(colunaX == 2):
                l = list(linha0)
                l[9] = 'X'
                linha0 = "".join(l)
            
        if(linhaX == 1):          
            if(colunaX == 0):
                l = list(linha1)
                l[1] = 'X'
                linha1 = "".join(l)
            elif(colunaX == 1):
                l = list(linha1)
                l[5] = 'X'
                linha1 = "".join(l)
            elif(colunaX == 2):
                l = list(linha1)
                l[9] = 'X'
                linha1 = "".join(l)
            
        if(linhaX == 2):          
            if(colunaX == 0):
                l = list(linha2)
                l[1] = 'X'
                linha2 = "".join(l)
            elif(colunaX == 1):
                l = list(linha2)
                l[5] = 'X'
                linha2 = "".join(l)
            elif(colunaX == 2):
                l = list(linha2)
                l[9] = 'X'
                linha2 = "".join(l)
            
        print(linha0)
        print("---+---+---")
        print(linha1)
        print("---+---+---")
        print(linha2)

        print()
        
    else:
        linhaO = int(input("Linha de O: "))
        colunaO = int(input("Coluna de O: "))

        if(linhaO == 0):
            if(colunaO == 0):
                l = list(linha0)
                l[1] = 'O'
                linha0 = "".join(l)
            elif(colunaO == 1):
                l = list(linha0)
                l[5] = 'O'
                linha0 = "".join(l)
            elif(colunaO == 2):
                l = list(linha0)
                l[9] = 'O'
                linha0 = "".join(l)
            
        if(linhaO == 1):          
            if(colunaO == 0):
                l = list(linha1)
                l[1] = 'O'
                linha1 = "".join(l)
            elif(colunaO == 1):
                l = list(linha1)
                l[5] = 'O'
                linha1 = "".join(l)
            elif(colunaO == 2):
                l = list(linha1)
                l[9] = 'O'
                linha1 = "".join(l)
            
        if(linhaO == 2):          
            if(colunaO == 0):
                l = list(linha2)
                l[1] = 'O'
                linha2 = "".join(l)
            elif(colunaO == 1):
                l = list(linha2)
                l[5] = 'O'
                linha2 = "".join(l)
            elif(colunaO == 2):
                l = list(linha2)
                l[9] = 'O'
                linha2 = "".join(l)
            
        print(linha0)
        print("---+---+---")
        print(linha1)
        print("---+---+---")
        print(linha2)

        print()
        
    rodada *= -1