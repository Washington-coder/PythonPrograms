flag = False
L = []


def isPrimo(numFlag):
    repeticoes = numFlag
    num = numFlag
    divisores = 0

    if numFlag == 1:
        return True
    else:
        while repeticoes != 0:
            if num % repeticoes == 0:
                divisores += 1
                repeticoes -= 1
            else:
                repeticoes -= 1

        if divisores == 2:
            return True
        else:
            return False


while (flag == False):
    numFlag = int(input())
    if(numFlag != 99):
        if isPrimo(numFlag) == True:
            L.append(True)
        else:
            L.append(False)
    else:
        flag = True

print(L)
