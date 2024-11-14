#ListaS: 
administradores = []
clientes = []
pets = []
servicos = []
usuarios = [administradores, pets, clientes]
agendados = []
registro = []
banho = []
servicos = []


#Codigo de acesso para Administradores
codigo_acesso_adm = "789456"

#Menu principal
def MenuPrincipal ():
    print("\n-----MENU-----")
    print("1. Cadastros")
    print("2. Atendimentos")
    print("3. Consultas/Relatórios")
    print("4. Sair")
    return  input ("\nEscolha uma das opções: ")

#Menu CADASTRO
def MenuCadastros ():
    print("\n-----CADASTROS:-----")
    print("1. Usuarios (Administrador)")
    print("2. Clientes")
    print("3. Pets ")
    print("4. Serviços (Administradores)")
    print("5. Voltar ao Menu Principal")
    return  input ("\nEscolha uma das opções: ")

#Menu CADASTRO: Admnistrador
def MenuADM():
    print("\n----USUÁRIO ADMNISTRADOR-----")
    print("1. Cadastrar novo usuário")
    print("2. Atualizar")
    print("3. Apagar ")
    print("4. Consultar")
    print("5. Voltar ao Menu Cadastro")
    return  input ("\nEscolha uma das opções: ")

#consultar adm
def CadastroADM():
    registro = {}
    registro['Nome_Login'] = input("Digite o nome de login: ")
    registro['Senha_Login'] = input("Digite a senha de login: ")
    registro['NomeCompleto_ADM'] = input("Digite o nome Completo do Usuário: ")
    registro['Telefone_ADM'] = input("Digite o telefone do usuário: ")
    registro['Email_ADM'] = input("Digite o email do usuário: ")
    registro['Endereço_ADM'] = input("Digite o endereço do usuário: ")
    registro['CPF_ADM'] = input("Digite o seu CPF: ")
    administradores.append(registro)
    print("Administrador cadastrado com sucesso!")

# Função para atualizar o Administrador: confere a lista e depois permite que o usuario escolha o dado a ser altera so exibir ele ao usuário, podendo escolher entre atribuir um novo "valor" ou deixar mesmo.
def AtualizarCadastroADM():
    nome_login = input("Digite o login do Administrador a ser atualizado: ")
    for registro in administradores:
        if registro['Nome_Login'] == nome_login:
            print(f"Atualizando Administrador: {nome_login}")
            registro['Nome_Login'] = input(f"Novo nome de login ({registro['Nome_Login']}): ") or registro['Nome_Login']
            registro['Senha_Login'] = input(f"Nova senha ({registro['Senha_Login']}): ") or registro['Senha_Login']
            registro['NomeCompleto_ADM'] = input(f"Novo nome completo ({registro['NomeCompleto_ADM']}): ") or registro['NomeCompleto_ADM']
            registro['Telefone_ADM'] = input(f"Novo telefone do usuário({registro ['Telefone_ADM']}): ") or registro["Telefone_ADM"]
            registro['Email_ADM'] = input(f"Digite o email do usuário({registro ['Email_ADM']}): ") or registro['Email_ADM']
            registro['Endereço_ADM'] = input(f"Digite o endereço do usuário({registro ['Endereço_ADM']}): ") or registro['Endereço_ADM']
            print("Administrador atualizado com sucesso!")
            administradores.append(registro)
            return
    print("Administrador não encontrado.") #caso não encontre o usuario

#Menu CADASTRO:Cliente
def MenuCliente():
    print("\n----USUÁRIO CLIENTE-----")
    print("1. Cadastrar novo usuário")
    print("2. Atualizar")
    print("3. Apagar (Administrador)")
    print("4. Consultar")
    print("5. Voltar ao Menu Cadastro")
    return  input ("\nEscolha uma das opções: ")

