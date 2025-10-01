#Bibliotecas do Python

import os

# Uma lista de restaurantes, como se fosse um array em C
restaurantes = [{'nome':'Pizza','categoria':'Sushi', 'ativo': False},
                {'nome':'Sushi', 'categoria': 'italiana', 'ativo': True},
                {'nome': 'Goias', 'categoria':'Sorvete', 'ativo':False},
                ]
                

#Exemplos de funções em Python


def exibir_nome():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system("cls")  #Limpa o terminal e exibe apenas o conteudo da função
    print(texto)
    print()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Encerrando o App')

def opcao_invalida():
    print('Opção Inválida!\n')
    
    voltar_ao_menu()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f"Dgite o nome da categoria do resturante {nome_do_restaurante}")
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes:\n ')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria} | {ativo}' )
    
    voltar_ao_menu()

#Apendendo if, else e elif no python (CONDICIONAIS)

def escolher_opcao():

    try:
        opcao_escolhida = int(input('\nEscolha sua opção: ')) 
        #opcao_escolhida = int (opcao_escolhida) -> Transforma a opcao_escolhida em uma variavel do tipo int
        #print(f'A opção escolhida foi: {opcao_escolhida}')  O uso do (f'x {y}?'), é outro metodo para a vizualização da variavel
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
        main()