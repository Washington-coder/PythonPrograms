nome = input()
nota = float(input())
frequencia = int(input())

if(nota >= 5.0 and frequencia >= 45):
    print(nome,"- Aprovado")
else:
    print(nome,"- Reprovado")