def CadastroClientes():
    registro = {}
    registro['Nome_Login'] = input("Digite o nome de login: ")
    registro['Senha_Login'] = input("Digite a senha de login: ")
    registro['NomeCompleto_C'] = input("Digite o nome Completo do Usuário: ")
    registro['Telefone_C'] = input("Digite o telefone do usuário: ")
    registro['Email_C'] = input("Digite o email do usuário: ")
    registro['Endereço_C'] = input("Digite o endereço do usuário: ")
    registro['CPF_C'] = input("Digite o seu CPF: ")
    registro["Nome_Pet"] = input("Nome do Pet: ")
    clientes.append(registro)
    print("Cliente cadastrado com sucesso!")
    
# Função para atualizar o Cliente: confere a lista e depois permite que o usuario escolha o dado a ser altera so exibir ele ao usuário, podendo escolher entre atribuir um novo "valor" ou deixar mesmo.
def AtualizarCadastroC():
    nome_login = input("Digite o login do Cliente a ser atualizado: ")
    for registro in clientes:
        if registro['Nome_Login'] == nome_login:
            print(f"Atualizando Cliente: {nome_login}")
            registro['Nome_Login'] = input(f"Novo nome de login ({registro['Nome_Login']}): ") or registro['Nome_Login']
            registro['Senha_Login'] = input(f"Nova senha ({registro['Senha_Login']}): ") or registro['Senha_Login']
            registro['NomeCompleto_C'] = input(f"Novo nome completo ({registro['NomeCompleto_C']}): ") or registro['NomeCompleto_C']
            registro['Telefone_C'] = input(f"Novo telefone do usuário({registro ['Telefone_C']}): ") or registro["Telefone_C"]
            registro['Email_C'] = input(f"Digite o email do usuário({registro ['Email_C']}): ") or registro['Email_C']
            registro['Endereço_C'] = input(f"Digite o endereço do usuário({registro ['Endereço_C']}): ") or registro['Endereço_C']
            print("Cliente atualizado com sucesso!")
            clientes.append(registro)

            return
    print("Cliente não encontrado.") #caso não encontre o usuario

#consultar cliente
def ConsultarDadosC():
     if clientes:
            print("\nLista de Clientes cadastrados:")
            for registro in clientes:
                print(f"Nome de Login: {registro['Nome_Login']}")
                print(f"Nome Completo: {registro['NomeCompleto_C']}")
                print(f"Telefone: {registro['Telefone_C']}")
                print(f"Email: {registro['Email_C']}")
                print(f"Endereço: {registro['Endereço_C']}")
                print(f"CPF: {registro['CPF_C']}")
                print(f"Nome do Pet: {registro['Nome_Pet']}\n")
     else:
        print("Nenhum cliente cadastrado.")

#Apagar cliente
def Apagar_C():
    print("Você fez um pedido para o Administrador!")
    MenuADM()

#Menu CADASTRO:Pet
def Menu_Pets():
    print("\n----PERFIL PET-----")
    print("1. Cadastrar novo usuário")
    print("2. Atualizar")
    print("3. Apagar (Administrador)")
    print("4. Consultar")
    print("5. Voltar ao Menu Cadastro")
    return  input ("\nEscolha uma das opções: ")

def CadastroPet():
    registro = {}
    registro["Nome_Pet"] = input("Digite nome do Pet:")
    registro["Tipo_Pet"] = input("Digite o tipo de Pet (cachorro, gato, etc): ")
    registro["Raca_Pet"] = input("Digite a raça do Pet: ")
    registro["Data_Nasc_Pet"] = input ("Digite a data de nascimento do pet:")
    registro["Sexo_Pet"] = input ("Digite o sexo do pet: ")
    registro['Nome_Login'] = input("Digite o nome de login do(a) responsável: ")
    registro["CPF_C"] = input("Digite o CPF do(a) responsável: ")
    pets.append(registro)
    print("Cliente cadastrado com sucesso!")

