# Monitorando Vendas
'''
x = int(input('Digite a quantidade de bananas vendidas: '))
y = int(input('\nDigite a quantidade de maças vendidas: '))

if x == y:
    print(f'\nA quantidade de maças e bananas vendidas foi igual{x}')
elif x < y: 
    print(f'\nAs mais vendidas foram as maças: {y}')
elif x > y: 
    print(f'\nAs mais vendidas foram as bananas: {x}')
'''
#Cauculando o tempo total do projeto
'''
A = input('Digite o tempo do projeto A: ')
B = input('Digite o tempo do projeto B: ')
C = input('Digite o tempo do projeto C: ')

if (A >= 0 and B >= 0 and C >= 0):
    tempo_total = A + B + C
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else: 
    print("Erro: Os dias não podem ser negativos.")
'''
#Temperatura dos servidores
'''
temperatura = int(input('Digite e atemperatura:'))

if temperatura >= 26:
    print('Alerta de perigo, temperatura muito alta!')
else:
    print(f'Temperatura = a {temperatura}°')
'''
#Calculo de IMC
'''
peso = int(input('DIgite seu peso: '))
altura = float(input('Digite sua altura:'))

IMC = peso/(altura*altura)

if IMC < 18.5:
    print('abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('peso normal')
else:
    print('acima do peso')
'''
#Controlando orçamento mensal
'''
limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")
'''
#COntrole de acesso ao escritorio
hora_atual = int(input("Digite a hora atual (formato 24 horas): "))
'''
if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
'''
#Classificando estudantes 
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")
'''
#Calculando Pedagio
'''
distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")
'''