#Bibliotecas do Python

import os

def exibir_nome():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')



#Exemplo de função em Python

def finalizar_app():
    os.system('cls') #Limpa o terminal e exibe apenas o conteudo da função
    print('Encerrando o App')

#Apendendo if, else e elif no python (CONDICIONAIS)

def escolher_opcao():

    opcao_escolhida = int(input('\nEscolha sua opção: ')) 
    #opcao_escolhida = int (opcao_escolhida) -> Transforma a opcao_escolhida em uma variavel do tipo int
    #print(f'A opção escolhida foi: {opcao_escolhida}')  O uso do (f'x {y}?'), é outro metodo para a vizualização da variavel
    
    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar Restaurante')
    elif opcao_escolhida == 3:
        print('Ativar Restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
        main()