# Função para atualizar o Pet: confere a lista e depois permite que o usuario escolha o dado a ser altera so exibir ele ao usuário, podendo escolher entre atribuir um novo "valor" ou deixar mesmo.
def AtualizarCadastroPet( ):
    nome_pet = input("Digite o nome do Pet a ser atualizado: ")
    for registro in pets:
        if registro['Nome_Pet'] == nome_pet:
            print(f"Atualizando Pet: {nome_pet}")
            registro['Nome_Pet'] = input(f"Novo nome do pet ({registro['Nome_Pet']}): ") or registro['Nome_Pet']
            registro['Tipo_Pet'] = input(f"Novo tipo de pet ({registro['Tipo_Pet']}): ") or registro['Tipo_Pet']
            registro['Raca_Pet'] = input(f"Nova raça ({registro['Raca_Pet']}): ") or registro['Raca_Pet']
            registro['Nome_Login'] = input(f"Novo nome de login do(a) responsável:({registro['Nome_Login']}): ") or registro['Nome_Login']
            print("Pet atualizado com sucesso!")
            pets.append(registro)
            return
    print("Pet não encontrado.")#caso não encontre o usuario

#consultar pets
def ConsultarDadosPets():
    if pets:
            print("\nLista de Pets cadastrados:")
            for registro in pets:
                print(f"Nome do Pet: {registro['Nome_Pet']}")
                print(f"Tipo de Pet: {registro['Tipo_Pet']}")
                print(f"Raça: {registro['Raca_Pet']}")
                print(f"Data de Nascimento: {registro['Data_Nasc_Pet']}")
                print(f"Sexo: {registro['Sexo_Pet']}")
                print(f"Nome de Login do(a) responsável: {registro['Nome_Login']}")
                print(f"CPF do(a) responsável: {registro['CPF_C']}\n")
    else:
        print("Nenhum pet cadastrado.")

#Menu Serviços
def MenuServicos():
        while True: 
            print("----SERVIÇOS----")
            print("1. Adcionar serviço")
            print("2. Apagar serviço")
            print("3. Mostrar Opções")
            print("4. Voltar ao Menu Cadastro")
            return input ("\nEscolha uma das opções: ")

#Consutar Opções de Serviço:      
def ServidorOpcoes():
    print("\n---- OPÇÕES DE SERVIÇOS ----")
    if not servicos:
        print("Não há serviços cadastrados.")
    else:
        for i, servico in enumerate(servicos, start=1):
            id_servico, valor, descricao = servico
            print(f"{i}. ID: {id_servico}\nValor: R${valor}\nDescrição: {descricao}")

#Adicionar Serviço
def adicionar_servico():
        codigo_acesso_adm = input("Digite a senha de admin para acessar:")
        if codigo_acesso_adm == "789456":
            id_servico = input("Digite o novo serviço: ")
            valor = input('Digite o valor do novo serviço: ')
            descricao = input("Digite a descrição do novo serviço: ")
            # Verifica se o ID do serviço já existe
            if any(id_servico == s[0] for s in servicos):
                print("Esse serviço já existe!")
            else:
                servicos.append((id_servico, valor, descricao))
                print("Serviço adicionado com sucesso!")

#Apagar Serviço 
def apagar_servico():
        codigo_acesso_adm = input("Digite a senha de admin para acessar:")
        if codigo_acesso_adm == "789456":
            id_servico = input("Digite o número do serviço a ser apagado: ")
            for servico in servicos:
                if servico[0] == id_servico:
                    servicos.remove(servico)
                    print("Serviço apagado com sucesso!")
                    return
            print("Esse serviço não existe!")
       
#Autenticação de usuário ADM:
def autenticar_administrador():
    codigo = input("\nDigite o código de acesso do administrador: ")
    return codigo == codigo_acesso_adm

