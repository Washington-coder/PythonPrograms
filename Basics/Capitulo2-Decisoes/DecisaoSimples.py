nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
prioridade = "Não"

if idade >= 65:
    prioridade = "Sim"
print("O paciente", nome, "possui atendimento prioritário?",prioridade)