#tem que usar: if, elif, else e match case - funções (def) - listas (espero que tuplas e string não)- while e for
#menu ja ta feito, fazer o sobre, cinco itens no minimo e quatro funcionais já vou passar, formatar dados e deixar a leitura agradável, usabilidade
#ok perguntar sobre a manipulação de listas
#fzr no mínimo 3 funções. usar parâmetros e retorno
#funções já vão ter cadastro, busca, validação e TALVEZ análise de dados, mas ver um jeito de mexer com números
#funções tem que ter comentários explicando
#isso é obrigatório: validar dados inseridos pelo usuário - exibir relatórios e análises produzidas pelo sistema.

contas = [] #colocar email + senha (talvez nome)

opcao = -1

while opcao != 0:
    print("\n===== Menu Geo Rocket =====")
    print("1 - Sobre a Geo Rocket.") # máximo 5 linhas
    print("2 - Cadastrar uma nova conta.") # fzr com função
    print("3 - Logar em uma conta.") #talvez eu faça isso - colocar instruções detalhadas pro usuário - fzr com função
    print("4 - Conferir meus alertas.")
    print("5 - Adicionar um local aos meus favoritos.") #talvez fazer com função
    print("6 - Conferir meus locais favoritos.")
    print("7 - Ver planos.") #fazer opção para assinar o outro plano
    print("8 - Conferir alertas do Brasil.")
    print("9 - Procurar um local.") # fazer com função (talvez criarv um sistema que gere números aleatórios e com base nesses números vai ser um alerta)
    print("10 - Ver meu local.") #fazer isso é uma possibilidade
    print("0 - Sair.")