#Menu Atendimento
def MenuAtendimento():
    print("-----ATENDIMENTOS-----")
    print("1. Iniciar")
    print("2. Agendar")
    print("3. Remarcar")
    print("4. Voltar ao Menu Principal")
    return  input ("\nEscolha uma das opções: ")

#Menu Atendimento: Agendar
def MenuAgendar ():
      print("\n-----AGENDAR-----")
      nome_pet = input("Nome do animal: ")
      pet_encontrado = False
      # Verifica se o pet está cadastrado
      for registro_pet in pets:
            if registro_pet['Nome_Pet'] == nome_pet:
                pet_encontrado = True
                print(f"Nome do Pet: {nome_pet}")
                print("Usuário autenticado")
                print("Pode seguir para o Agendamento")
                # Exibe as opções de serviço
                ServidorOpcoes()
                try:
                    opcao_AGD = int(input("\nEscolha uma das opções (número do serviço): "))
                    opcao_AGD -= 1  # Ajusta o índice para lista
                    if 0 <= opcao_AGD < len(servicos):
                        id_servico, valor, descricao = servicos[opcao_AGD]
                        print(f"\nVocê selecionou o serviço: {id_servico}\nValor: R${valor}\nDescrição: {descricao}")# Recebe a data e hora do agendamento
                        data = input("Digite a data para o atendimento (dd/mm/aaaa): ")
                        hora = input("Digite a hora para o atendimento (hh:mm): ")
                        # Valida a data e hora
                        if not validar_data(data):
                            print("Data inválida. Tente novamente.")
                            return
                        if not validar_hora(hora):
                            print("Hora inválida. Tente novamente.")
                            # Confirmar agendamento
                        print(f"Agendamento confirmado para o pet {nome_pet} no serviço {id_servico} em {data} às {hora}.")
                        agendados.append({'pet': nome_pet, 'data': data, 'hora': hora, "ID": id_servico})
                        print("O atendimento foi agendado com sucesso!")
                        return servicos[opcao_AGD]
                    else:
                        print("Opção inválida! Por favor, escolha um número da lista.")
                except ValueError:
                    print("Entrada inválida! Por favor, digite um número válido.")
                    break
            if not pet_encontrado:
                print("Pet ainda não cadastrado!")
    

#Validar cliente

def validar_cliente(nome_pet):
    return any(agendamento['pet'].lower() == nome_pet.lower() for agendamento in agendados)

#Validar a hora e data
import re
from datetime import datetime

def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, '%H:%M')
        return True
    except ValueError:
        return False
   
# Menu Atendimento: Remarcar
def MenuRemarcar():
    print("\n-----REMARCAR ATENDIMENTO-----")
    nome_pet = input("Digite o nome do pet: ")
    pet_encontrado = False

    # Verifica se o pet está cadastrado nos agendamentos
    for agendamento in agendados:
        if agendamento['pet'].lower() == nome_pet.lower():
            pet_encontrado = True
            print(f"Pet encontrado: {nome_pet}")
            print("Escolha uma opção para remarcação:")
            print("1. Remarcar Data")
            print("2. Remarcar Horário")
            print("3. Voltar Menu Atendimento")

            # Solicita a opção do usuário
            opcao_remarcar = input("\nEscolha uma das opções (número): ")

            if opcao_remarcar == "1":
                nova_data = input("Digite a nova data para o atendimento (dd/mm/aaaa): ")
                if not validar_data(nova_data):
                    print("Data inválida. Tente novamente.")
                    return
                # Atualiza a data 
                agendamento['data'] = nova_data
                print(f"Data do atendimento para o pet {nome_pet} remarcada para {nova_data}.")
            
            elif opcao_remarcar == "2":
                nova_hora = input("Digite a nova hora para o atendimento (hh:mm): ")
                if not validar_hora(nova_hora):
                    print("Hora inválida. Tente novamente.")
                    return
                # Atualiza a hora 
                agendamento['hora'] = nova_hora
                print(f"Hora do atendimento para o pet {nome_pet} remarcada para {nova_hora}.")
            elif opcao_remarcar == "3":
                MenuAtendimento()
            else:
                print("Opção inválida! Por favor, escolha 1 ou 2.")
            return  

    if not pet_encontrado:
        print("Pet ainda não cadastrado ou não possui agendamento!")

