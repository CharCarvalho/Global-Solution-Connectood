import re
import datetime

#Função criada para coletar o nome da pessoa responsável das instituições que buscam doação dos alimentos na plataforma.
def coleta_nome_funcionario():
    corrigir_nome = True
    while corrigir_nome:
        nome_representante = str(input("Digite o nome do(a) representante que irá buscar o alimento: "))
        validar_nome = str(input("Deseja corrigir alguma informação do nome? ('S' para recadastrar/ 'N' para continuar para próxima etapa): "))
        if validar_nome.lower() == "n":
            corrigir_nome = False
    return nome_representante

#Função criada para coletar o endereço da instituição que busca doação dos alimentos na plataforma.
def endereco_instituicao():
    endereco_instituicao = str(input("Digite o endereço da instituição que irá adquirir os alimentos: "))
    return endereco_instituicao

#Função criada para registrar a quantidade e tipos de alimentos buscados para doação pelas instituições beneficentes que utilizarão a plataforma
def lista_de_alimentos_buscados():
    n = int(input("Digite quantos alimentos serão coletados: (a disponibilidade depende de quanto sobrou na feira e apenas 1kg de cada alimento pode ser retirado)"))
    i = 0
    lista_alimentos = []
    while i < n:
        alimentos = str(input("Digite o nome do alimento {}: ".format(str(i + 1))))
        lista_alimentos.append(alimentos)
        i = i + 1
    return lista_alimentos

#Função criada para coletar o nome do feirante que irá se registrar na plataforma e disponibilizará doação de alimentos.
def coleta_nome_feirante():
    corrigir_nome = True
    while corrigir_nome:
        nome_feirante = str(input("Digite o nome do feirante responsável: "))
        validar_nome = str(input("Deseja corrigir alguma informação do nome? ('S' para recadastrar/ 'N' para continuar para próxima etapa): "))
        if validar_nome.lower() == "n":
            corrigir_nome = False
    return nome_feirante

#Função criada para coletar o endereço da feira de atuação do feirante que doará alimentos através da plataforma.        
def endereco_feira():
    endereco_feira = str(input("Digite o endereço da feira em que você atua: "))
    return endereco_feira

#Função criada para registrar quantidade e tipos de alimentos que serão doados pelos feirantes através da plataforma.
def lista_de_alimentos_doados():
    n = int(input("Digite quantos alimentos serão doados: "))
    i = 0
    lista_alimentos_disponiveis = []
    while i < n:
        alimentos = str(input("Digite o nome do alimento {}: ".format(str(i + 1))))
        lista_alimentos_disponiveis.append(alimentos)
        i = i + 1
    return lista_alimentos_disponiveis

#Função criada para registrar o nome da instituição beneficente que buscará doações de alimentos na plataforma.
def nome_instituicao():
    corrigir_nome = True
    while corrigir_nome:
        nome_instituicao = str(input("Digite o nome da instituição (NA caso seja Pessoa Física): "))
        validar_nome = str(input("Deseja corrigir alguma informação do nome? ('S' para recadastrar/ 'N' para continuar para próxima etapa): "))
        if validar_nome.lower() == "n":
            corrigir_nome = False
    return nome_instituicao

#Função criada para cadastrar CPF da pessoa usuária da plataforma. Função coleta e verifica se o CPF é válido.
def numero_cpf():
    valida_cpf = True
    while valida_cpf:
        cpf = str(input("Digite seu CPF, sem ponto e hífen: "))
        cpf_numeros = re.sub(r"[^0-9]", "", cpf)
        if len(cpf_numeros) != 11:
            print("CPF inválido. Digite novamente.")
            valida_cpf = True
        else:            
            cpf_sem_digito_controle = int(cpf_numeros[0:9])
            cpf1 = cpf_sem_digito_controle

            cpf_digito_controle1 = int(cpf_numeros[0:10])
            cpf2 = cpf_digito_controle1

            digito_controle1 = int(cpf_numeros[9])
            digito_controle2 = int(cpf_numeros[10])

            soma = 0
            mult = 2
            while cpf1 > 0:
                digito = cpf1%10
                soma = soma + (digito * mult)
                cpf1 = cpf1//10
                mult = mult + 1
            resto1 = (soma*10)%11

            if resto1 == 10:
                resto1 = 0

            soma = 0
            mult = 2
            while cpf2 > 0:
                digito = cpf2%10
                soma = soma  + (digito * mult)
                cpf2 = cpf2//10
                mult = mult + 1
            resto2 = (soma*10)%11

            if resto2 == 10:
                resto2 = 0

            if ((resto1 == digito_controle1) and (resto2 == digito_controle2)):
                valida_cpf = False
                return cpf
            else:
                print("Esse CPF é inválido! Digite novamente!")

