from numpy import round_


listaProdutos = eval(input())
listaQtdProdutos = eval(input())

total = 0

for i in range(len(listaProdutos)):
    if(listaProdutos[i] == "ARROZ"):
        total += listaQtdProdutos[i] * 1.25
    if(listaProdutos[i] == "FEIJAO"):
        total += listaQtdProdutos[i] * 2.60
    if(listaProdutos[i] == "BIS"):
        total += listaQtdProdutos[i] * 1.80
    if(listaProdutos[i] == "MIOJO"):
        total += listaQtdProdutos[i] * 0.85
    if(listaProdutos[i] == "FANTA"):
        total += listaQtdProdutos[i] * 3.20

print(round_(total, 2))