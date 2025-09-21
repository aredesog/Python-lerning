'''

# Uso dos Exercicos pré ditados na ALURA para aprofundamento do conteúdo

print('\nPython na Escola de Programação da Alura\n')

# Declaração de variáveis e inserção em uma frase 
nome = 'Guilherme'
idade = 19 
print(f'Meu nome é {nome} e tenho {idade} anos')

#Impressão da palavra ALURA

print(
'''
#A
#L
#U
#R
#A
''')

# Frase com valor de Pi

pi = 3.14159 
print(f'O valor arredondado de pi é: {pi:.2f}')


#Solicite ao usuário que insira um número, par ou impara?

print('\n IMPAR ou PAR?\n')

numero = int(input('Digite um número\n'))

if numero % 2 == 0: 
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')

#Pergunte da idade e clçassifique

print('\nVerficação de idade\n')

idade = int(input('Digite a sua idade:'))

if idade <= 12:
    print(f'Criança pela idade {idade}')
elif 13<= idade <= 18:
    print(f'Adolescente pela idade {idade}')
else:
    print(f'Adulto pela idade {idade}')

#Solicite uma senha e um nome de Usuario e faça a a verificação

print('\nVerificação de Usuário\n')

nome = str(input('Digite seu nome de Usuário: '))
senha = int(input('Digite sua senha: '))

nome_verificado = str(input('\nDigite seu nome de Usuário: '))
senha_verficada = int(input('Digite sua senha: '))

if nome == nome_verificado and senha == senha_verficada:
    print('\nAcesso Liberado')
else:
    print('\nAcesso Negado')
    
#Verificação de coordenadas e quadrantes

print('\nCoordenadas e seus Quadrantes\n')

x = int(input('Digite as coordenadas de x:'))
y = int(input('Digite as coordenadas de y:'))

if x > 0 and y > 0:
    print('Coordenada localizada no 1° Quadrante')
elif x < 0 and y > 0:
    print('Coordenada localizada no 2° Quadrante')
elif x > 0 and y < 0:
    print('Coordenada localizada no 3° Quadrante')
elif x < 0 and y < 0:
    print('Coordenada localizada no 4° Quadrante')
else:
    print('Ponto localizado na origem!')

'''