#Função criada para coletar CPF da instituição usuária da plataforma. 
def numero_cnpj():
    valida_cnpj = True
    while valida_cnpj:
        cnpj = str(input("Digite seu CNPJ, sem ponto e hífen: "))
        cnpj_numeros = re.sub(r"[^0-9]", "", cnpj)
        if len(cnpj_numeros) != 14:
            print("CPF inválido. Digite novamente.")
            valida_cnpj = True
        else:            
            return cnpj

#Função criada para coleta do telefone da pessoa usuária da plataforma
def coletar_telefone():
        celular = int(input("Digite um número de celular: "))
        tam = str(celular)
        while len(tam) != 11:
            celular = int(input("Digite um número de celular válido: "))
            tam = str(celular)
        return celular

#Função criada para coletar data de nascimento do feirante. Função verifica se o formato de entrada de dados é válido.
def data_nascimento_feirante():
        data_nascimento = str(input("Digite a data de nascimento no formato DD/MM/AAAA: "))
        while True:
            try:
                datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
                return data_nascimento
            except ValueError: 
                data_nascimento = str(input("Digite CORRETAMENTE a data de nascimento no formato a seguir DD/MM/AAAA: "))

#Função criada para coletar número de certificação MAPA do feirante que se cadastrar na plataforma.
def certificado_MAPA():
    certificacao = str(input("Digite o código de sua certificação MAPA para registro: "))
    return certificacao

