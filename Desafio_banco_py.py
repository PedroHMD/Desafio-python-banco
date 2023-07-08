import textwrap

# =============================================================================================================================================#
'''Essa função exibe um menu e solicita uma entrada do usuário:
O código começa importando o módulo textwrap, que é usado para formatar o texto no menu. Em seguida, a função menu() é definida.
Dentro da função, uma variável chamada menu é criada e armazena o texto do menu. O texto do menu é formatado usando textwrap.dedent(menu_text). 
Isso remove o espaço em branco comum do início de cada linha do texto do menu, o que facilita a leitura e formatação.
O texto do menu formatado é exibido na tela. A função input() é usada para solicitar uma entrada do usuário. A mensagem exibida é o texto 
do menu formatado. A entrada do usuário é retornada como resultado da função menu(). Em resumo, essa função exibe um menu e solicita que o 
usuário escolha uma opção digitando a letra correspondente. O valor digitado pelo usuário é então retornado como resultado da função.
'''


def menu():
    menu = """\n
    =========| SISTEMA BANCÁRIO |=========
    [1]\tDepositar                    |
    [2]\tSacar                        |
    [3]\tExtrato                      |
    [4]\tNova conta                   |
    [5]\tListar contas                |
    [6]\tNovo usuário                 |
    [0]\tSair                         |
    ======================================
    => Digite a opção: """

    return input(textwrap.dedent(menu))


# =============================================================================================================================================#
# =============================================================================================================================================#
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


# =============================================================================================================================================#
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# =============================================================================================================================================#
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


# =============================================================================================================================================#
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


# =============================================================================================================================================#
# Recebe argumentos apenas por posição "/", tudo que estiver antes do caracter "/"
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


# =============================================================================================================================================#
def sacar(*, saldo, valor, extrato, limite, numero_saques,
          limite_saques):  # Recebe argumentos apenas de forma nomeada (keyword only)
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


# =============================================================================================================================================#
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


''' Função principal chamada main(). O código define algumas variáveis iniciais, como LIMITE_SAQUES, AGENCIA, saldo, limite, extrato, 
numero_saques, usuarios e contas. Em seguida, um loop infinito é iniciado usando o comando "while True". Isso permite que o programa execute 
continuamente até que a opção "q" (sair) seja selecionada. Dentro do loop, a função menu() é chamada para exibir o menu e solicitar a entrada do
usuário. O valor retornado é armazenado na variável "opcao". O código verifica qual opção foi selecionada usando uma estrutura condicional if, 
elif e else:

=> "d" (Depositar), o código solicita ao usuário que informe o valor do depósito. Em seguida, a função depositar() é chamada para atualizar o 
saldo e o extrato com base no valor fornecido.
=> "s" (Sacar), o código solicita ao usuário que informe o valor do saque. Em seguida, a função sacar() é chamada para verificar se o saque 
pode ser realizado com base nos limites definidos e atualizar o saldo e o extrato.
=> "e" (Extrato), a função exibir_extrato() é chamada para exibir o saldo atual e o extrato de transações. Se a opção for "nu" (Novo usuário), 
a função criar_usuario() é chamada para criar um novo usuário e adicioná-lo à lista de usuários.
=> "nc" (Nova conta), o código gera um número de conta com base no número de contas existentes. Em seguida, a função criar_conta() é chamada 
para criar uma nova conta associada aos usuários existentes e adicioná-la à lista de contas.
=> "lc" (Listar contas), a função listar_contas() é chamada para exibir as informações das contas existentes. Se a opção for "q" (Sair), o loop 
é interrompido com o comando break, e o programa termina.
Se nenhuma das opções acima for selecionada, o código exibe uma mensagem de "Operação inválida" e retorna ao início do loop.

Em resumo, a função main() implementa a lógica principal do programa, onde o usuário pode interagir com o sistema bancário através de um menu 
para realizar operações como depósito, saque, exibir extrato, criar usuários, criar contas e listar contas. O loop principal garante que o 
programa continue em execução até que a opção de sair seja escolhida.
'''


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()  # Chama a função menu

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()