def MenuConsultasERelatorios():
    while True:
        print("\n-----CONSULTAS E RELATÓRIOS-----")
        print("1. Consulta de Agendamentos")
        print("2. Relatório do Pet")
        print("3. Voltar ao Menu Principal")
        return input("\nEscolha uma das opções (número): ")

def ConsultarAgendamentos():
    if agendados:
        print("\n-----AGENDAMENTOS-----")
        for agendamento in agendados:
            print(f"Pet: {agendamento['pet']}, Serviço ID: {agendamento['ID']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")
    else:
        print("Não há agendamentos registrados.")

def RelatorioPet():
    nome_pet = input("\nDigite o nome do pet para consulta do relatório: ")
    pet_encontrado = False

    for pet in pets:
        if pet['Nome_Pet'].lower() == nome_pet.lower():
            pet_encontrado = True
            ConsultarDadosPets()
            # Se o pet tiver uma condição de saúde, o adm pode adicionar  detalhes
            codigo_acesso_adm = input("Digite a senha de admin para acessar:")
            if codigo_acesso_adm == "789456":
                Relatorio = input("Faça um relatório sobre a condição do animal: ")
                pet.append(Relatorio)
                print(f"Relatório atualizado: {pet['Relatorio']}")
                break

    if not pet_encontrado:
        print(f"Pet {nome_pet} não encontrado.")

def login():
    print("-----SISTEMA DE LOGIN-----")
    nome_usuario = input("Digite o nome de usuário: ")

    # Verifica se o nome de usuário já está cadastrado
    if nome_usuario in usuarios:
        senha = input("Digite a senha: ")
        if usuarios[nome_usuario] == senha:
            print("Login bem-sucedido!")
            # Chamar o menu principal ou próximo passo aqui
            MenuPrincipal()
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não cadastrado.")
        # Redireciona para o cadastro
        MenuPrincipal()

#Menu PRINCIPAL

