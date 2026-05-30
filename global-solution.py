#tem que usar: if, elif, else e match case - funções (def) - listas (espero que tuplas e string não)- while e for
#menu ja ta feito, fazer o sobre, cinco itens no minimo e quatro funcionais já vou passar, formatar dados e deixar a leitura agradável, usabilidade
#ok perguntar sobre a manipulação de listas
#fzr no mínimo 3 funções. usar parâmetros e retorno
#funções já vão ter cadastro, busca, validação e TALVEZ análise de dados, mas ver um jeito de mexer com números
#funções tem que ter comentários explicando
#isso é obrigatório: validar dados inseridos pelo usuário - exibir relatórios e análises produzidas pelo sistema.

contas = [] #colocar email + senha (talvez nome)
alertas = ["Há uma nevasca perto de você. Procure um local seguro para se abrigar e busque mais orientações. - 29/05/2026", "Há um incêndio perto de você. Procure se manter longe do fogo e busque mais orientações. - 27/05/2026", "Há uma tempestade perto de você. Procure um local seguro para se abrigar e busque mais orientações. - 25/05/2026"]

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
    print("9 - Ver previsão do tempo.")
    print("10 - Procurar um local.") # fazer com função (talvez criarv um sistema que gere números aleatórios e com base nesses números vai ser um alerta)
    print("11 - Ver meu local.") #fazer isso é uma possibilidade
    print("0 - Sair.")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite apenas números.")
        continue

    match opcao:
        case 1:
            print("A Geo Rocket é uma empresa voltada ao monitoramento de áreas rurais e urbanas, através do uso de satélites, a fim de registrar e prever ocorrências como incêndios, tempestades e outros eventos potencialmente perigosos para a população. O principal objetivo da Geo Rocket é tornar seu entorno ainda mais seguro, pois, através de nosso aplicativo, o usuário poderá acessar um serviço de previsão do tempo acurado e conferir riscos potenciais ou acontecimentos em tempo real em sua localidade e, assim, ter mais tempo para se preparar e proteger de uma ocorrência.")

        case 2:
            print("Seja bem-vindo a Geo Rocket! Para criar uma conta, siga os seguintes passos: ")
            username = input("Digite seu nome de usuário: ").strip()
            email = input("Digite seu email: ").strip()
            senha = input("Digite sua senha: ").strip()
            user_conta = {"username": username, "email": email, "senha": senha}
            contas.append(user_conta)
            print("Parabéns, Sua conta foi cadastrada com sucesso!")

        case 3:
            print("Para logar em sua conta, insira os dados solicitados abaixo: ")
            email_login = input("Digite seu email: ")
            senha_login = input("Digite sua senha: ")
            login = {"email_login": email_login, "senha_login": senha_login}
            
            logado = False

            for conta in contas:
                if conta["email"] == email_login and conta["senha"] == senha_login:
                    logado = True
                    print("Parabéns, você fez login com sucesso!")
                    break  

            if not logado:
                    print("Houve um erro, seu email ou senha estão errados.")

        case 4: 
            print(alertas)





            