#início do programa
iniciar = str(input("Deseja acessar a plataforma Connectood? (S/N): "))
if iniciar.lower() == "s": #caso o usuário decida iniciar o programa, o usuário entrará no menu principal do programa
    continuar = True 
    while continuar: #Laço de repetição criado para que o usuário acesse uma das opções abaixo e, caso deseje, retorne ao menu principal
        print("-----------------------------------------")                   
        print("Connectood - Conectando você a alimentos de qualidade doados da feira mais próxima!")
        print("Abaixo, você encontrará instruções para cadastro,")
        print("busca de alimentos ou doação de alimentos")
        print("Digite: ")
        print("------------")
        print("1 - Buscar Alimentos perto de você")
        print("Verifique a disponibilidade de doações na sua região")
        print("------------")
        print("2 - Registrar alimentos para doação")
        print("Feirante, cadastre alimentos destinados à doação")
        print("------------")
        print("3 - Cadastro na plataforma")
        print("Registro instituição beneficente ou feirante")
        print("-----------------------------------------")
        menu = str(input("Digite qual opção deseja iniciar: "))
        if menu == "1": #opção responsável pela busca de alimentos doados na plataforma, usuário digita o nome, endereço e quais alimentos deseja
            funcionario = coleta_nome_funcionario()
            endereco = endereco_instituicao()
            lista_buscados = lista_de_alimentos_buscados()
            print("-----------------------------------------")
            print("Nome funcionário: ", funcionario)
            print("Endereço Instituição: ", endereco)
            print("Lista de Alimentos Buscados: ", lista_buscados)
            print("-----------------------------------------")
            continuar = False           
        elif menu == "2": #opção responsável pelo registro de alimentos a serem registrados para doação na plataforma
            nome_feirante = coleta_nome_feirante()
            endereco = endereco_feira()
            lista_doados = lista_de_alimentos_doados()
            print("-----------------------------------------")
            print("Nome feirante: ", nome_feirante)
            print("Endereço da feira: ", endereco)
            print("Lista de Alimentos Doados: ", lista_doados)
            print("-----------------------------------------")
            continuar = False            
        elif menu == "3": #opção responsável pelo cadastro, tanto de feirante quanto instituição beneficente, na plataforma           
            verificador_cadastro = True
            while verificador_cadastro:

                print("1 - Cadastro Instituição Beneficente")
                print("2 - Cadastro Feirante")
                tipo_cadastro = str(input("Digite a opção desejada: "))
                
                if tipo_cadastro == "1": #opção responsável pelo cadastro de instituição que receberá doação
                    nome_funcionario = coleta_nome_funcionario()
                    instituicao = nome_instituicao()
                    telefone = coletar_telefone()
                    endereco = endereco_instituicao()                    
                    verificador_cpf_cnpj = True
                    while verificador_cpf_cnpj:

                        print("O cadastro da instituição está vinculado a quais das opções abaixo: ")
                        print("1 - CPF")
                        print("2 - CNPJ")
                        tipo_cpf_cnpj = str(input("Digite a opção desejada: "))

                        if tipo_cpf_cnpj == "1": #caso a instituição esteja vinculada a um CPF, essa opção será selecionada
                            cpf = numero_cpf()
                            print("-----------------------------------------")
                            print("Nome Funcionário cadastrado: ", nome_funcionario)
                            print("Nome da Instituição Cadastrada: ", instituicao)
                            print("Telefone Celular Cadastrado: ", telefone)
                            print("Endereço Cadastrado da Instituição: ", endereco)
                            print("Número CPF vinculado ao cadastro da Instituição: ", cpf)
                            print("-----------------------------------------")
                            verificador_cpf_cnpj = False
                            verificador_cadastro = False
                            continuar = False

                        elif tipo_cpf_cnpj == "2": #caso a instituição esteja vinculada a um CNPJ, essa opção será selecionada
                            cnpj = numero_cnpj()
                            print("-----------------------------------------")
                            print("Nome Funcionário cadastrado: ", nome_funcionario)
                            print("Nome da Instituição Cadastrada: ", instituicao)
                            print("Telefone Celular Cadastrado: ", telefone)
                            print("Endereço Cadastrado da Instituição: ", endereco)
                            print("Número CNPJ vinculado ao cadastro da Instituição: ", cnpj)
                            print("-----------------------------------------")
                            verificador_cpf_cnpj = False 
                            verificador_cadastro = False
                            continuar = False

                        else: #verifica entrada de dados e enquanto não for selecionada uma opção válida, a repetição se mantêm
                            print("Opção inválida! Digite 1 para cadastro com CPF ou digite 2 para cadastro com CNPJ")

                elif tipo_cadastro == "2": #opção para cadastro do feirante na plataforma, o mesmo irá registrar alimentos para doação
                    nome_feirante = coleta_nome_feirante()
                    nascimento = data_nascimento_feirante()
                    cpf = numero_cpf()
                    endereco = endereco_feira()
                    mapa = certificado_MAPA()
                    print("-----------------------------------------")
                    print("Nome Cadastrado do Feirante: ", nome_feirante)
                    print("Data de Nascimento Cadastrada: ", nascimento)
                    print("CPF Cadastrado - Feirante: ", cpf)
                    print("Endereço Cadastro - Feirante: ", endereco)
                    print("Número de Certificação MAPA cadastrado: ", mapa)
                    print("-----------------------------------------")
                    verificador_cadastro = False
                    continuar = False
                else:#verifica entrada de dados e enquanto não for selecionada uma opção válida, a repetição referente ao cadastro se mantêm
                    print("Opção inválida! Digite 1 para cadastro de Instituição ou digite 2 para cadastro Feirante")
                    verificador_cadastro = True
                
                if verificador_cadastro == False: #verificador referente ao cadastro
                    resposta_cadastro = input("Deseja cadastrar/recadastrar outras informações? S/N ")
                    if resposta_cadastro.lower() != "s":            
                        verificador_cadastro = False
                        print("Agradecemos o cadastro!")
        else:
            print("-----------------------------------------")
            print("Número selecionado inválido!!") 
            print("-----------------------------------------")           
            continuar = True

        if continuar == False:                 
            resposta = input("Deseja doar, receber alimentos ou se cadastrar novamente? S/N ")
            if resposta.lower() != "s":            
                continuar = False
                print("Espero termos ajudado, obrigado pelo acesso!")
            else:
                continuar = True
else:
    print("Agradecemos contato, permanecemos à disposição!")
