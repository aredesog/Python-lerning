#Clientes

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

#Contador 
contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1  

#Bem-vindo

for i in range(5):
    print("Bem-vindo ao Buscante!")

#Soma

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma total das receitas é: {soma}")

#projeto

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)

#Livro

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break

#estoque

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break

#contagem 

for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")