#tem que usar: if, elif, else e match case - funções (def) - listas (espero que tuplas e string não)- while e for
#menu ja ta feito, fazer o sobre, cinco itens no minimo e quatro funcionais já vou passar, formatar dados e deixar a leitura agradável, usabilidade
#ok perguntar sobre a manipulação de listas
#fzr no mínimo 3 funções. usar parâmetros e retorno
#funções já vão ter cadastro, busca, validação e TALVEZ análise de dados, mas ver um jeito de mexer com números
#funções tem que ter comentários explicando
#isso é obrigatório: validar dados inseridos pelo usuário - exibir relatórios e análises produzidas pelo sistema.
import random

contas = [] #colocar email + senha (talvez nome)
meus_alertas = ["Há uma nevasca perto de você. Procure um local seguro para se abrigar e busque mais orientações. - 29/05/2026", "Há um incêndio perto de você. Procure se manter longe do fogo e busque mais orientações. - 27/05/2026", "Há uma tempestade perto de você. Procure um local seguro para se abrigar e busque mais orientações. - 25/05/2026"]
fav_locais = []
alertas_brasil = ["Risco de 'super El Niño' faz Governo montar grupo de monitoramento. - 31/05/2026", "Chuvas e muitas nuvens sobre o litoral nordestino. - 30/05/2026", "Frio intenso volta a afetar as regiões Sul e Sudeste do país, derrubando as temperaturas. - 27/05/2026"]
previsao_tempo = ["Hoje | Mín: 15° - Máx: 21° | Sol entre nuvens", "Segunda-feira | Mín: 13° - Máx: 21° | Sol entre nuvens", "Terça-feira | Mín: 12° - Máx: 20° | '45%' de chance de chuva", "Quarta-feira | Mín: 12° - Máx: 20° | Nublado", "Quinta-feira | Mín: 13° - Máx: 20° | Nublado", "Sexta-feira | Mín: 11° - Máx: 20° | '45%' de chance de chuva", "Sábado | Mín: 10° - Máx: 21° | Sol", "Domingo | Mín: 10° - Máx: 22° | Nublado"]
historico_locais = []

def favoritar_local(local): #Função com o objetivo de favoritar o local inserido pelo usuário. A função também realiza uma busca para, caso o local inserido pelo usuário já esteja favoritado, não duplicá-lo na lista.
    if local in fav_locais:
        print("Não foi possível favoritar esse local pois ele já está favoritado.")
    else: 
        fav_locais.append(local)
        print("O local foi favoritado com sucesso!")

def mostrar_listas(lista): #Função com o objetivo de facilitar a formatação de listas para a exibição.
    if len(lista) == 0:
        print("Não há nenhum item aqui.")
    else:
        for elemento in lista:
            print(elemento)

def assinatura(area, status): #Função para realizar o cálculo do valor do plano Agro, baseando-se em fatores como o tamanho da propriedade e seu propósito (subsistência ou comercial).
    if area <=0:
        print("Valor inválido fornecido para a quantidade de hectares. Para prosseguir com a assinatura, selecione a opção 7 novamente.")
        return None
    else:
        preco = area * 0.5
        if status == 1:
            preco += 40
        elif status == 2:
            preco += 140
        else:
            print("Não foi possível completar a assinatura. Para prosseguir com a assinatura, selecione a opção 7 novamente.")
            return None
        return preco
    
def alerta_busca_locais(): #Função responsável por determinar a situação do local que o usuário pesquisou.
    alerta_local = random.randint(1, 11)
    if 1 <= alerta_local <= 4:
        return "Tempo firme."
    elif 5 <= alerta_local <= 6:
        return "Sol entre nuvens."
    elif 7 <= alerta_local <= 8:
        return "Céu nublado."
    elif 9 <= alerta_local <= 10:
        return "Chuva."
    elif alerta_local == 11:
        return "Tempestade."
    elif alerta_local == 12:
        return "Chuva com enchente próxima ao local."
    else: 
        return "Tempo firme, mas um incêndio foi registrado próximo ao local."
    
def adicionar_ao_historico(lugar_e_alerta): #Função responsável por adicionar o local pessquisado ao histórico.
    if lugar_e_alerta not in historico_locais:
        historico_locais.append(lugar_e_alerta)


opcao = -1

