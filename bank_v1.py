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
    for i, j in extrato:
        if i == 'Saque':
            print(f"{i} : {-j}")
        else:
            print(f"{i} : {j}")
    print(f"Saldo: {saldo}")

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
  
        valor = float(input("Qual valor deseja depositar?"))

        if valor <= 0:
            print("Não é possível efetuar o depósito deste valor, tente novamente")
        else:
            saldo += valor
            extrato.append(['Depósito', valor])

    elif opcao == "s":
        print("Saque")
        valor = float(input("Qual valor deseja sacar?"))

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


    elif opcao == "e":
        print_extrato(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