#Chamando menu principal
while True:
    opcao_login = login()
    
    #MENU PRINCIPAL: CADASTRO (chamando menu cadastros)
    opcao_principal = MenuPrincipal()
    if opcao_principal == "1":
        opcao_cadastro = MenuCadastros()
         
         #MENU CADASTRO: Usuário Admnistrador
        if opcao_cadastro == "1":
            if autenticar_administrador():
                while True:
                    opcao_ADM = MenuADM()
                    if opcao_ADM == "1":
                        print("-----CADASTRAR-SE-----")
                        CadastroADM()
                    elif opcao_ADM == "2":
                        print("-----ATUALIZAR-----")
                        AtualizarCadastroADM()
                    elif opcao_ADM == "3":
                        print("-----APAGAR-----")
                        codigo_acesso_adm = input("Digite a senha de Administrador para apagar:")
                        if codigo_acesso_adm == "789456":
                            nome_login = input("Nome do Administrador que será apagado: ")
                            # Iterar sobre a lista de administradores
                            for i in range(len(administradores) - 1, -1, -1):
                                if administradores[i]['Nome_Login'] == nome_login:
                                    del administradores[i]
                                    print("Administrador apagado com sucesso!")
                                    break
                                else:
                                    print("Administrador não encontrado.")
                    elif opcao_ADM == "4":
                        print("-----CONSULTAR------")
                        nome_login = input("Digite o login do Administrador a ser consultado: ")
                        for registro in administradores:
                            if registro['Nome_Login'] == nome_login:
                                 print(f"Dados dos Administradores: {nome_login}")
                                 registro['Nome_Login'] = print(f"Nome de login: ({registro['Nome_Login']})")  
                                 registro['NomeCompleto_ADM'] = print(f"Nome completo: ({registro['NomeCompleto_ADM']})") 
                                 registro['Telefone_ADM'] = print(f"Telefone do usuário: ({registro ['Telefone_ADM']})") 
                                 registro['Email_ADM'] = print(f"Email do usuário({registro ['Email_ADM']}): ") 
                                 registro['Endereço_ADM'] = print(f"Endereço do usuário: ({registro ['Endereço_ADM']})") 
                                 MenuADM()
                            print("Administrador não encontrado.") #caso não encontre o usuario 
                        else:
                            print("Nenhum administrador cadastrado.")
                    elif opcao_ADM == "5":
                        MenuCadastros()
                    else:
                     print("Opção inválida. Tente novamente.")
        
        #MENU CADASTRO: Usuário Cliente
        elif opcao_cadastro == "2":
            while True:
                opcao_C = MenuCliente()
                if opcao_C == "1":
                     print("-----CADASTRAR-SE-----")
                     CadastroClientes()
                elif opcao_C == "2":
                    print("-----ATUALIZAR-----")
                    AtualizarCadastroC()
                elif opcao_C == "3":
                    print("-----APAGAR-----")
                    print("Apagar Cliente")
                    codigo_acesso_adm = input("Digite a senha do Cliente para apagar:")
                    if codigo_acesso_adm == "789456":
                        nome_login = input("Nome do Cliente que quer apagar: ")
                        # Iterar sobre a lista de administradores
                        for i in range(len(clientes) - 1, -1, -1):
                            if clientes[i]['Nome_Login'] == nome_login:
                                del clientes[i]
                                print("Usuário Cliente apagado com sucesso!")
                                break
                            else:
                                print("Cliente não encontrado.")
                    else:
                        print("\nPerfil sem permisão\nSua solicitação para apagar perfil foi enviada aos Administradores ")
                        MenuCliente()
                            
                elif opcao_C == "4":
                     print("-----CONSULTAR------")
                     nome_login = input("Digite o login do Cliente a ser consultado: ")
                     for registro in clientes:
                            if registro['Nome_Login'] == nome_login:
                                 print(f"Dado do Cliente: {nome_login}")
                                 registro['Nome_Login'] = print(f"Nome de login: ({registro['Nome_Login']})")  
                                 registro['NomeCompleto_C'] = print(f"Nome completo: ({registro['NomeCompleto_C']})") 
                                 registro['Telefone_C'] = print(f"Telefone do usuário: ({registro ['Telefone_C']})")
                                 registro['Email_C'] = print(f"Email do usuário({registro ['Email_C']}): ")
                                 registro['Endereço_C'] = print(f"Endereço do usuário: ({registro ['Endereço_C']})") 
                                 MenuCliente()
                            print("Cliente não encontrado.") #caso não encontre o usuario 
                     else:
                        print("Nenhum cliente cadastrado.")
                elif opcao_C == "5":
                    MenuCadastros()
                else:
                     print("Opção inválida. Tente novamente.")
        #MENU CADASTRO: Usuário Pets
        elif opcao_cadastro == "3":
            while True:
                opcao_Pets = Menu_Pets()
                if opcao_Pets == "1":
                     print("-----CADASTRAR-SE-----")
                     CadastroPet()
                elif opcao_Pets == "2":
                    print("-----ATUALIZAR-----")
                    AtualizarCadastroPet()
                elif opcao_Pets == "3":
                    print("-----APAGAR-----")
                    print("Apagar Pet")
                    codigo_acesso_adm = input("Digite a senha de Administrador para apagar:")
                    if codigo_acesso_adm == "789456":
                        nome_login = input("Nome do Pet que quer apagar: ")
                        # Iterar sobre a lista de administradores
                        for i in range(len(pets) - 1, -1, -1):
                            if pets[i]['Nome_Pet'] == nome_login:
                                del pets[i]
                                print(" Usuário Pet apagado com sucesso!")
                                break
                            else:
                                print("Pet não encontrado.")
                    else:
                        print("\nPerfil sem permisão\nSua solicitação para apagar perfil foi enviada aos Administradores ")
                        Menu_Pets()
                            
                elif opcao_Pets == "4":
                     print("-----CONSULTAR------")
                     nome_pet = input("Digite o login do Pet a ser consultado: ")
                     for registro in pets:
                            if registro['Nome_Pet'] == nome_pet:
                                 print(f"Dado do Pet: {nome_pet}")
                                 registro['Nome_Pet'] = print(f"Nome do pet: ({registro['Nome_Pet']}) ")
                                 registro['Tipo_Pet'] = print(f"Tipo de pet: ({registro['Tipo_Pet']}) ") 
                                 registro['Raca_Pet'] = print(f"Nova raça: ({registro['Raca_Pet']}) ")
                                 registro['Nome_Login'] = input(f"Novo nome de login ({registro['Nome_Login']}): ")
                                 Menu_Pets()
                            print("Pet não encontrado.") #caso não encontre o usuario 
                     else:
                        print("Nenhum pet cadastrado.")
                elif opcao_Pets == "5":
                    MenuCadastros()
                else:
                     print("Opção inválida. Tente novamente.")
        #MENU CADASTRO: Serviços
        elif opcao_cadastro == "4":
            while True:
                opcao_servico = MenuServicos()
                if opcao_servico == "1":
                    adicionar_servico()
                elif opcao_servico == "2":
                    apagar_servico()
                elif opcao_servico == "3":
                    ServidorOpcoes()
                elif opcao_servico == "4":
                    MenuCadastros()
                else:
                    ("Opção inválida. Tente novamente.")

        elif opcao_cadastro == "5":
            MenuPrincipal()
        else:
            ("Opção inválida. Tente novamente.")

        #Salvar dados :
        print(administradores)
        print(clientes)
        print(pets)
        print(usuarios)
    #MENU ATENDIMENTOS:
    elif opcao_principal == "2":
        opcao_atd = MenuAtendimento()
         
        #MENU ATENDIMENTOS: Iniciar
        if opcao_atd == "1":
            nome_login = input("Login do cliente: ")
            cliente_encontrado = False
            # Verifica se o cliente está cadastrado
            for registro in clientes:
                if registro['Nome_Login'] == nome_login:
                    cliente_encontrado = True
                    print(f"Login Cliente: {nome_login}")
                    print("Usuário autenticado")
                    nome_pet = input("Nome do animal: ")
                    pet_encontrado = False
                    # Verifica se o pet está cadastrado
                    for registro_pet in pets:
                        if registro_pet['Nome_Pet'] == nome_pet:
                            pet_encontrado = True
                            print(f"Nome do Pet: {nome_pet}")
                            print("Usuário autenticado") 
                            print("Pode seguir para o Agendamento")
                            break  
                        if not pet_encontrado:
                            print("Pet ainda não cadastrado!")
                            break 
                        if not cliente_encontrado:
                            print("Cliente ainda não cadastrado!")

         #MENU ATENDIMENTOS: Agendar
        elif opcao_atd == "2":
            MenuAgendar() 
        elif opcao_atd == "3":
            MenuRemarcar()
        elif opcao_atd == "4":
            MenuPrincipal
        else:
            print("Opção inválida. Tente novamente.")
    #MENU CONSULTAS E RELATORIOS:
    elif opcao_principal == "3":
        opcao_CR = MenuConsultasERelatorios()
        if opcao_CR == "1":
            ConsultarAgendamentos()
        elif opcao_CR == "2":
            RelatorioPet()
        elif opcao_CR == "3":
            MenuPrincipal
        else:
            print("Cliente ainda não cadastrado!")
    #SAIR
    elif opcao_principal == "4":
        break
    


    
