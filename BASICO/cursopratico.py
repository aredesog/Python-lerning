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

peso = int(input('DIgite seu peso: '))
altura = int(input('Digite sua altura'))