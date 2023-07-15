"""
    Projeto: Sistema Bancário
    Versão: 1.0.0
    Criado por: Magda G.
    Data: 14/07/2023
    Python 3.11.3
"""

saldo_disponível = 0
saque = 0
qtd_saque = 0
deposito = 0
extrato = ''
LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500

menu = '''
    \nOpções:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    Digite a opção desejada: '''

print(f'{"-"*100}')
print(f'{"Sistema Bancário":^100}')
print(f'{"-"*100}')

while True:
    opcao = int(input(f'{menu}'))

    if opcao == 0:
        break

    elif opcao == 1:
        
        deposito = float(input(f'\nInsira o valor desejado R$ '))

        if deposito <= 0:
            print(f'\nOperação Falhou! Valor informado inválido.')
        else:
            saldo_disponível += deposito
            extrato += f'\nDepósito: R$ {deposito:.2f}'
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
    
    elif opcao == 2:

        excedeu_limite_saque_diario = qtd_saque >= LIMITE_SAQUE

        if excedeu_limite_saque_diario:
            print(f'Você excedeu o limite de saque permitido por dia.')
        
        else:
            
            saque = float(input(f'\nInsira o valor desejado: R$ '))

            possui_saldo = (saldo_disponível != 0) or (saldo_disponível >= saque) 

            valor_informado_invalido = saque <= 0 

            excedeu_valor_saque = saque > VALOR_LIMITE_SAQUE

            if not possui_saldo:
                print(f'Saldo Insuficiente: R$ {saldo_disponível}')

            elif excedeu_valor_saque:
                print(f'Operação não realizada! Valor máximo por saque excedido')

            elif valor_informado_invalido:
                print(f'Operação Falhou! Valor informado inválido.')
            
            else:
                saldo_disponível -= saque
                qtd_saque -= 1
                extrato += f'\nSaque: R$ {saque:.2f}'

                print(f'Saque de R${saque:.2f} realizado com sucesso!')
    
    elif opcao == 3:
        
        print(f'\n{"="*42} {"Extrato":^} {"="*42}')
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f'Saldo: R$ {saldo_disponível:.2f}')
        print(f'\n{"="*(100 - len("Extrato"))}')
    else:
        print(f'Opção inválida! Tente novamente.')