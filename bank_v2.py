menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = '0001'

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com este CPF!")
        return
    
    nome = input("Nome Completo:")
    data_nascimento = input("Data de Nascimento (dd-mm-aaa):")
    endereco = input("Informe o endereço: ")

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('usuario criado com sucesso!')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, criação de conta encerrada!")

def listar_contas(contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']} - Numero da CC: {conta['numero_conta']} - Usuario: {conta['usuario']['nome']}")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

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

    elif opcao == 'nu':
        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 'lc':
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
