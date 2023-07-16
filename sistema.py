"""
    Projeto: Sistema Bancário
    Versão: 1.0.1
    Criado por: Magda G.
    Data de criação: 14/07/2023
    Data de atualização: 15/07/2023
    Python 3.11.3
"""

def depositar(saldo, extrato, valor):

    if valor <= 0:
        print(f'\nOperação Falhou! Valor informado inválido.')
    else:
        saldo += valor
        extrato += f'\nDepósito: R$ \t{valor:.2f}'
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, numero_saque):

    LIMITE_QTD_SAQUE = 3
    VALOR_LIMITE_SAQUE = 500
    
    excedeu_limite_saque_diario = numero_saque >= LIMITE_QTD_SAQUE

    if excedeu_limite_saque_diario:
        print(f'Você excedeu o limite de saque permitido por dia.')
    
    else:

        possui_saldo = (saldo != 0) or (saldo >= valor) 

        valor_informado_invalido = valor <= 0 

        excedeu_valor_saque = valor > VALOR_LIMITE_SAQUE

        if not possui_saldo:
            print(f'Saldo Insuficiente: R$ {saldo}')

        elif excedeu_valor_saque:
            print(f'Operação não realizada! Valor máximo por saque excedido')

        elif valor_informado_invalido:
            print(f'Operação Falhou! Valor informado inválido.')
        
        else:
            saldo -= valor
            numero_saque += 1
            extrato += f'\nSaque: R$ \t{valor:.2f}'

            print(f'Saque de R${valor:.2f} realizado com sucesso!')

    return saldo, extrato, numero_saque


def exibir_extrato(saldo, /, *, extrato):

    print(f'\n{"="*42} {"Extrato":^} {"="*42}')
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f'\nSaldo: R$ \t{saldo:.2f}')
    print(f'\n{"="*(100 - len("Extrato"))}')


def filtrar_usuario(cpf, usuarios):
    usuario_cadastrado = [ usuario for usuario in usuarios if usuarios["cpf"] == cpf ]

    return usuario_cadastrado[0] if usuario_cadastrado else None


def cadastrar_usuario(lista_usuarios):
    nr_cpf = int(input('\nInforme o número do CPF (somente numeros): '))

    usuario_possui_cadastro = filtrar_usuario(nr_cpf, lista_usuarios)

    if usuario_possui_cadastro:
        print(f'\nJá existe o usuario com o CPF: {nr_cpf}')
        return 
    
    nome_completo = input('\nInforme seu nome completo: ')
    dt_nascimento = input('Informe sua data de nascimento (dd-mm-yyyy): ')
    endereco = input('Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    lista_usuarios.append({"nome":nome_completo, "data_nascimento":dt_nascimento, "cpf":nr_cpf,"logradouro":endereco})

    print(f'Cadastro realizado com sucesso!')


def criar_conta(lista_contas, usuarios):
    AGENCIA = '0001'

    nr_cpf = input('Informe o seu CPF (somente números): ')

    usuario_cadastrado = filtrar_usuario(nr_cpf, usuarios)

    if usuario_cadastrado:
        nr_conta = range(len(lista_contas) + 1, 999999, 1)

        conta = {'usuario':nr_cpf,  'agencia':AGENCIA, 'conta': nr_conta}
    
        return conta
    
    print('Usiario não encontrado! Retornando para menu inicial.')
    
    return None


def mostrar_menu():

    menu = '''
        \nOpções:

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Cadastrar Cliente
        [5] Criar Conta
        [0] Sair

        Digite a opção desejada: '''
    
    return input(menu)


def main():

    print(f'{"-"*100}')
    print(f'{"Sistema Bancário":^100}')
    print(f'{"-"*100}') 


saldo_disponível = 0
qtd_saque = 0
extrato = ''
lista_usuario = []
lista_contas = []


while True:
    main()

    opcao = int(mostrar_menu())

    if opcao == 0:
        break

    elif opcao == 1:
        valor_deposito = float(input(f'\nInsira o valor desejado R$ '))

        retorno_deposito = depositar(saldo_disponível, extrato, valor_deposito)

        saldo_disponível, extrato = retorno_deposito
    
    elif opcao == 2:

        valor_saque = float(input(f'\nInsira o valor desejado: R$ '))
        
        retorno_saque = sacar(saldo = saldo_disponível, valor=valor_saque, extrato= extrato, numero_saque=qtd_saque)
        
        saldo_disponível, extrato, qtd_saque = retorno_saque
    
    elif opcao == 3:
        exibir_extrato(saldo_disponível, extrato=extrato)

    elif opcao == 4:
        cadastrar_usuario(lista_usuario)
    
    elif opcao == 5:
        conta_criada = criar_conta(lista_contas,  lista_usuario)

        if conta_criada:
            lista_contas.append(conta_criada)
       
    else:
        print(f'Opção inválida! Tente novamente.')