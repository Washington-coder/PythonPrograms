ano = int(input())

if ((ano % 400 == 0) or (ano % 4 == 0)) and ano % 100 != 0:
    print("EH BISSEXTO")
else:
    print("NAO EH BISSEXTO")