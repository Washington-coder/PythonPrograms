horas = float(input())

if horas >= 0 and horas <= 10:
    pagamento = horas * 50 + 500
elif horas > 10 and horas <= 20:
    pagamento = horas * 60 + 600
elif horas > 20 and horas <= 30:
    pagamento = horas * 70 + 700
elif horas > 30:
    pagamento = horas * 80 + 800

print(round(pagamento,1))