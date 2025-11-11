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



#Listando coisas

numeros =[1,2,3,4,5,6,7,8,9,10]
nomes = ['angela','aredes','paola','mendes']
anos = [2006, 2025]

for numero in numeros:
    print(f"O numero e: {numero}\n")

for nome in nomes:
    print(f"O nome é: {nome}\n")

for ano in anos:
    if ano == 2006:
        print(f"O ano que eu nasci é: {ano}\n")
    else:
        print(f"O ano atual é: {ano}")


#Cauculando numeros impares da lista numeros

soma = 0
numeros =[1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if (numero % 2) == 1:
        soma = soma + numero
        print(f"A soma esta em: {soma}")
    else:
        print("\nEsse numero é par!")

print(f"\nA soma dos numeros impares é: {soma}\n")



#Imprimindo em ordem decrescente

i = 0

for i in range(10, 0, -1):
    print(i)


#Impressão da tabuada de um numero solicitado

i = 0
Z = 0

valor = int(input("Digite um numero que deseja saber a tabuda de 0 a 10: "))

for i in  range(11):
    print(f"{Z} x {valor} = {Z*valor} \n")
    Z = Z + 1


#Soma de todos os elementos da lista com o try

numeros =[1,2,3,4,5,6,7,8,9,10]
soma = 0
i = 0

try:
    for numero in numeros:
        soma = soma + numero[i] 
        i = i + 1
        print(f"A soma dos elementos foi: {soma}")
except Exception as e:
    print(f"Ocorreu um erro {e}")



#Media de todos os elementos de uma lista

soma = 0
numeros =[1,2,3,4,5,6,7,8,9,10]

try:
    for numero in numeros:
        soma = soma + numero 
        print(f"A soma dos elementos foi: {soma}")
    media = soma/ len(numeros)
    print(f"A media cauculada foi {media}")
except ZeroDivisionError:
    print("Lista vazia")
except Exception as e:
    print(f"Ocorreu um erro {e}")
    
    '''

    


