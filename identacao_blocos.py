# Identção de blocos de código
# por convenção damos 4 espaços a dentro de cada bloco
# if, funções, métodos e etc. observe o exemplo ao lado
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu money na boca do caixa")
        saldo -= valor
        print("saldo atual = ", saldo)

    print("Obrigado por confiar na gente, tenha um bom dia!\n")


def depositar(valor):
    saldo = 2000
    saldo += valor
    print("Deposito efetuado com sucesso")
    print("Saldo atual = ", saldo)


sacar(100)


depositar(500)