while opcao != 0:
    print("\n===== Menu Geo Rocket =====")
    print("1 - Sobre a Geo Rocket.") # máximo 5 linhas
    print("2 - Cadastrar uma nova conta.") # fzr com função
    print("3 - Logar em uma conta.") #talvez eu faça isso - colocar instruções detalhadas pro usuário - fzr com função
    print("4 - Conferir meus alertas.")
    print("5 - Adicionar um local aos meus favoritos.") #talvez fazer com função
    print("6 - Conferir meus locais favoritos.")
    print("7 - Ver planos.") #fazer opção para assinar o outro plano ||| perguntar sobre as coisas de pagamento e se precisa add novas coisas
    print("8 - Conferir alertas do Brasil.")
    print("9 - Ver previsão do tempo.")
    print("10 - Buscar um local.") # fazer com função (talvez criarv um sistema que gere números aleatórios e com base nesses números vai ser um alerta) ||| talvez eu tenha problemas em manter o local ligado ao alerta
    print("11 - Ver histórico de locais buscados.")
    print("12 - Ver meu local.") #fazer isso é uma possibilidade
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
            email_login = input("Digite seu email: ").strip()
            senha_login = input("Digite sua senha: ").strip()
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
            mostrar_listas(meus_alertas)

        case 5:
            print("Para favoritar um local, insira seu endereço abaixo. Caso deseje, pode colocar um nome para identificar o local")
            lugar_fav = input("Digite o endereço do local que você deseja favoritar: ").strip()
            adicionar_nm = int(input("Deseja adicionar um nome para o local? Digite 1 para sim e 2 para não: "))
            if adicionar_nm == 1:
                nome = input("Digite o nome que deseja colocar no local: ").strip()
                lugar_com_nome = {"Lugar": lugar_fav, "Nome": nome}
                favoritar_local(lugar_com_nome)
            else:
                lugar_sem_nome = {"Lugar": lugar_fav}
                favoritar_local(lugar_sem_nome)

        case 6:
            mostrar_listas(fav_locais) #perguntar pra prof sobre a formatação daqui

        case 7:
            print("\nA Geo Rocket possui 2 planos:")
            print("\nPlano Básico: O plano básico concede ao usuário acesso a todos os serviços básicos da Geo Rocket. O usuário pode procurar locais, receber alertas, consultar uma previsão precisa do tempo, entre outras funcionalidades.")
            print("\nPlano Agro: O plano Agro é voltado principalmente a usuários com propriedades agrícolas que desejam usufruir do monitoramento da Geo Rocket de forma mais avançada. Com este plano, a Geo Rocket irá monitorar a propriedade do assinante, notificando-o de eventos climáticos, alterações na vegetação, incêndios, alagamentos, entre outros acontecimentos. O preço da assinatura é proporcional ao tamanho da propriedade.")

            assinar_plano = int(input("\nDeseja assinar o plano Agro? Digite 1 para sim e 2 para não: "))
            if assinar_plano == 1:
                print("Perfeito! Para prosseguir, insira os dados requisitados abaixo: ")

                hectare = float(input("Sua propriedade possui quantos hectares? "))
                subsistencia = int(input("Sua propriedade possui qual propósito? Digite 1 para Subsistência e 2 para Comercial: "))
                endereco = input("Digite o endereço de sua propriedade: ").strip()

                valor = assinatura(hectare, subsistencia)

                if valor is not None:
                    print("\n===== RESUMO DA ASSINATURA =====")
                    print(f"Endereço: {endereco}")
                    print(f"Área: {hectare} hectares")
                    print(f"Valor mensal: R${valor:.2f}")
                    print("==================================\n")
                
                    confirmar_assinatura = int(input("Deseja prosseguir? Digite 1 para sim e 2 para não: "))
                    if confirmar_assinatura == 1:
                        print("Perfeito! Sua assinatura foi confirmada!")
                    else:
                        print("Ok, retornando para o menu.")

                else:
                    print("Não foi possível completar a assinatura. Para prosseguir com a assinatura, selecione a opção 7 novamente.")                    
            else:
                print("Ok, retornando para o menu.")

        case 8:
            mostrar_listas(alertas_brasil)

        case 9:
            mostrar_listas(previsao_tempo)

        case 10:
            print("Esta é a busca de locais. Aqui, você consegue procurar por um local no Brasil e verificar sua situação em tempo real, podendo ver como está o tempo e  se há algum evento como enchentes ou incêndios.")
            lugar_busca = input("Digite o endereço do local que você deseja buscar: ").strip()
            situacao = alerta_busca_locais()
            print(lugar_busca + " - " + situacao)
            lugar_e_situacao = {"Lugar buscado": lugar_busca, "Situação": situacao}
            adicionar_ao_historico(lugar_e_situacao)

        case 11:
            mostrar_listas(historico_locais)

        case 12:
            print("Atualmente, você se encontra em: Avenida Paulista - Bela Vista, São Paulo - SP")

        case 0:
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida. Digite uma opção válida do menu.")







            