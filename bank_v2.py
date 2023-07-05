menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def print_extrato(extrato):
    print("==============EXTRATO=======================\n")
    for i, j in extrato:
        if i == 'Saque':
            print(f"{i} : R$ {-j:.2f}")
        else:
            print(f"{i} : R$ {j:.2f}")
    print(f"Saldo: R$ {saldo:.2f} \n")
    print("=============================================\n")

def depositar(saldo, valor, extrato,/):
    if valor <= 0:
        print("Não é possível efetuar o depósito deste valor, tente novamente")
    else:
        saldo += valor
        extrato.append(['Depósito', valor])

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Não é possível efetuar o saque deste valor, tente novamente")
    elif saldo < valor:
        print("Você não possui saldo suficiente para efetuar esta operação!")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Você excedeu o limite de saque diário de {LIMITE_SAQUES}!")
    elif valor > limite:
        print(f"Você excedeu o limite de valor de saque: {limite}!")
    else:
        saldo -= valor
        extrato.append(['Saque', valor])
        numero_saques += 1

    return saldo, extrato


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
  
        valor = float(input("Qual valor deseja depositar?"))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        print("Saque")
        valor = float(input("Qual valor deseja sacar?"))

        saldo, extrato = sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            limite=limite, 
            numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES
            )


    elif opcao == "e":
        print_extrato(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
