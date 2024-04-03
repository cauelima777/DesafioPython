print("Digite o seu salário mensal")
salario = float(input())

if salario <= 280:
    aumento_percentual = 20
    aumento = salario * (aumento_percentual / 100)
    novo_salario = salario + aumento
elif salario <= 700:
    aumento_percentual = 15
    aumento = salario * (aumento_percentual / 100)
    novo_salario = salario + aumento
elif salario <= 1500:
    aumento_percentual = 10
    aumento = salario * (aumento_percentual / 100)
    novo_salario = salario + aumento
else:
    aumento_percentual = 5
    aumento = salario * (aumento_percentual / 100)
    novo_salario = salario + aumento

print("1. Salário antes do reajuste:", salario)
print("2. Percentual de aumento aplicado:", aumento_percentual, "%")
print("3. Valor do aumento:", aumento)
print("4. Novo salário após o aumento:", novo_salario)

inflacao = 3.8 / 100
aumento_real = aumento - (aumento * inflacao)
print("5. Valor do aumento real, descontado a inflação:", aumento_real)
