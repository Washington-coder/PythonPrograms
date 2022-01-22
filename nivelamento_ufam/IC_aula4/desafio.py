
matrizBase = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

linha0 = "   |   |   "
linha1 = "   |   |   "
linha2 = "   |   |   "

fim = 1
rodada = 1
empate = 0
segundaTentativa = 0

print()
print("########## O JOGO DA VELHA ##########")
print()
print(linha0)
print("---+---+---")
print(linha1)
print("---+---+---")
print(linha2)

print()

while(fim == 1):
    if(rodada == 1):
        
        #---------------------------JOGO DO 'X'---------------------------#
        print("------------- Vez do jogador X -------------")
        print()
        linhaX = int(input("Informe a linha de X: "))
        #VERIFICANDO SE A LINHA ESTA DENTRO DO INTERVALO
        if(linhaX > 2 or linhaX < 0):
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print()
                print("Coordenada invalida ! Digite um valor entre 0 e 2")
                print()
                print("------------- Vez do jogador X -------------")
                print()
                linhaX = int(input("Informe novamente a linha de X: "))
                if(linhaX >= 0 and linhaX <= 2):
                    segundaTentativa = 0
                
        colunaX = int(input("Informe a coluna de X: "))
        #VERIFICANDO SE A COLUNA ESTA DENTRO DO INTERVALO
        if(colunaX > 2 or colunaX < 0):
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print()
                print("Coordenada invalida ! Digite um valor entre 0 e 2")
                print()
                print("------------- Vez do jogador X -------------")
                print()
                colunaX = int(input("Informe novamente a coluna de X: "))
                if(colunaX >= 0 and colunaX <= 2):
                    segundaTentativa = 0
                  
        #---------------OBTENDO AS COORDENADAS PARA PODER EXIBIR---------------#
        if(matrizBase[linhaX][colunaX] == 0):
            if(linhaX == 0 and colunaX == 0):          
                l = list(linha0)
                l[1] = 'X'
                linha0 = "".join(l)
                
            elif(linhaX == 0 and colunaX == 1):          
                l = list(linha0)
                l[5] = 'X'
                linha0 = "".join(l)
                
            elif(linhaX == 0 and colunaX == 2):          
                l = list(linha0)
                l[9] = 'X'
                linha0 = "".join(l)
                
            elif(linhaX == 1 and colunaX == 0):          
                l = list(linha1)
                l[1] = 'X'
                linha1 = "".join(l)
                
            elif(linhaX == 1 and colunaX == 1):          
                l = list(linha1)
                l[5] = 'X'
                linha1 = "".join(l)
                
            elif(linhaX == 1 and colunaX == 2):          
                l = list(linha1)
                l[9] = 'X'
                linha1 = "".join(l)
                
            elif(linhaX == 2 and colunaX == 0):          
                l = list(linha2)
                l[1] = 'X'
                linha2 = "".join(l)
                
            elif(linhaX == 2 and colunaX == 1):          
                l = list(linha2)
                l[5] = 'X'
                linha2 = "".join(l)
                
            elif(linhaX == 2 and colunaX == 2):          
                l = list(linha2)
                l[9] = 'X'
                linha2 = "".join(l)
            
        
        print()
        
        if(matrizBase[linhaX][colunaX] == 0):
            matrizBase[linhaX][colunaX] = 1
            
            #-------VALIDACOES DE VITORIA-------#
            
            #CONDIÇÃO PARA GANHAR NO EIXO X 
            for i in range(len(matrizBase)):
                if(matrizBase[i][0] == 1 and matrizBase[i][1] == 1 and matrizBase[i][2] == 1):
                    print("------------- O jogador X ganhou -------------")
                    print()
                    fim = 0
            
            #CONDIÇÃO PARA GANHAR NO EIXO Y
            for j in range(len(matrizBase)):
                if(matrizBase[0][j] == 1 and matrizBase[1][j] == 1 and matrizBase[2][j] == 1):
                    print("------------- O jogador X ganhou -------------")
                    print()
                    fim = 0
                    
            #CONDIÇÃO PARA GANHAR NA DIAGONAL PRINCIPAL
            if(matrizBase[0][0] == 1 and matrizBase[1][1] == 1 and matrizBase[2][2] == 1):
                print("------------- O jogador X ganhou -------------")
                print()
                fim = 0
                
            #CONDIÇÃO PARA GANHAR NA DIAGONAL SECUNDARIA
            if(matrizBase[0][2] == 1 and matrizBase[1][1] == 1 and matrizBase[2][0] == 1):
                print("------------- O jogador X ganhou -------------")
                print()
                fim = 0           
            
            #CONDICAO DE EMPATE
            empate += 1
            if(empate == 9):
                print("########## O jogo empatou ! ##########")
                print()
                fim = 0
                
        #VERIFICA SE A POSICAO ESTA OCUPADA
        elif(matrizBase[linhaX][colunaX] == 1 or matrizBase[linhaX][colunaX] == 2):
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print("Esta posicao esta ocupada !")
                print()
                print("########## Vez do jogador X ##########")
                print()
                linhaX = int(input("Informe novamente a linha de X: "))
                if(linhaX > 2 or linhaX < 0):
                    segundaTentativa = 1
                    while(segundaTentativa == 1):
                        print()
                        print("Coordenada invalida ! Digite um valor entre 0 e 2")
                        print()
                        print("------------- Vez do jogador X -------------")
                        print()
                        linhaX = int(input("Informe novamente a linha de X: "))
                        if(linhaX >= 0 and linhaX <= 2):
                            segundaTentativa = 0
                colunaX = int(input("Informe novamente a coluna de X: "))
                if(colunaX > 2 or colunaX < 0):
                    segundaTentativa = 1
                    while(segundaTentativa == 1):
                        print()
                        print("Coordenada invalida ! Digite um valor entre 0 e 2")
                        print()
                        print("------------- Vez do jogador X -------------")
                        print()
                        colunaX = int(input("Informe novamente a coluna de X: "))
                        if(colunaX >= 0 and colunaX <= 2):
                            segundaTentativa = 0
                print()
                if(matrizBase[linhaX][colunaX] == 0):
                    matrizBase[linhaX][colunaX] = 1
                    #---------------OBTENDO AS COORDENADAS PARA PODER EXIBIR---------------#

                    if(linhaX == 0 and colunaX == 0):          
                        l = list(linha0)
                        l[1] = 'X'
                        linha0 = "".join(l)
                        
                    elif(linhaX == 0 and colunaX == 1):          
                        l = list(linha0)
                        l[5] = 'X'
                        linha0 = "".join(l)
                        
                    elif(linhaX == 0 and colunaX == 2):          
                        l = list(linha0)
                        l[9] = 'X'
                        linha0 = "".join(l)
                        
                    elif(linhaX == 1 and colunaX == 0):          
                        l = list(linha1)
                        l[1] = 'X'
                        linha1 = "".join(l)
                        
                    elif(linhaX == 1 and colunaX == 1):          
                        l = list(linha1)
                        l[5] = 'X'
                        linha1 = "".join(l)
                        
                    elif(linhaX == 1 and colunaX == 2):          
                        l = list(linha1)
                        l[9] = 'X'
                        linha1 = "".join(l)
                        
                    elif(linhaX == 2 and colunaX == 0):          
                        l = list(linha2)
                        l[1] = 'X'
                        linha2 = "".join(l)
                        
                    elif(linhaX == 2 and colunaX == 1):          
                        l = list(linha2)
                        l[5] = 'X'
                        linha2 = "".join(l)
                        
                    elif(linhaX == 2 and colunaX == 2):          
                        l = list(linha2)
                        l[9] = 'X'
                        linha2 = "".join(l)
                    
                    print()
                    
                    #-------VALIDACOES DE VITORIA-------#
                    
                    #CONDIÇÃO PARA GANHAR NO EIXO X 'X'
                    for i in range(len(matrizBase)):
                        if(matrizBase[i][0] == 1 and matrizBase[i][1] == 1 and matrizBase[i][2] == 1):
                            print("########## O jogador X ganhou ##########")
                            print()
                            fim = 0
                    
                    #CONDIÇÃO PARA GANHAR NO EIXO Y 'X'
                    for j in range(len(matrizBase)):
                        if(matrizBase[0][j] == 1 and matrizBase[1][j] == 1 and matrizBase[2][j] == 1):
                            print("########## O jogador X ganhou ##########")
                            print()
                            fim = 0
                            
                    #CONDIÇÃO PARA GANHAR NA DIAGONAL PRINCIPAL 'X'
                    if(matrizBase[0][0] == 1 and matrizBase[1][1] == 1 and matrizBase[2][2] == 1):
                        print("########## O jogador X ganhou ##########")
                        print()
                        fim = 0
                        
                    #CONDIÇÃO PARA GANHAR NA DIAGONAL SECUNDARIA 'X'
                    if(matrizBase[0][2] == 1 and matrizBase[1][1] == 1 and matrizBase[2][0] == 1):
                        print("########## O jogador X ganhou ##########")
                        print()
                        fim = 0           
                    
                    #CONDICAO DE EMPATE
                    empate += 1
                    if(empate == 9):
                        print("########## O jogo empatou ##########")
                        print()
                        fim = 0
                    
                    segundaTentativa = 0
        
        print()
        print("########## O JOGO DA VELHA ##########")
        print()
        print(linha0)
        print("---+---+---")
        print(linha1)
        print("---+---+---")
        print(linha2)

        print()
        
    else:
        
        #---------------------------JOGO DO 'O'---------------------------#
        print("-------- Vez do jogador 'O' --------")
        print()
        linhaO = int(input("Informe a linha de O: "))
        #VERIFICANDO SE A LINHA ESTA DENTRO DO INTERVALO
        if(linhaO > 2 or linhaO < 0):
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print()
                print("Coordenada invalida ! Digite um valor entre 0 e 2")
                print()
                print("-------- Vez do jogador 'O' --------")
                print()
                linhaO = int(input("Informe novamente a linha de O: "))
                if(linhaO >= 0 and linhaO <= 2):
                    segundaTentativa = 0
                    
        colunaO = int(input("Informe a coluna de O: "))
        #VERIFICANDO SE A COLUNA ESTA DENTRO DO INTERVALO
        if(colunaO > 2 or colunaO < 0):
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print()
                print("Coordenada invalida ! Digite um valor entre 0 e 2")
                print()
                print("-------- Vez do jogador 'O' --------")
                print()
                colunaO = int(input("Informe novamente a coluna de X: "))
                if(colunaO >= 0 and colunaO <= 2):
                    segundaTentativa = 0
                    
        #---------------OBTENDO AS COORDENADAS PARA PODER EXIBIR---------------#
        if(matrizBase[linhaO][colunaO] == 0):
            if(linhaO == 0 and colunaO == 0):          
                l = list(linha0)
                l[1] = 'O'
                linha0 = "".join(l)
                
            if(linhaO == 0 and colunaO == 1):          
                l = list(linha0)
                l[5] = 'O'
                linha0 = "".join(l)
                
            if(linhaO == 0 and colunaO == 2):          
                l = list(linha0)
                l[9] = 'O'
                linha0 = "".join(l)
                
            if(linhaO == 1 and colunaO == 0):          
                l = list(linha1)
                l[1] = 'O'
                linha1 = "".join(l)
                
            if(linhaO == 1 and colunaO == 1):          
                l = list(linha1)
                l[5] = 'O'
                linha1 = "".join(l)
                
            if(linhaO == 1 and colunaO == 2):          
                l = list(linha1)
                l[9] = 'O'
                linha1 = "".join(l)
                
            if(linhaO == 2 and colunaO == 0):          
                l = list(linha2)
                l[1] = 'O'
                linha2 = "".join(l)
                
            if(linhaO == 2 and colunaO == 1):          
                l = list(linha2)
                l[5] = 'O'
                linha2 = "".join(l)
                
            if(linhaO == 2 and colunaO == 2):          
                l = list(linha2)
                l[9] = 'O'
                linha2 = "".join(l)
        
        
        print()
        
        if(matrizBase[linhaO][colunaO] == 0):
            matrizBase[linhaO][colunaO] = 2
            
            #-------VALIDACOES DE VITORIA-------#
            
            #CONDIÇÃO PARA GANHAR NO EIXO X
            for i in range(len(matrizBase)):
                if(matrizBase[i][0] == 2 and matrizBase[i][1] == 2 and matrizBase[i][2] == 2):
                    print("------------- O jogador 'O' ganhou -------------")
                    print()
                    fim = 0
            
            #CONDIÇÃO PARA GANHAR NO EIXO Y
            for j in range(len(matrizBase)):
                if(matrizBase[0][j] == 2 and matrizBase[1][j] == 2 and matrizBase[2][j] == 2):
                    print("------------- O jogador 'O' ganhou -------------")
                    print()
                    fim = 0
                    
            #CONDIÇÃO PARA GANHAR NA DIAGONAL PRINCIPAL
            if(matrizBase[0][0] == 2 and matrizBase[1][1] == 2 and matrizBase[2][2] == 2):
                print("------------- O jogador 'O' ganhou -------------")
                print()
                fim = 0
                
            #CONDIÇÃO PARA GANHAR NA DIAGONAL SECUNDARIA
            if(matrizBase[0][2] == 2 and matrizBase[1][1] == 2 and matrizBase[2][0] == 2):
                print("------------- O jogador 'O' ganhou -------------")
                print()
                fim = 0           
            
            #CONDICAO DE EMPATE
            empate += 1
            if(empate == 9):
                print("------------- O jogo empatou -------------")
                print()
                fim = 0
        
        #VERIFICA SE A POSICAO ESTA OCUPADA
        else:
            segundaTentativa = 1
            while(segundaTentativa == 1):
                print("Esta posicao esta ocupada !")
                print()
                print("------------- Vez do jogador 'O' -------------")
                print()
                linhaO = int(input("Informe novamente a linha de O: "))
                if(linhaO > 2 or linhaO < 0):
                    segundaTentativa = 1
                    while(segundaTentativa == 1):
                        print()
                        print("Coordenada invalida ! Digite um valor entre 0 e 2")
                        print()
                        print("-------- Vez do jogador 'O' --------")
                        print()
                        linhaO = int(input("Informe novamente a linha de O: "))
                        if(linhaO >= 0 and linhaO <= 2):
                            segundaTentativa = 0
                colunaO = int(input("Informe novamente a coluna de O: "))
                if(colunaO > 2 or colunaO < 0):
                    segundaTentativa = 1
                    while(segundaTentativa == 1):
                        print()
                        print("Coordenada invalida ! Digite um valor entre 0 e 2")
                        print()
                        print("-------- Vez do jogador 'O' --------")
                        print()
                        colunaO = int(input("Informe novamente a coluna de X: "))
                        if(colunaO >= 0 and colunaO <= 2):
                            segundaTentativa = 0
                print()
                
                if(matrizBase[linhaO][colunaO] == 0):
                    matrizBase[linhaO][colunaO] = 2
                    #---------------OBTENDO AS COORDENADAS PARA PODER EXIBIR---------------#

                    if(linhaO == 0 and colunaO == 0):          
                        l = list(linha0)
                        l[1] = 'O'
                        linha0 = "".join(l)
                        
                    if(linhaO == 0 and colunaO == 1):          
                        l = list(linha0)
                        l[5] = 'O'
                        linha0 = "".join(l)
                        
                    if(linhaO == 0 and colunaO == 2):          
                        l = list(linha0)
                        l[9] = 'O'
                        linha0 = "".join(l)
                        
                    if(linhaO == 1 and colunaO == 0):          
                        l = list(linha1)
                        l[1] = 'O'
                        linha1 = "".join(l)
                        
                    if(linhaO == 1 and colunaO == 1):          
                        l = list(linha1)
                        l[5] = 'O'
                        linha1 = "".join(l)
                        
                    if(linhaO == 1 and colunaO == 2):          
                        l = list(linha1)
                        l[9] = 'O'
                        linha1 = "".join(l)
                        
                    if(linhaO == 2 and colunaO == 0):          
                        l = list(linha2)
                        l[1] = 'O'
                        linha2 = "".join(l)
                        
                    if(linhaO == 2 and colunaO == 1):          
                        l = list(linha2)
                        l[5] = 'O'
                        linha2 = "".join(l)
                        
                    if(linhaO == 2 and colunaO == 2):          
                        l = list(linha2)
                        l[9] = 'O'
                        linha2 = "".join(l)
                    
                    print()
                    
                    #-------VALIDACOES DE VITORIA-------#
            
                    #CONDIÇÃO PARA GANHAR NO EIXO X
                    for i in range(len(matrizBase)):
                        if(matrizBase[i][0] == 2 and matrizBase[i][1] == 2 and matrizBase[i][2] == 2):
                            print("------------- O jogador 'O' ganhou -------------")
                            print()
                            fim = 0
                    
                    #CONDIÇÃO PARA GANHAR NO EIXO Y
                    for j in range(len(matrizBase)):
                        if(matrizBase[0][j] == 2 and matrizBase[1][j] == 2 and matrizBase[2][j] == 2):
                            print("------------- O jogador 'O' ganhou -------------")
                            print()
                            fim = 0
                            
                    #CONDIÇÃO PARA GANHAR NA DIAGONAL PRINCIPAL
                    if(matrizBase[0][0] == 2 and matrizBase[1][1] == 2 and matrizBase[2][2] == 2):
                        print("------------- O jogador 'O' ganhou -------------")
                        print()
                        fim = 0
                        
                    #CONDIÇÃO PARA GANHAR NA DIAGONAL SECUNDARIA
                    if(matrizBase[0][2] == 2 and matrizBase[1][1] == 2 and matrizBase[2][0] == 2):
                        print("------------- O jogador 'O' ganhou -------------")
                        print()
                        fim = 0           
                    
                    #CONDICAO DE EMPATE
                    empate += 1
                    if(empate == 9):
                        print("------------- O jogo empatou -------------")
                        print()
                        fim = 0
                    
                    segundaTentativa = 0
                    
        print()
        print("########## O JOGO DA VELHA ##########")
        print()
        print(linha0)
        print("---+---+---")
        print(linha1)
        print("---+---+---")
        print(linha2)

        print()
        
    rodada *= -1
        