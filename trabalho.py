import csv

# Leitura do arquivo CSV
with open('registros.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    matriz = list(reader)

# função para salvar as alterações no arquivo CSV (opção 6 no menu)
def salvar(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for linha in matriz:
            writer.writerow(linha)

# função para cadastrar felinos (opção 1 do menu)
def CadastrarFelino(matriz):
    nome = input('1 - Digite o Nome do Felino (ou digite 0 para voltar ao menu principal): ').upper()
    if nome == '0':
        print("Voltando ao menu principal...")
        return
    sexo = input('2 - Digite o sexo do Felino (M ou F): ').upper()
    idade = input('3 - Digite a idade do Felino: ')
    raca = input('4 - Digite a raça do Felino: ').upper()
    cor = input('5 - Digite a cor predominante do Felino: ').upper()
    castrado = input('6 - O felino é castrado? (S ou N): ').upper()
    data_resgate = input('7 - Digite a data do resgate: [dd/mm/aaaa]')
    adotado = input('8 - O felino foi adotado? (S ou N): ').upper()
    print("")
    nova_linha = [nome, sexo, idade, raca, cor, castrado, data_resgate, adotado]
    matriz.append(nova_linha)
    print("Novo felino cadastrado com sucesso.")
    return


# função para alterar informações dos felinos (opção 2 do menu)
def alterar_status(matriz):
    while True:
        print("******* Lista de Felinos *******")
        for i, felino in enumerate(matriz):
            print(f"{i + 1}: Nome: {felino[0]} | Idade: {felino[2]}| Raça: {felino[3]}")
        
        escolha = input("Escolha o número do felino que deseja alterar ou '0' para voltar ao menu principal: ")

        try:
            escolha = int(escolha)
            if escolha == 0:
                print("Voltando ao menu principal...")
                return
            elif 1 <= escolha <= len(matriz):
                felino_selecionado = matriz[escolha - 1]
                print("\n******* Informações do Felino Selecionado *******")
                for j, info in enumerate(felino_selecionado):
                    print(f"{j + 1}: {info}")
                
                while True:
                    num_info = input("\nEscolha o número da informação que deseja alterar ou '0' para voltar ao menu anterior: ")
                    try:
                        num_info = int(num_info)
                        if num_info == 0:
                            break
                        elif 1 <= num_info <= len(felino_selecionado):
                            nova_info = input(f"Digite a nova informação para '{felino_selecionado[num_info - 1]}': ")
                            felino_selecionado[num_info - 1] = nova_info
                            print("Informação alterada com sucesso.")
                        else:
                            print("Número de informação inválido.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
            else:
                print("Número de felino inválido.")
        except ValueError:
            print("Por favor, digite um número válido para escolher o felino.")

# função para consultar informações dos felinos (opção 3 do menu)
def consultar_informacoes_felino(matriz):
    print("\nLista de felinos:")
    for idx, felino in enumerate(matriz):
        print(f"{idx + 1}: {felino[0]}")
    
    escolha = int(input("Escolha o número do felino que deseja consultar: ")) - 1
    print("\nInformações do felino selecionado:")
    print(f"Nome: {matriz[escolha][0]}")
    print(f"Sexo: {matriz[escolha][1]}")
    print(f"Idade: {matriz[escolha][2]}")
    print(f"Raça: {matriz[escolha][3]}")
    print(f"Cor predominante: {matriz[escolha][4]}")
    print(f"Castrado: {matriz[escolha][5]}")
    print(f"Data de resgate: {matriz[escolha][6]}")
    print(f"Adotado: {matriz[escolha][7]}")

# Função para calcular estatísticas sobre a planilha (opção 4 do menu)
def calcular_estatisticas(matriz):
    total_felinos = len(matriz)
    total_machos = sum(1 for felino in matriz if felino[1] == 'M')
    total_femeas = total_felinos - total_machos
    
    total_adotados = sum(1 for felino in matriz if felino[7] == 'S')
    total_nao_adotados = total_felinos - total_adotados
    
    print('')
    print("\n********* Estatísticas gerais: *********")
    print(f"Porcentagem de machos: {total_machos / total_felinos * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {total_femeas / total_felinos * 100:.2f}%")
    print(f"Porcentagem de adotados: {total_adotados / total_felinos * 100:.2f}%")
    print(f"Porcentagem de não adotados: {total_nao_adotados / total_felinos * 100:.2f}%")
    print('**********************************************')

# Função de filtragem (opção 5 do menu)
def filtragem_dados(matriz):
    while True:
        print("\n******* Submenu de Filtragem *******")
        print("1) Consultar gatos resgatados por período")
        print("2) Consultar gatos adotados por período")
        print("0) Voltar ao menu principal")
        
        subopcao = input("Digite o número da subopção que deseja: ")
        
        if subopcao == '0':
            print("Voltando ao menu principal...")
            break
        elif subopcao in ['1', '2']:
            ano_inicio = input("Digite o ano de início (aaaa): ")
            ano_fim = input("Digite o ano de fim (aaaa): ")
            
            try:
                ano_inicio = int(ano_inicio)
                ano_fim = int(ano_fim)
                
                if subopcao == '1':
                    # Filtragem por período de resgate
                    felinos_filtrados = []
                    for felino in matriz:
                        try:
                            ano_resgate = int(felino[6].split('/')[-1])
                            if ano_inicio <= ano_resgate <= ano_fim:
                                felinos_filtrados.append(felino)
                        except ValueError:
                            print(f"Data de resgate inválida para o felino: {felino[0]}")
                    print(f"\nGatos resgatados entre {ano_inicio} e {ano_fim}:")
                elif subopcao == '2':
                    # Filtragem por período de adoção
                    felinos_filtrados = []
                    for felino in matriz:
                        try:
                            ano_resgate = int(felino[6].split('/')[-1])
                            if felino[7] == 'S' and ano_inicio <= ano_resgate <= ano_fim:
                                felinos_filtrados.append(felino)
                        except ValueError:
                            print(f"Data de resgate inválida para o felino: {felino[0]}")
                    print(f"\nGatos adotados entre {ano_inicio} e {ano_fim}:")
                
                if not felinos_filtrados:
                    print("Nenhum gato encontrado nesse período.")
                else:
                    for felino in felinos_filtrados:
                        print(f"Nome: {felino[0]}, Sexo: {felino[1]}, Idade: {felino[2]}, Raça: {felino[3]}, Cor: {felino[4]}, Castrado: {felino[5]}, Data de Resgate: {felino[6]}, Adotado: {felino[7]}")
            except ValueError:
                print("Por favor, digite anos válidos.")
        else:
            print("Subopção inválida. Por favor, digite uma subopção válida.")


########################## Código ##########################

while True: # apresenta o menu até o usuário digitar 7 
    print('******* MENU *******')
    print('1) Cadastrar felino ')
    print('2) Alterar status de felino')
    print('3) Consultar informações sobre felino')
    print('4) Apresentar estatísticas gerais')
    print('5) Filtragem de dados')
    print('6) Salvar')
    print('7) Sair do programa')
    print('')

    opcaousuario = input("Digite o número da opção que deseja: ")

    if opcaousuario == '1':
        CadastrarFelino(matriz)
    elif opcaousuario == '2':
        alterar_status(matriz)
    elif opcaousuario == '3':
        consultar_informacoes_felino(matriz)
    elif opcaousuario == '4':
        calcular_estatisticas(matriz)
    elif opcaousuario == '5':
        filtragem_dados(matriz)
    elif opcaousuario == '6':
        salvar('registros.csv', matriz)
        print('')
        print('Registros atualizados com sucesso!')
        print('')
    elif opcaousuario == '7':
        print('')
        print("Salvando e Saindo do programa...")
        print('')
        salvar('registros.csv', matriz)
        break  #sair do loop